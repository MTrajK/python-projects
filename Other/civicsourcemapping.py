"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
Date: 2019.04.19
"""


# python default modules
import argparse
import os
import csv
import datetime



def get_args():
    """Gets and parses the arguments and values from the command-line execution.

    Returns:
        Object with arguments (in this case only the config file path)
    """

    # creates a description of the task
    description = 'Takes two tab delimited text files '\
                  'and converts the data into the '\
                  'CivicSource Integration Guide 1.42 format. '\
                  'Requirements: python 3+ (https://www.python.org/downloads/).'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        '-c', 
        '--config',
        default='Config.txt',
        help='path to the config file (default=\'Config.txt\')')
 
    return parser.parse_args()



class CivicSourceMapping(object):
    
    @staticmethod
    def __read_config(config_file):
        """Private method, reads the config file. Config file should be composed of these 3 lines:
            Line 1: the location and name of the Legal Description File
            Line 2: the location and name of the Multiple Years Due File
            Line 3: the location of where to write the output (if the output file should be in the same folder with the script just left an empty line)
            The paths could be relative or absolute paths.

        Parameters:
            config_file: location of the Config file

        Returns:
            Dictionary which contains 3 paths: legal_description_file, multiple_years_due_file and output_file
        """

        restult = {}
        datetime_now = datetime.datetime.now().strftime('%Y-%m-%d')
        output_file_name = 'Delinquency File - GCM - {0}.csv'.format(datetime_now)

        with open(config_file, encoding='utf-8', mode='r') as file:
            restult['legal_description_file'] = file.readline().strip()
            restult['multiple_years_due_file'] = file.readline().strip()
            restult['output_file'] = os.path.join(file.readline().strip(), output_file_name)
        
        return restult



    @staticmethod
    def __read_legal_description(file_path, mapping):
        """Private method, reads 2 fields (TAX ID and LEGAL DESCRIPTION, fields 1 and 6) from the Legal Description File and save those field into the mapping dictionary.
        
        Parameters:
            file_path: location of the Legal Description File
            mapping: mapping directory
        """

        with open(file_path, encoding='utf-8', mode='r') as file:
            reader = csv.reader(file, delimiter='\t')

            # read row by row
            for row in reader:
                tax_id = '88{0}'.format(row[0]) # adds 88 as TAX ID prefix
                legal_description = row[5]

                mapping[tax_id] = {
                    'TAX ID': tax_id,
                    'LEGAL DESCRIPTION': '\"{0}\"'.format(legal_description)
                }



    @staticmethod
    def __read_multiple_years_due(file_path, mapping):
        """Private method, reads all fields (without the months) from the Multiple Years Due File and save those field into the mapping dictionary.
        
        Parameters:
            file_path: location of the Multiple Years Due File
            mapping: mapping directory
        """

        with open(file_path, encoding='utf-8', mode='r') as file:
            reader = csv.reader(file, delimiter='\t')
            columns_names = next(reader)

            tax_years = 0

            # count the number of tax years
            for col in range(len(columns_names)):
                columns_names[col] = columns_names[col].strip()
                if columns_names[col].startswith('TAX YEAR'):
                    tax_years += 1
            
            current_month = datetime.datetime.now().strftime("%B")
            months_by_year = 5

            owner_info = tax_years * months_by_year + tax_years + months_by_year + 2

            # read row by row
            for row in reader:
                tax_id = row[0]

                # ignore this data if there is no legal description for it
                if not tax_id in mapping:
                    continue
                
                mapping[tax_id]['WEB PIN'] = row[1]
                mapping[tax_id]['OWNER NAME 1'] = '\"{0}\"'.format(row[owner_info])
                mapping[tax_id]['OWNER NAME 2'] = '\"{0}\"'.format(row[owner_info + 1])
                mapping[tax_id]['OWNER STREET'] = '\"{0}\"'.format(row[owner_info + 2])
                mapping[tax_id]['OWNER CITY'] = row[owner_info + 3]
                mapping[tax_id]['OWNER STATE'] = row[owner_info + 4]
                mapping[tax_id]['OWNER ZIP'] = row[owner_info + 5]
                mapping[tax_id]['PROPERTY LOCATION'] = '\"{0}\"'.format(row[owner_info + 6])

                # if a number is not supplied, prefix the addresses (OWNER STREET and PROPERTY LOCATION) with a "0" (zero)
                if not mapping[tax_id]['OWNER STREET'][1].isdigit():
                    mapping[tax_id]['OWNER STREET'] = '\"0 {0}'.format(mapping[tax_id]['OWNER STREET'][1:])
                if not mapping[tax_id]['PROPERTY LOCATION'][1].isdigit():
                    mapping[tax_id]['PROPERTY LOCATION'] = '\"0 {0}'.format(mapping[tax_id]['PROPERTY LOCATION'][1:])

                row_idx = 2

                for year in range(1, tax_years + 1):
                    tax_year = {
                        'YEAR': row[row_idx],
                        'AMOUNT': ''
                    }

                    # checks if the current month exist in the file
                    for idx in range(row_idx + 1, row_idx + months_by_year + 1):
                        if columns_names[idx] == current_month:
                            if row[idx].strip() != '':
                                tax_year['AMOUNT'] = row[idx]
                            break

                    if tax_year['AMOUNT'] == '':
                        # uses the last month available if the current month is not useful
                        for idx in range(row_idx + months_by_year, row_idx, -1):
                            if row[idx].strip() != '':
                                tax_year['AMOUNT'] = row[idx]
                                break
                    
                    if tax_year['AMOUNT'] != '':
                        # if there is a value (non-blank) in the month column for the account, creates a REC record with the year and amount
                        mapping[tax_id]['TAX YEAR {0}'.format(year)] = tax_year

                    row_idx += months_by_year + 1
                


    @staticmethod
    def __write_output(file_path, mapping):
        """Private method, reads 2 fields (TAX ID and LEGAL DESCRIPTION, fields 1 and 6) from the Legal Description File and save those field into the mapping dictionary.
        
        Parameters:
            file_path: location of the Output File
            mapping: mapping directory
        """
        
        with open(file_path, 'w', newline='') as file:
            # there are commas in some descriptions, because of that we need to quote these strings
            writer = csv.writer(file, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE, escapechar='\\')
            
            current_date = datetime.datetime.now().strftime('%Y%m%d')

            # The first 4 lines of the file are static
            writer.writerow(['VER', '1.41', 'Property Import'])
            writer.writerow(['RET', 'I', '01', 'Real Estate Tax', '', 'T', 'County', '100.00'])
            writer.writerow(['RET', 'I', '02', 'Tax Sale Cost', '', 'C', 'County', '100.00'])
            writer.writerow(['RET', 'I', '03', 'Monthly Interest', '', 'T', 'County', '100.00'])

            count = 0
            receivable_total = 0

            for tax_id in mapping:
                item = mapping[tax_id]

                if not 'WEB PIN' in item:
                    # ignore all tax_ids that don't contains the informations from Multiple Years Due file
                    continue

                count += 1

                # Account (ACT Record) mapping
                writer.writerow(['ACT', item['TAX ID'], 'I', item['LEGAL DESCRIPTION'], 'U', 'D', current_date])

                # Parcel (PAR Record) mapping
                writer.writerow(['PAR', item['TAX ID'], item['WEB PIN'], '', '', '', '', '', '', 
                    item['PROPERTY LOCATION'], '', '', '', '', '', '', '', '', item['LEGAL DESCRIPTION']])

                # Owner (OWN Record) mapping
                writer.writerow(['OWN', item['TAX ID'], '', 'T', item['OWNER NAME 1'], item['OWNER NAME 2'],
                    item['OWNER STREET'], '', item['OWNER CITY'], item['OWNER STATE'], item['OWNER ZIP'], 
                    '', '', '', '', '', '', '', '', 'T'])

                # Receivable (REC Record) mapping
                for year in range(1, 7):
                    tax_year = 'TAX YEAR {0}'.format(year)

                    if not tax_year in item:
                        # no record for this tax year
                        continue
                    
                    amount = item[tax_year]['AMOUNT']
                    receivable_total += float(amount)

                    writer.writerow(['REC', item['TAX ID'], item[tax_year]['YEAR'], '01',
                        '1', amount, '', '', '', amount, ''])

            # Totals (TOT Record) mapping
            writer.writerow(['TOT', count, '{0:.2f}'.format(round(receivable_total,2)), '0.00'])



    @staticmethod
    def execute(config_file):
        """The main method (public), converts two tab delimited text files into csv file with CivicSource Integration Guide 1.42 format.
        
        Workflow:
            1. Reads and parses the paths from the config.txt
            2. Creates a mapping dictionary where the key will be TAX ID
            3. Reads the Legal Description File and maps the data into the mapping dictionary
            4. Reads the Multiple Years Due File and maps the data into the mapping dictionary
            5. Writes the results from the mapping dictionary into the output csv file

        Parameters:
            config_file: location of the config file (relative or absolute path)
        """

        paths = CivicSourceMapping.__read_config(config_file)

        mapping = {}
        
        CivicSourceMapping.__read_legal_description(paths['legal_description_file'], mapping)

        CivicSourceMapping.__read_multiple_years_due(paths['multiple_years_due_file'], mapping)

        CivicSourceMapping.__write_output(paths['output_file'], mapping)
        


if __name__ == "__main__":
    """The script starts here"""
    
    args = get_args()
    
    CivicSourceMapping.execute(args.config)

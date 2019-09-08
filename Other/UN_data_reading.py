"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
"""

import csv
import os
import math

"""
for easily data manipulation, the data dictionaries will be structured like this
data = {
    id : {
        name: XXXX,
        // all series like keys, for example:
        'Population annual rate of increase (percent)': // list of all years
        [
            {
                year: YYYY,
                value: ZZ,
                footnotes: WWWWWWWWWWWWWW
            },
            ...
        ],
        ...
    },
    ...
}
"""
data_by_region = {}
data_by_country = {}
# in the answers array we'll store the questions and answers like tuples (question, answer)
answers = []
"""
How to get all regions and IDs?
Go to - http://data.un.org/
Right click anywhere and click "Inspect element"
In the console, copy-paste this JavaScript script and press enter:

allRegions = document.querySelectorAll(".CountryList")[1].children[0].children
nRegions = allRegions.length
dictRegions = {}

for (i=1; i<nRegions; i++) {
	a = allRegions[i].children[0]
	first = a.href.lastIndexOf("g") + 1
	last = a.href.length - 5

	id = a.href.substring(first, last)
	region = a.innerText
    
	dictRegions[id] = region
}

console.log(dictRegions)
"""
nor_region_country = {
    1: "Total, all countries or areas",
    158: "Other non-specified areas"
}
regions = {
    2: "Africa", 
    5: "South America", 
    9: "Oceania", 
    11: "Western Africa", 
    13: "Central America", 
    14: "Eastern Africa", 
    15: "Northern Africa", 
    17: "Middle Africa", 
    18: "Southern Africa", 
    19: "Americas", 
    21: "Northern America", 
    29: "Caribbean", 
    30: "Eastern Asia", 
    34: "Southern Asia", 
    35: "South-eastern Asia", 
    39: "Southern Europe", 
    53: "Australia and New Zealand", 
    54: "Melanesia", 
    57: "Micronesia", 
    61: "Polynesia", 
    142: "Asia", 
    143: "Central Asia", 
    145: "Western Asia", 
    150: "Europe", 
    151: "Eastern Europe", 
    154: "Northern Europe", 
    155: "Western Europe", 
    202: "Sub-Saharan Africa", 
    419: "Latin America & the Caribbean"
}

def load_dictionaries():
    """ Reads the data from the data.csv file and fill the dictionaries.
    """
    global data_by_region
    global data_by_country

    # oped the data.csv file for reading and fill data_by_region and data_by_country
    data_file = os.path.dirname(os.path.abspath(__file__)) + '\\data.csv'
    
    with open(data_file, encoding='utf-8', mode='r') as file:
        reader = csv.reader(file)
        next(reader) # ignore the column's names

        # read row by row
        for row in reader:
            row_id = int(row[0])
            
            # check if this is a region, a country or the nor_region_country's data
            if row_id in nor_region_country:
                continue # ignore the nor_region_country's data
            elif row_id in regions:
                insert_item_in_dict(data_by_region, row)
            else:
                insert_item_in_dict(data_by_country, row)

def write_answers(answers):
    """ Writes the answers into UIN_answers.txt file.

    Parameters:
        answers: list with strings. 
    """
    # oped the data.csv file for reading and fill data_by_region and data_by_country
    write_file = os.path.dirname(os.path.abspath(__file__)) + '\\UIN_answers.txt'
    
    with open(write_file, encoding='utf-8', mode='w') as file:
        # writes all answers with the questions
        for i in range(len(answers)):
            print('{0}. {1} - {2}'.format(str(i + 1), answers[i][0], answers[i][1]), file=file)

def insert_item_in_dict(data_dict, data_item):
    """ Inserts an item into a dictionary.

    Parameters:
        data_dict: dictionary with different data for regions or countries.
        data_item: the item that needs to be inserted.
    """
    data_id = int(data_item[0])
    data_name = data_item[1]
    data_year = int(data_item[2])
    data_series = data_item[3]
    data_value = float(str(data_item[4]).replace(',', '.'))
    data_footnotes = data_item[5]
    data_object = {
        'year': data_year,
        'value': data_value,
        'footnotes': data_footnotes
    }

    if not data_id in data_dict:
        # checks if ID exists in the dictionary
        data_dict[data_id] = {
            'name': data_name,
            data_series: [data_object]
        }
    elif not data_series in data_dict[data_id]:
        # checks if SERIES exists in the dictionary
        data_dict[data_id][data_series] = [data_object]
    else:
        # checks if YEAR exists in the dictionary
        found = False

        for ds in data_dict[data_id][data_series]:
            if ds['year'] == data_year:
                found = True
                break
        
        if not found:
            data_dict[data_id][data_series].append(data_object)

def largest_numeric_decrease_maternal_mortality(data_by_region):
    """ Which region had the largest numeric decrease in Maternal mortality ratio from 2005 to 2015?

    Parameters:
        data_by_region: dictionary with different data for regions.
    
    Returns:
        Tuple(String, String) - (Question, region name).
    """
    data_series = 'Maternal mortality ratio (deaths per 100,000 population)'
    
    start_year = 2005
    end_year = 2015

    smallest = math.inf
    result = ''

    for ID in data_by_region:
        if data_series in data_by_region[ID]:
            # finds all data between 2005 and 2015
            everything_between = []

            for data in data_by_region[ID][data_series]:
                if data['year'] >= start_year and data['year'] <= end_year:
                    everything_between.append(data)
            
            # finds the numeric difference between the maternal mortality from the max and min year
            if len(everything_between) > 1:
                max_year = max(everything_between, key=lambda d: d['year'])
                min_year = min(everything_between, key=lambda d: d['year'])
                diff = max_year['value'] - min_year['value']

                if diff < smallest:
                    smallest = diff
                    result = data_by_region[ID]['name']

    return ('Which region had the largest numeric decrease in Maternal mortality ratio from 2005 to 2015?', result)

def largest_percentage_decrease_maternal_mortality(data_by_region):
    """ Which region had the largest percentage decrease in Maternal mortality ratio from 2005 to 2015?

    Parameters:
        data_by_region: dictionary with different data for regions.
    
    Returns:
        Tuple(String, String) - (Question, region name).
    """
    data_series = 'Maternal mortality ratio (deaths per 100,000 population)'

    start_year = 2005
    end_year = 2015

    smallest = math.inf
    result = ''

    for ID in data_by_region:
        if data_series in data_by_region[ID]:
            # finds all data between 2005 and 2015
            everything_between = []

            for data in data_by_region[ID][data_series]:
                if data['year'] >= start_year and data['year'] <= end_year:
                    everything_between.append(data)
            
            # finds the percentage difference between the maternal mortality from the max and min year
            if len(everything_between) > 1:
                max_year = max(everything_between, key=lambda d: d['year'])
                min_year = min(everything_between, key=lambda d: d['year'])
                diff = max_year['value'] / min_year['value']

                if diff < smallest:
                    smallest = diff
                    result = data_by_region[ID]['name']

    return ('Which region had the largest percentage decrease in Maternal mortality ratio from 2005 to 2015?', result)

def largest_numeric_increase_life_expectancy(data_by_region):
    """ Which region had the largest numeric increase in Life expectancy at birth for both sexes from 2005 to 2015?

    Parameters:
        data_by_region: dictionary with different data for regions.
    
    Returns:
        Tuple(String, String) - (Question, region name).
    """
    data_series = 'Life expectancy at birth for both sexes (years)'

    start_year = 2005
    end_year = 2015

    largest = -math.inf
    result = ''

    for ID in data_by_region:
        if data_series in data_by_region[ID]:
            # finds all data between 2005 and 2015
            everything_between = []

            for data in data_by_region[ID][data_series]:
                if data['year'] >= start_year and data['year'] <= end_year:
                    everything_between.append(data)
            
            # finds the numeric difference between the life expectancy from the max and min year
            if len(everything_between) > 1:
                max_year = max(everything_between, key=lambda d: d['year'])
                min_year = min(everything_between, key=lambda d: d['year'])
                diff = max_year['value'] - min_year['value']

                if diff > largest:
                    largest = diff
                    result = data_by_region[ID]['name']

    return ('Which region had the largest numeric increase in Life expectancy at birth for both sexes from 2005 to 2015?', result)

def largest_numeric_decrease_infant_mortality(data_by_country):
    """ Which country had the largest decrease in Infant mortality for both sexes from 2005 to 2015?

    Parameters:
        data_by_country: dictionary with different data for countries.
    
    Returns:
        Tuple(String, String) - (Question, country name).
    """
    data_series = 'Infant mortality for both sexes (per 1,000 live births)'

    start_year = 2005
    end_year = 2015

    smallest = math.inf
    result = ''

    for ID in data_by_country:
        if data_series in data_by_country[ID]:
            # finds all data between 2005 and 2015
            everything_between = []

            for data in data_by_country[ID][data_series]:
                if data['year'] >= start_year and data['year'] <= end_year:
                    everything_between.append(data)
            
            # finds the difference between the mortality from the max and min year
            if len(everything_between) > 1:
                max_year = max(everything_between, key=lambda d: d['year'])
                min_year = min(everything_between, key=lambda d: d['year'])
                diff = max_year['value'] - min_year['value']

                if diff < smallest:
                    smallest = diff
                    result = data_by_country[ID]['name']

    return ('Which country had the largest decrease in Infant mortality for both sexes from 2005 to 2015?', result)

def largest_numeric_increase_infant_mortality(data_by_country):
    """ Which country had the largest increase in Infant mortality for both sexes from 2005 to 2015?

    Parameters:
        data_by_country: dictionary with different data for countries.
    
    Returns:
        Tuple(String, String) - (Question, country name).
    """
    data_series = 'Infant mortality for both sexes (per 1,000 live births)'
    start_year = 2005
    end_year = 2015

    largest = -math.inf
    result = ''

    for ID in data_by_country:
        if data_series in data_by_country[ID]:
            # finds all data between 2005 and 2015
            everything_between = []

            for data in data_by_country[ID][data_series]:
                if data['year'] >= start_year and data['year'] <= end_year:
                    everything_between.append(data)
            
            # finds the difference between the infant mortality from the max and min year
            if len(everything_between) > 1:
                max_year = max(everything_between, key=lambda d: d['year'])
                min_year = min(everything_between, key=lambda d: d['year'])
                diff = max_year['value'] - min_year['value']

                if diff > largest:
                    largest = diff
                    result = data_by_country[ID]['name']

    return ('Which country had the largest increase in Infant mortality for both sexes from 2005 to 2015?', result)

def largest_total_fertility_2015(data_by_country):
    """ Which country had the largest Total fertility rate in 2015?

    Parameters:
        data_by_country: dictionary with different data for countries.
    
    Returns:
        Tuple(String, String) - (Question, country name).
    """
    data_series = 'Total fertility rate (children per women)'
    year = 2015

    largest = -math.inf
    result = ''

    for ID in data_by_country:
        if data_series in data_by_country[ID]:
            # finds the 2015 year and checks if this is the largest Total fertility rate
            for data in data_by_country[ID][data_series]:
                if data['year'] == year:
                    if data['value'] > largest:
                        largest = data['value']
                        result = data_by_country[ID]['name']
                    break

    return ('Which country had the largest Total fertility rate in 2015?', result)

def smallest_total_fertility_2015(data_by_country):
    """ Which country had the smallest Total fertility rate in 2015?

    Parameters:
        data_by_country: dictionary with different data for countries.
    
    Returns:
        Tuple(String, String) - (Question, country name).
    """
    data_series = 'Total fertility rate (children per women)'
    year = 2015

    smallest = math.inf
    result = ''

    for ID in data_by_country:
        if data_series in data_by_country[ID]:
            # finds the 2015 year and checks if this is the smallest Total fertility rate
            for data in data_by_country[ID][data_series]:
                if data['year'] == year:
                    if data['value'] < smallest:
                        smallest = data['value']
                        result = data_by_country[ID]['name']
                    break
            
    return ('Which country had the smallest Total fertility rate in 2015?', result)

def main():
    load_dictionaries()

    global answers
    global data_by_region
    global data_by_country
    
    answers = [
        largest_numeric_decrease_maternal_mortality(data_by_region),
        largest_percentage_decrease_maternal_mortality(data_by_region),
        largest_numeric_increase_life_expectancy(data_by_region),
        largest_numeric_decrease_infant_mortality(data_by_country),
        largest_numeric_increase_infant_mortality(data_by_country),
        largest_total_fertility_2015(data_by_country),
        smallest_total_fertility_2015(data_by_country)
    ]
    
    write_answers(answers)

main()

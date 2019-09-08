"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
Date: 2019.04.25
"""


# python default modules
import argparse
import os
import glob
import sys
import logging
import csv
import datetime
import re

# gevent module
import gevent

# ebaysdk modules
from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError



def get_default_paths():
    """Returns the paths for log and output directories, depends on the OS (Windows, Linux).

    Returns:
        Object with 2 paths, for log and output directory.
    """
    
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # Linux
        output = ['~']
        log = ['~', 'log']
    elif sys.platform == 'win32':
        # Windows
        output = ['~', 'Downloads']
        log = ['~', 'Downloads', 'log']
    else:
        # Mac or something else
        raise Exception('Not supported OS!')

    return {
        'output': os.path.expanduser(os.sep.join(output)),
        'log': os.path.expanduser(os.sep.join(log))
    }



def get_args():
    """Parses the arguments and values from the script user.

    Returns:
        Object with arguments (output directory, log directory, delimiter, seller id, maximum parallel api calls)
    """

    # find the output and log default directories
    paths = get_default_paths()

    # create description of task
    description = 'Extracts a list of active '\
                  'eBay listings from a eBay seller '\
                  'using the eBay API. '\
                  'Requirements: python 3+ (https://www.python.org/downloads/), '\
                  'gevent (pip install gevent) '\
                  'and ebaysdk (pip install ebaysdk).'
    parser = argparse.ArgumentParser(description=description)

    # add string type argument
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=paths['output'],
        help='full path to output directory (without the name of the output file)')
    parser.add_argument(
        '-l',
        '--log',
        type=str,
        default=paths['log'],
        help='full path to log directory (without the name of the log file)')
    parser.add_argument(
        '-f', 
        '--file',
        default='ebay.yaml',
        help='path to eBay yaml file (API keys file) (default=\'ebay.yaml\', first looks into the current directory after that into the home)')
    parser.add_argument(
        '-d',
        '--delimiter',
        type=str,
        default=',',
        help='delimiter for the output file ("," for CSV files, "\\t" for TSV files, everything else for TXT files)  (default=\',\')')
    
    # add int type argument
    parser.add_argument(
        '-c',
        '--calls',
        type=int,
        default=10,
        help='maximum parallel API calls (default=10, max=18 suggested by eBay)')
    parser.add_argument(
        '-m',
        '--months',
        type=int,
        default=36,
        help='max months in the past for item searching (default=36)')
    parser.add_argument(
        '-x',
        '--xdays',
        type=int,
        default=90,
        help='get all items older than last sale or listing start date if no sales (default=90)')

    # add action_store/boolean type argument
    parser.add_argument(
        '-p',
        '--preserve',
        action='store_true',
        help='preserve previous versions of the output (without this arg the previous versions are removed)')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='verbose logging (console and log file) (without this arg there is no logging)')
    parser.add_argument(
        '-s',
        '--sort',
        action='store_true',
        help='sorts the items in ascending order (without this arg items will be in descending order, the item with the oldest sale will be first)')


    return parser.parse_args()



def create_logger(args):
    """Creates a logger (file and console logger) (if verbose is True).

    Parameters:
        args: Object with arguments (log file directory, verbose)

    Returns:
        Function which logs in 2 places (in the file and in the console).
    """

    if args.verbose:
        # logger formatting
        fmt = '%(asctime)s - %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        level = logging.INFO

        # if at least one directory doesn't exist from the path, create all directories from the given output path
        if not os.path.isdir(args.log):
            os.makedirs(args.log)

        # add the current datetime to the file name
        datetime_now = datetime.datetime.now().strftime('%Y_%m_%d-%H-%M-%S')
        file_name = 'ebaylistings-log_{0}.log'.format(datetime_now)
        file = os.path.join(args.log, file_name)

        # create a file logger and configure the way of logging
        file_handler = logging.FileHandler(file)        
        file_handler.setFormatter(formatter)

        file_logger = logging.getLogger('file_logger')
        file_logger.setLevel(level)
        file_logger.addHandler(file_handler)

        # create a console logger and configure the way of logging
        console_handler = logging.StreamHandler(sys.stdout)        
        console_handler.setFormatter(formatter)

        console_logger = logging.getLogger('console_logger')
        console_logger.setLevel(level)
        console_logger.addHandler(console_handler)
    
    # create a function to log message in the file and in the console
    def log(message):
        if args.verbose:
            file_logger.info(message)
            console_logger.info(message)

    return log



def remove_outputs(args):
    """Removes the previous output versions (if args.preserve is False).

    Parameters:
        args: Object with arguments (output file directory, preserve)
    """

    if not args.preserve:
        # removes all files from the output directory which names starts with 'ebaylistings_'
        remove_all = os.path.join(args.output, 'ebaylistings_*')

        for file in glob.glob(remove_all):
            os.remove(file)



def __parse_helper(dur, dur_dict):
    """Helper function for __parse_iso_duration"""

    key = re.split('[0-9]+', dur)[1:]
    value = re.split('[A-Z]+', dur)[:-1]

    for i in range(len(key)):
        dur_dict[key[i]] = int(value[i])
    


def __parse_iso_duration(duration):
    """Parses ISO 8601 duration format (P(n)Y(n)M(n)DT(n)H(n)M(n)S) into Y-M-D h:m:s format.

    Parameters:
        duration: Object with arguments (output directory, seller id, maximum parallel api calls)

    Returns:
        Duration in Y-M-D h:m:s format.
    """

    durs = duration.replace('P', '').split('T')

    duration_period = {
        'Y': 0,
        'M': 0,
        'D': 0 
    }
    __parse_helper(durs[0], duration_period)

    duration_time = {
        'H': 0,
        'M': 0,
        'S': 0
    }
    __parse_helper(durs[1], duration_time)

    return '{0}-{1}-{2} {3}:{4}:{5}'.format(duration_period['Y'], duration_period['M'], 
        duration_period['D'], duration_time['H'], duration_time['M'], duration_time['S'])



def ebay_listings(args, logger):
    """The function with the main logic for this script.

    Parameters:
        args: Object with arguments (output directory, seller id, maximum parallel api calls)
        logger: Function used for logging.
    """

    # names of the required fields 
    fieldnames=[
        'Item ID',
        'Title',
        'Total Sales',
        'Views',
        'Watchers',
        'Start Date',
        'End Date',
        'Time Left',
        'Days Since Last Sale'
    ]

    # if at least one directory doesn't exist from the path, create all directories from the given output path
    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    
    # checks if the file with keys is located in appdata/local on windows OS
    api_keys = args.file
    if (sys.platform == 'win32') and (not os.path.isfile(api_keys)):  
        local_appdata = os.path.expandvars(r'%LOCALAPPDATA%')
        full_path = os.path.expanduser(os.sep.join([local_appdata, api_keys]))
        
        if os.path.isfile(full_path):
            api_keys = full_path

    # add the current datetime to the file name
    datetime_now = datetime.datetime.now().strftime('%Y_%m_%d-%H-%M-%S')
    output_name = 'ebaylistings_{0}'.format(datetime_now)
    output_file = os.path.join(args.output, output_name)

    # check the delimiter and add the appropriate extension to the output file
    if args.delimiter == ',':
        # Comma Separated Values
        output_file += '.csv'
    elif args.delimiter == '\t':
        # Tab Separated Values
        output_file += '.tsv'
    else:
        # There is no file types for the rest delimiters, so use the TXT file
        output_file += '.txt'

    # create and open the output file for writing
    with open(output_file, 'w', newline='') as write_file:
        logger('The output file is created and opened for writing: {0}'.format(output_file))
        
        items_counter = 0

        # create a writer with wanted delimiter
        writer = csv.DictWriter(write_file, delimiter=args.delimiter, fieldnames=fieldnames)
        # write the header of file
        writer.writeheader()

        try:
            # configure the trading api
            trading_api = Trading(config_file=api_keys)

            # paging constants
            START_PAGE = 1 # starts from 1
            MAX_PAGING_ITEMS = 50 # max 200, fails often with 200 (the PC can't read that info in 20 sec)
            MAX_PAGING_TRANSACTIONS = 10 # max 200, no need from all of them, we need only the last transaction
            MAX_TIMEOUT = 120 # seconds

            intervals = []
            items = []
            items_dict = {}

            current_datetime = datetime.datetime.now(datetime.timezone.utc)
            datetime_iter = current_datetime - datetime.timedelta(days=args.xdays)

            # convert current_datetime from offset-aware to offset-naive
            current_datetime_str = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
            current_datetime_offset_naive = datetime.datetime.strptime(current_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            # creates all intervals
            # one iteration takes all items in range of 30 days (1 month)
            for i in range(args.months):
                # the oldest date
                datetime_from = (datetime_iter - datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
                # the most recent date
                datetime_to = datetime_iter.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
                
                interval = {
                    'PageNumber': START_PAGE,
                    'StartTimeFrom': datetime_from,
                    'StartTimeTo': datetime_to
                }
                intervals.append(interval)
                datetime_iter = (datetime_iter - datetime.timedelta(days=30))


            # go through all intervals and find all items
            # parallel execution, using the gevent
            while len(intervals) > 0:
                
                # handle the GEVENT's "The read operation timed out" exception
                try:
                    intervals_count = min(len(intervals), args.calls)
                    # leave all left intervals for the next cycle
                    leftIntervals = intervals[intervals_count:]

                    # max 120 sec to execute all parallel API calls
                    timeout = gevent.Timeout(MAX_TIMEOUT)
                    timeout.start()

                    calls = []

                    # get all irems in parallel
                    for i in range(intervals_count):
                        interval = intervals[i]

                        items_params = {
                            'Pagination': {
                                'EntriesPerPage': MAX_PAGING_ITEMS,
                                'PageNumber': interval['PageNumber']
                            },
                            'StartTimeFrom': interval['StartTimeFrom'],
                            'StartTimeTo': interval['StartTimeTo'],
                            'IncludeWatchCount': 'true',
                            'GranularityLevel': 'Fine',
                            'OutputSelector': [
                                'PageNumber',
                                'HasMoreItems',
                                'ItemArray.Item.SellingStatus.ListingStatus',
                                'ItemArray.Item.SellingStatus.QuantitySold',
                                'ItemArray.Item.HitCount',
                                'ItemArray.Item.WatchCount',
                                'ItemArray.Item.Title',
                                'ItemArray.Item.TimeLeft',
                                'ItemArray.Item.ItemID',
                                'ItemArray.Item.ListingDetails.StartTime',
                                'ItemArray.Item.ListingDetails.EndTime',
                            ]
                        }
                        # add this call to gevent parallel execution
                        # call GetSellerList API
                        call = gevent.spawn(trading_api.execute, 'GetSellerList', items_params)
                        calls.append(call)
                    
                    # wait for all API calls to finsih
                    gevent.joinall(calls)
                    timeout.cancel()

                except Exception as e:
                    # GEVENTs "The read operation timed out" exception, try again!
                    logger('GetSellerList exception: {0}'.format(str(e)))
                    continue

                # check all of the results from the parallel calls
                for i in range(len(calls)):
                    logger('GetSellerList API executed.')

                    call = calls[i].get().dict()

                    # parse items from the response
                    if call['ItemArray'] != None:
                        call_items = call['ItemArray']['Item']
                        if type(call_items) is dict: # checks if there is only one item
                            call_items = [call_items]

                        for item in call_items:
                            # we need only the active listings
                            if item['SellingStatus']['ListingStatus'] != 'Active':
                                continue

                            item_id = item['ItemID']

                            # ignore duplicates
                            if item_id in items_dict:
                                continue
                            
                            quantity_sold = 0
                            if ('QuantitySold' in item['SellingStatus']) and (item['SellingStatus']['QuantitySold'] != None):
                                quantity_sold = int(item['SellingStatus']['QuantitySold'])

                            hit_count = None
                            if 'HitCount' in item:
                                hit_count = item['HitCount']

                            watch_count = None
                            if 'WatchCount' in item:
                                watch_count = item['WatchCount']

                            start_time = datetime.datetime.strptime(item['ListingDetails']['StartTime'], "%Y-%m-%dT%H:%M:%S.%fZ")  # convert to offset-naive
                            diff_delta = current_datetime_offset_naive - start_time

                            parsed_item = {
                                'DaysSinceLastSale': diff_delta.days,
                                'PageNumber': START_PAGE,
                                'HitCount': hit_count,
                                'WatchCount': watch_count,
                                'TimeLeft': item['TimeLeft'],
                                'EndTime': item['ListingDetails']['EndTime'],
                                'StartTime': item['ListingDetails']['StartTime'],
                                'QuantitySold': quantity_sold,
                                'Title': item['Title'],
                                'ItemID': item_id
                            }
                            items_dict[item_id] = parsed_item
                            items.append(parsed_item)

                        if call['HasMoreItems'] == 'true':
                            # find the right interval from the intervals, update and append it to leftInterval
                            updated_interval = intervals[i]
                            updated_interval['PageNumber'] = int(call['PageNumber']) + 1
                            leftIntervals.append(updated_interval)

                # update the intervals for the next cycle
                intervals = leftIntervals

    
            # array with all items (final results)
            results = []


            # go through all items and find the last sale/transaction
            # parallel execution, using the gevent
            items_idx = 0
            
            while items_idx < len(items):
                # save the start item_idx and how many new results are added, in case if the parallel execution fails
                start_item_idx = items_idx
                added_results = 0

                # handle the GEVENT's "The read operation timed out" exception
                try:
                    # max 120 sec to execute all parallel API calls
                    timeout = gevent.Timeout(MAX_TIMEOUT)
                    timeout.start()

                    calls = []

                    # get all transactions for items (items that have more than 0 sales) in parallel
                    while (len(calls) < args.calls) and (items_idx < len(items)):
                        item = items[items_idx]
                        items_idx += 1

                        # no need to search for transactions if there are 0 sold items
                        if item['QuantitySold'] > 0:
                            transactions_params = {
                                'ItemID': item['ItemID'],
                                'Pagination': {
                                    'EntriesPerPage': MAX_PAGING_TRANSACTIONS,
                                    'PageNumber': item['PageNumber']
                                },
                                'GranularityLevel': 'Fine',
                                'OutputSelector': [
                                    'HasMoreTransactions',
                                    'PaginationResult.TotalNumberOfPages',
                                    'TransactionArray.Transaction.CreatedDate',
                                    'Item.ItemID'
                                ]
                            }
                            # add this call to gevent parallel execution
                            # call GetItemTransactions API
                            call = gevent.spawn(trading_api.execute, 'GetItemTransactions', transactions_params)
                            calls.append(call)
                        else:
                            # add this item into the results array
                            results.append(item)
                            added_results += 1

                    # wait for all API calls to finsih
                    gevent.joinall(calls)
                    timeout.cancel()
                
                except Exception as e:
                    # GEVENTs "The read operation timed out" exception, try again!
                    logger('GetItemTransactions exception: {0}'.format(str(e)))
                    # reset results and item_idx
                    results = results[:len(results)-added_results]
                    items_idx = start_item_idx
                    continue


                # check all of the results from the parallel calls
                for c in calls:
                    logger('GetItemTransactions API executed.')

                    call = c.get().dict()
                    itemID = call['Item']['ItemID']
                    item = items_dict[itemID]

                    if ('TransactionArray' in call) and ('Transaction' in call['TransactionArray']):
                        call_transactions = call['TransactionArray']['Transaction']
                        if type(call_transactions) is dict: # checks if there is only one transaction
                            call_transactions = [call_transactions]
                        
                        created_date_str = call_transactions[-1]['CreatedDate'] # get last
                        created_date = datetime.datetime.strptime(created_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")  # convert to offset-naive
                        diff_delta = current_datetime_offset_naive - created_date
                        item['DaysSinceLastSale'] = diff_delta.days

                    # if there are more transactions, execute again (using pagination to find the last transaction)
                    if call['HasMoreTransactions'] == 'true':
                        item['PageNumber'] = int(call['PaginationResult']['TotalNumberOfPages']) # go to the last page
                        items.append(item)
                    else:
                        if item['DaysSinceLastSale'] <= args.xdays:
                            # add this item into the results array if it is older than xdays
                            results.append(item)

            # remove the duplicates (just in case)
            unique_results = {}
            for item in results:
                if not item['ItemID'] in unique_results:
                    unique_results[item['ItemID']] = item
            
            results = []
            for key in unique_results:
                results.append(unique_results[key])

            # sort the results
            results = sorted(results, key=lambda k: k['DaysSinceLastSale'], reverse=(not args.sort)) 
            
            # write the results into the output file
            for item in results:
                
                time_left = __parse_iso_duration(item['TimeLeft'])

                hit_count = '0'
                if item['HitCount'] != None:
                    hit_count = item['HitCount']

                watch_count = '0'
                if item['WatchCount'] != None:
                    watch_count = item['WatchCount']

                item_id = item['ItemID']
                title = item['Title'].replace(args.delimiter, '')
                quantity_sold = item['QuantitySold']
                start_date = item['StartTime']
                end_date = item['EndTime']
                days_sience_last_sale = item['DaysSinceLastSale']

                writer.writerow({
                    'Item ID': item_id,
                    'Title': title,
                    'Total Sales': quantity_sold,
                    'Views': hit_count,
                    'Watchers': watch_count,
                    'Start Date': start_date,
                    'End Date': end_date,
                    'Time Left': time_left,
                    'Days Since Last Sale': days_sience_last_sale
                })

                items_counter += 1
                logger('{0}. Item with ID {1} succesfully written'.format(items_counter, item_id))


        except ConnectionError as e:
            logger('CONNECTION ERROR : {0}'.format(e.message))
            raise e

        except Exception as e:
            logger('ERROR : {0}'.format(str(e)))
            raise e
        
        # success
        logger('{0} active eBay listings are successfully received and saved'.format(items_counter))



if __name__ == "__main__":
    """The script starts here.

    Workflow:
    1. Gets and parses the arguments from the command-line execution.
    2. Creates a logger, logs in 2 places: log file and console.
    3. Removes the previous output versions.  
    4. Ebay listings, gets results from the eBay API.
    """

    # get and parse the arguments
    args = get_args()
    
    # create a logger
    logger = create_logger(args)

    # remove older outputs
    remove_outputs(args)

    try:
        # call the ebay listings method
        ebay_listings(args, logger)
    except:
        logger('An error occurred, not all eBay listings are successfully received and saved')

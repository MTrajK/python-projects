"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
Last update: 2019.05.03
"""


# python default modules
import argparse
import os
import sys
import logging
import datetime

# requests module
import requests



def get_default_paths():
    """Returns the paths for credentials file and log directory, depends on the OS (Windows, Linux).

    Returns:
        Object with 2 paths, for credentials file and log directory.
    """
    
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # Linux
        credentials_file = ['~']
        log = ['~', 'log']
    elif sys.platform == 'win32':
        # Windows
        local_appdata = os.path.expandvars(r'%LOCALAPPDATA%')
        credentials_file = [local_appdata]
        log = ['~', 'Downloads', 'log']
    else:
        # Mac or something else
        raise Exception('Not supported OS!')

    credentials_file_name = 'suredone.yaml'
    credentials_file.append(credentials_file_name)

    return {
        'credentials_file': os.path.expanduser(os.sep.join(credentials_file)),
        'log': os.path.expanduser(os.sep.join(log))
    }



def get_args():
    """Parses the arguments and values from the script user.

    Returns:
        Object with arguments (input file, credentials file, log directory, verbose logging, email, selections)
    """

    # find the output and log default directories
    paths = get_default_paths()

    # create description of task
    description = 'Uploads a file to SureDone using SureDone API. '\
                  'Requirements: python 3+ (https://www.python.org/downloads/), '\
                  'requests (pip install requests)'
    parser = argparse.ArgumentParser(description=description)

    # add string type argument
    parser.add_argument(
        '-i',
        '--input_file',
        type=str,
        help='path to input file (Absolute/full or relative path. Start directory for the relative paths: in windows %%USERPROFILE%%\\Downloads\\, in linux $HOME/)')
    parser.add_argument(
        '-c',
        '--credentials_file',
        type=str,
        default=paths['credentials_file'],
        help='path to credentials file (full or relative path)')
    parser.add_argument(
        '-l',
        '--log',
        type=str,
        default=paths['log'],
        help='path to log directory (full or relative path)')
    parser.add_argument(
        '-e',
        '--email',
        type=str,
        required=True,
        help='results emailed when processing is complete')
    parser.add_argument(
        '-n',
        '--name_integration',
        type=str,
        required=True,
        help='name used from SureDone to identify your application to the API for logging'
    )

    # add list type argument
    parser.add_argument(
        '-s',
        '--selections',
        type=str,
        nargs='*',
        default=[],
        help='ID of the checkboxes that should be selected from the SureDone bulk upload form.\
            Default no selection. Can be one, any combination or all from these values: \
            sd-force (Force), sd-importmedia (Import Media URL\'s), sd-syncskip (Skip All channels), \
            sd-skip-ebay (Skip ebay Mail), sd-skip-walmart (Skip walmart).'
    )

    # add action_store/boolean type argument
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='verbose logging (console and log file) (without this arg there is no logging)')
    parser.add_argument(
        '-p',
        '--preserve',
        action='store_true',
        help='preserve the input file after successfully uploading (without this arg the input file is removed after successfully uploading)')
    
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
        file_name = 'suredone_upload-log_{0}.log'.format(datetime_now)
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



def get_credentials(args, logger):
    """Parses the credentials yaml file and gets user and token (simple yaml parser, key-value parser).

    Parameters:
        args: Object with command line arguments (credentials file)
        logger: Function used for logging
    
    Returns:
        Credentials, user and token.
    """

    data = {}

    with open(args.credentials_file, 'r') as credentials_file:
        logger('Reading the credentials file')

        # parse line by line
        for line in credentials_file.readlines():

            # ignore comments
            if line.startswith('#'):
                continue

            # split the line and take the key and value
            values = line.split(':')
            key = values[0].strip()
            value = values[1].strip()
            data[key] = value
    
    if not 'user' in data:
        raise Exception('There is no user found in the credentials file')

    if not 'token' in data:
        raise Exception('There is no token found in the credentials file')
        
    logger('The credentials are read successfully')
        
    return data



def construct_input_file_path(args, logger):
    """Gets the input file value from the command line and construct the path.

    Parameters:
        args: Object with command line arguments (input file path)
        logger: Function used for logging
    
    Returns:
        Input file path.
    """

    if args.input_file == None:
        raise Exception('Missing input file path.')

    # absolute path
    if os.path.isabs(args.input_file):
        return args.input_file

    # relative path
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # Linux
        input_file = ['~']
    elif sys.platform == 'win32':
        # Windows
        input_file = ['~', 'Downloads']
    
    input_file.append(args.input_file)

    return os.path.expanduser(os.sep.join(input_file))
    


def suredone_upload(args, credentials, logger, input_file_path):
    """The function with the main logic for this script.

    Parameters:
        args: Object with command line arguments 
        credentials: Credentials for the API (user and token)
        logger: Function used for logging
        input_file_path: Input file path
    """

    url = 'https://api.suredone.com/v1/bulk'
    
    headers = {
        # no need from Content-Type: multipart/form-data, the post method is adding that
        'X-Auth-Integration': args.name_integration,
        'X-Auth-User': credentials['user'],
        'X-Auth-Token': credentials['token']
    }

    params = {
        'sd_bulk_email': args.email
    }

    # add the names of all checkboxes that needs to be selected
    for param in args.selections:
        params[param] = 'on' # 'on' is a default value when submitting a form

    files = {}

    with open(input_file_path, 'rb') as input_file: # works with r and rb
        logger('Reading the input file')

        input_file_data = input_file.read()
        input_file_basename = os.path.basename(input_file.name)
        input_file_name = os.path.splitext(input_file_basename)[0]

        files['bulk_file'] = input_file_data
        params['bulk_name'] = input_file_name

    logger('Uploading the input file')

    response = requests.post(
        url, 
        files=files, 
        headers=headers, 
        params=params
    )

    response_json = response.json()

    if (response.status_code == 200) and (response_json['result'] == 'success'):
        logger('The input file is uploaded successfully')
        logger('Request file: {0}'.format(response_json['request_file']))
        logger('Result file: {0}'.format(response_json['result_file']))
    else:
        if ('result' in response_json) and ('message' in response_json):
            raise Exception('Status code: {0}; Result: {1}; Message: {2}'.format(
                response.status_code, 
                response_json['result'], 
                response_json['message'])
            )
        else:
            raise Exception('Status code: {0}; Response: {1}'.format(
                response.status_code, 
                str(response_json))
            )



def remove_input_file(args, logger, input_file_path):
    """Removes the input file (if args.preserve is False).

    Parameters:
        args: Object with arguments (preserve)
        logger: Function used for logging
        input_file_path: Input file path
    """

    if not args.preserve:
        os.remove(input_file_path)
        logger('The input file is removed locally')
    else:
        logger('The input file is not removed')



def main():
    """Workflow:
        1. Gets and parses the arguments from the command-line execution.
        2. Creates a logger, logs in 2 places: log file and console.
        3. Reads the credentials from the yaml file.
        4. Constructs the input file path. 
        5. Uploads a file to SureDone using the SureDone API.
        6. Removes the input file after successfully uploading.
    """

    # get and parse the arguments
    args = get_args()
    
    # create a logger
    logger = create_logger(args)

    try:
        # get credentials
        credentials = get_credentials(args, logger)
    except Exception as e:
        logger('An error occurred during reading the credentials: {0}'.format(str(e)))
        return

    try:
        # construct input file path
        input_file_path = construct_input_file_path(args, logger)
    except Exception as e:
        logger('An error occurred: Input file path argument is required (-i --input_file)')
        return
        
    try:
        # call the suredone upload method
        suredone_upload(args, credentials, logger, input_file_path)
    except Exception as e:
        logger('An error occurred during uploading the file: {0}'.format(str(e)))
        return

    # remove the input file after successfully uploading
    remove_input_file(args, logger, input_file_path)



if __name__ == "__main__":
    """The script starts here."""
    main()

# SureDone API
[SureDone](https://www.suredone.com) is a multichannel listing tool built for merchants who are looking for a simple way to list products on Amazon and eBay, as well as their own website.\
This script uploads a file to SureDone using the [SureDone API](https://www.suredone.com/guides/api/).

## Requirements
- python 3+ ([https://www.python.org/downloads/](https://www.python.org/downloads/)) 
- [requests](https://pypi.org/project/requests/) (```pip install requests```)

## Usage
```shell
python suredone_upload.py [-h] [-i INPUT_FILE] [-c CREDENTIALS_FILE] [-l LOG] [-e EMAIL] [-n NAME_INTEGRATION] [-s [SELECTIONS [SELECTIONS ...]]] [-v] [-p]
```

## API key
In order to access SureDone API, you'll need user and token from SureDone. Add the keys in a YAML file with this format:

```yaml
# username from the SureDone platform
user:   <SureDone user>
# token from the SureDone platform
token:  <SureDone token>
```

## Script arguments
-  **-h, --help** - show this help message and exit
-  **-i INPUT_FILE, --input_file INPUT_FILE** - path to input file (Absolute/full or relative path. Start directory for the relative paths: in windows `%USERPROFILE%\Downloads\`, in linux `$HOME/`)
-  **-c CREDENTIALS_FILE, --credentials_file CREDENTIALS_FILE** - path to credentials file (full or relative path)
-  **-l LOG, --log LOG** - path to log directory (full or relative path)
-  **-e EMAIL, --email EMAIL** - results emailed when processing is complete
-  **-n NAME_INTEGRATION, --name_integration NAME_INTEGRATION** - name used from SureDone to identify your application to the API for logging
-  **-s [SELECTIONS [SELECTIONS ...]], --selections [SELECTIONS [SELECTIONS ...]]** - ID of the checkboxes that should be selected from the SureDone bulk upload form. Default no selection. Can be one, any combination or all from these values: sd-force (Force), sd-importmedia (Import Media URL's), sd-syncskip (Skip All channels), sd-skip-ebay (Skip ebay Mail), sd-skip-walmart (Skip walmart).
-  **-v, --verbose** - verbose logging (console and log file) (without this arg there is no logging)
-  **-p, --preserve** - preserve the input file after successfully uploading (without this arg the input file is removed after successfully uploading)
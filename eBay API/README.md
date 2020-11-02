# eBay API
[EBay](https://www.ebay.com/) is an e-commerce corporation that facilitates consumer-to-consumer and business-to-consumer sales through its website.\
This script extracts a list of active eBay listings from a eBay seller using the [eBay API](https://developer.ebay.com/).


## Requirements
- python 3+ ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- [gevent](https://pypi.org/project/gevent/) (```pip install gevent```)
- [ebaysdk](https://github.com/timotheus/ebaysdk-python) (```pip install ebaysdk```)

## Usage
```shell
python ebaylistings.py [-h] [-o OUTPUT] [-l LOG] [-f FILE] [-d DELIMITER] [-c CALLS] [-m MONTHS] [-x XDAYS] [-p] [-v] [-s]
```

## API key
In order to access eBay API, you'll need appid, certid, devid and token from eBay. Add the keys in a YAML file with this format:

```yaml
# Trading API - https://www.x.com/developers/ebay/products/trading-api
api.ebay.com:
    compatibility: 1083
    appid: <eBay appid>
    certid: <eBay certid>
    devid: <eBay devid>
    token: <eBay token>
```

## Script arguments
-  **-h, --help** - show this help message and exit
-  **-o OUTPUT, --output OUTPUT** - full path to output directory (without the name of the output file)
-  **-l LOG, --log LOG** - full path to log directory (without the name of the log file)
-  **-f FILE, --file FILE** -  path to eBay yaml file (API keys file) (default='ebay.yaml', first looks into the current directory after that into the home)
-  **-d DELIMITER, --delimiter DELIMITER** - delimiter for the output file ("," for CSV files, "\t" for TSV files, everything else for TXT files) (default=',')
-  **-c CALLS, --calls CALLS** maximum parallel API calls (default=10, max=18 suggested by eBay)
-  **-m MONTHS, --months MONTHS** - max months in the past for item searching (default=36)
-  **-x XDAYS, --xdays XDAYS** - get all items older than last sale or listing start date if no sales (default=90)
-  **-p, --preserve** - preserve previous versions of the output (without this arg the previous versions are removed)
-  **-v, --verbose** - verbose logging (console and log file) (without this arg there is no logging)
-  **-s, --sort** - sorts the items in ascending order (without this arg items will be in descending order, the item with the oldest sale will be first)
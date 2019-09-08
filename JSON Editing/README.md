# JSON Editing
Tool for editing a simple MK-EN dictionary in JSON.

## Requirements
- python 3+ ([https://www.python.org/downloads/](https://www.python.org/downloads/)) 
- [wxPython](https://pypi.org/project/wxPython/) (```pip install wxPython```)

## Usage
```shell
python json_editing.py
```

## Description
You'll need to create `content.json` file with this JSON template:

```json
{
    "Example 1": {
        "mk": "mk example 1", 
        "en": "en example 1"
    }, 
    "Example 2": {
        "mk": "mk example 2", 
        "en": "en example 2"
    }
}
```

And with this tool you can edit `mk` and `en` fields. This tool is useful when you have a bunch of data and want to search for some field and change it.

![JSON editing](https://raw.githubusercontent.com/MTrajK/python-projects/master/JSON%20Editing/json_editing.png "JSON editing") 
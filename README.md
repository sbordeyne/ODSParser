# ODSParser
A python library that parses ODS files, and return the spreadsheet in a pandas dataframe

# How to use :

```
python
from ODSParser import ODSParser

with ODSParser("my_spreadsheet.ods") as ods_file:
    #do stuff
```

# Required libraries :

- zipfile
- pandas
- lxml
- numpy (future)

# Planned features :

For now, getting a first release would be good, though, it will come soon. I plan on adding several features though :

- LibreOffice Calc functions imported in python to refresh the spreadsheet if need be.
- Export the data in other DataFrames format such as numpy arrays, python matrixes etc...
- Make it PyPI ready
- Handle IO/File exceptions
- As of now it's read-only, so making it read/write the data

# **Instructions for Using the JSON Configuration File**

This document provides detailed instructions on how to configure and use the JSON parameter file to calculate profits based on the SELIC rate.

Author: Alan Moura Silva

## JSON File Structure

The JSON file has the following structure:

```json
{
    "general":{
        "capital":"657.43", //float
        "save_csv":"TRUE" //bool
    },

    "dates":{
        "start_date":"2010-1-1", //date YYYY-M-D
        "end_date":"2021-3-1", //date YYYY-M-D
        "frequency":"D" //string (D,M or Y)
    },

    "range":{
        "days":"500" //int
    },

    "urlAPIParameters":{
        "baseURL": "https://api.bcb.gov.br/dados/serie/", //string
        "serie_name" : "SELIC" //string
    },

    "logging":{
        "level":"INFO"
    }
}
```

### **General parameters (general)**

- capital: The initial capital amount for profit calculation.
Example: "capital": "657.43"

- save_csv: Determines whether the results should be saved in a CSV file.
Possible values: "TRUE" or "FALSE"
Example: "save_csv": "TRUE"

### **Dates**

- start_date: Start date of the period for profit calculation.
Format: "YYYY-MM-DD"
Example: "start_date": "2010-01-01"

- end_date: End date of the period for profit calculation.
Format: "YYYY-MM-DD"
Example: "end_date": "2021-03-01"

- frequency: Frequency of calculations (daily, monthly, or annually).
Possible values: "D" (Daily), "M" (Monthly), "Y" (Annually)
Example: "frequency": "D"

### **Range**

- days: Number of days to find the most profitable period.
Example: "days": "500"

### **API Parameters**

- baseURL: Base URL of the Central Bank API to obtain SELIC rate data.
Example: "baseURL": "https://api.bcb.gov.br/dados/serie/"

- serie_name: Name of the data series for the SELIC rate.
Example: "serie_name": "SELIC"

### **Logging**

- level: Logging level for logs.
Possible values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
Example: "level": "INFO"


# **Instructions for Use**

**Initial Configuration:**
Edit the JSON file with the desired parameters. Make sure that the values are correct and within the specified formats.

**Program Execution:**
Use the JSON file as configuration for your Python program. Your program should read the parameters from the JSON file and use them to calculate profits based on the SELIC rate.

Execute the main file. A snippet of the data and the best day to invest among the dates provided as parameters will be displayed in the command terminal.

**Saving Results:**
If save_csv is set to "TRUE", the results will be saved in the path specified by the program.

**Checking Logs:**
Logs will be generated according to the level defined in logging. Check the logs for detailed information about the program's execution.


# Question answer
![Description of Image](https://i.imgur.com/RH3OGWn.png)

As requested, the answer to the question displayed by the code is:

'The best day to invest is 2015-06-16, with an amount earned of 787.952750655493 after 500 days (2015-06-16 to 2016-10-28)'

And it can be viewed in the screenshot above.

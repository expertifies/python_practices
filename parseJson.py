import pandas as pd
import json
import glob

data = []

# Change the glob if you want to only look through files with specific names
files = glob.glob('C:/Users/m.usman/Desktop/python-practice/jsonfiles/*', recursive=True)

# Loop through files

isin  = 'Null'
cusip = 'Null'
DUNS = 'Null'
NECOID = 'Null'
ACORN = 'Null'

for single_file in files:
#   text = 'some string... this part will be removed.'
  head, sep, tail = single_file.partition('\\')
  with open(single_file, 'r') as f:
    # print(f)
    json_file = json.load(f)
    # print(json_file)  

    ################################### companyCode ######################################################## 
    companyCode = json_file['resource']['companyCode'][0]["value"]

    ################################### companyData ######################################################## 
    for companyData in json_file['resource']['companyRecords']:
        symbol = 'Null'
        exchange = 'Null'
        reasonForTagging = 'Null'
        score = 'Null'
        tickerHierarchy = 'Null'
        micExchangeCode = 'Null'
        ################################### SYMBOLS ######################################################## 
        if companyData.get('symbol') is None:
            symbol = 'Null'
        else:
            symbol = companyData.get('symbol')

        ################################### tickerHierarchy ######################################################## 
        if companyData.get("tickerHierarchy") is not None: 
            tickerHierarchy = companyData.get("tickerHierarchy")

        ################################### EXCHANGE ######################################################## 
        if companyData.get("exchange") is not None: 
            exchange = companyData.get("exchange")

        ################################### reasonForTagging ######################################################## 
        if companyData.get("reasonForTagging") is not None: 
            reasonForTagging = companyData.get("reasonForTagging")


        ################################### score ######################################################## 
        if companyData.get("score") is not None: 
            score = companyData.get("score")

        ################################### micExchangeCode ######################################################## 
        if companyData.get("micExchangeCode") is not None: 
            micExchangeCode = companyData.get("micExchangeCode")

        ################################### securityIdentifiers ######################################################## 
        if companyData.get("securityIdentifiers") is not None:

            for securityIdentifier in companyData.get("securityIdentifiers"):
                if securityIdentifier.get("name") is not None and securityIdentifier.get("name") == "ISIN": 
                    isin = securityIdentifier.get("value")

                if securityIdentifier.get("name") is not None and securityIdentifier.get("name") == "CUSIP": 
                    cusip = securityIdentifier.get("value")


        ################################### otherIdentifiers ######################################################## 
        if companyData.get("otherIdentifiers") is not None:

    
            for otherIdentifier in companyData.get("otherIdentifiers"):
                if otherIdentifier.get("name") is not None and otherIdentifier.get("name") == "DUNS": 
                    DUNS = otherIdentifier.get("value")

                if otherIdentifier.get("name") is not None and otherIdentifier.get("name") == "NECOID": 
                    NECOID = otherIdentifier.get("value")

                if otherIdentifier.get("name") is not None and otherIdentifier.get("name") == "ACORN": 
                    ACORN = otherIdentifier.get("value")




        ################################### Appending Data Here ######################################################## 
        data.append([
            tail,
            companyData.get('companyName'),
            symbol,
            exchange,
            reasonForTagging,
            companyCode,
            isin,
            cusip,
            DUNS,
            NECOID,
            ACORN,
            score,
            micExchangeCode,
            tickerHierarchy
        ])

columnsName = ["file_name","company_name","symbol", "exchange", "reasons-for-taging", "company_code", "ISIN", "CUSIP", "DUNS", "NECOID", "ACORN", "score", "mic-exchange-code" ,"ticker-hierarchy"]
df2 = pd.DataFrame(data)
df2.to_csv('C:/Users/m.usman/Desktop/python-practice/file1.csv', header=columnsName, index=False)

df3 = pd.read_csv("C:/Users/m.usman/Desktop/python-practice/file1.csv")
print(df3)

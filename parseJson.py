###################################################################################################
''' JUST REMINDER 
KINDLY SEARCH THIS STRING: "C:/Users/m.usman/Desktop/python-practice/"
AND CHANGE ACCORDING TO YOUR PATH
'''
###################################################################################################

import pandas as pd
import json
import glob

data = []

# Change the glob if you want to only look through files with specific names
# files = glob.glob('C:/Users/m.usman/Desktop/python-practice/20220425/*.json', recursive=True)
files = glob.glob('C:/Users/m.usman/Desktop/python-practice/data/*.json', recursive=True)

# Loop through files

isin  = 'Null'
cusip = 'Null'
DUNS = 'Null'
NECOID = 'Null'
ACORN = 'Null'

filesWithoutCompanyRecords = []

for single_file in files:

  head, sep, tail = single_file.partition('\\')
  
  with open(single_file, 'r', encoding='utf-8') as f:
    # print(f)
    json_file = json.load(f)
    # print(json_file)  
    
    ################################### companyData ######################################################## 
    checkcompanyRecords = json_file['resource'].get('companyRecords')
    if checkcompanyRecords is not None:
        for companyData in json_file['resource']['companyRecords']:
            companyName = companyData.get('companyName')
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
                companyName,
                symbol,
                exchange,
                reasonForTagging,
                isin,
                cusip,
                DUNS,
                NECOID,
                ACORN,
                score,
                micExchangeCode,
                tickerHierarchy
            ])
    else:
        filesWithoutCompanyRecords.append(tail)
        
columnsName = ["file_name","company_name","symbol", "exchange", "reasons-for-taging", "ISIN", "CUSIP", "DUNS", "NECOID", "ACORN", "score", "mic-exchange-code" ,"ticker-hierarchy"]
df2 = pd.DataFrame(data)
df2.to_csv('C:/Users/m.usman/Desktop/python-practice/companyRecords.csv', header=columnsName, index=False)

# columnsName = ["file_name"]
# df3 = pd.DataFrame(filesWithoutCompanyRecords)
# df3.to_csv('C:/Users/m.usman/Desktop/python-practice/filesWithoutCompanyRecords.csv', header=columnsName, index=False)

df4 = pd.read_csv("C:/Users/m.usman/Desktop/python-practice/companyRecords.csv")
print(df4)

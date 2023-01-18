from openpyxl import load_workbook
import pandas as pd
import getDomainData
import requests
import append
import json
import random
import time
import os

# Make list of words from excel
df = pd.read_excel('domains-to-check.xlsx')
domain_list = df['domain'].tolist()
print("The domain list as seen at the excel file: {0}".format(domain_list))

# domains = ["zg-pages.co.il","marmar.co.il"]
# Get data from similar web for each domain URL
# and add data to Excel file
i = 0
for domain in domain_list:
    result_data_dict_for_domain = getDomainData.getDomainExpirationDate(i,domain)
    # print(result_data_dict_for_domain)
    df2 = pd.DataFrame(data=result_data_dict_for_domain, index=[i])
    append.append_df_to_excel('result.xlsx', df2)
    # time.sleep(random.randrange(1, 3))
    i = i + 1

print("Done. The results were added to the result.xlsx file")






    

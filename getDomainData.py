# from fake_useragent import UserAgent
import pycountry
import requests
import random
import json
import time

def getDomainExpirationDate(index, domain):
    apikey = "VJnS27V879VqYEfaihB5B7RZWSlZGtA4"
    result_data_dict = {
        "Domain Name": domain,
        "Domain Expiration Date": ""
    }
    url = "https://api.apilayer.com/whois/query?domain="+str(domain)  
    header = {"apikey":apikey}

    response = requests.get(url, headers=header)
    print("{0}) The response for '{1}' from api is: {2}".format(index,domain,response))

    try:
        data_dict = response.json()
        print("The data_dict : {0}".format(data_dict))
        domain_expiration_date = data_dict["result"]["expiration_date"]
        print((str)(domain),"expiration_date:"+str(domain_expiration_date)) 
    # except ValueError:
    #     print("Decoding JSON has failed, I am waiting 1 minute and trying again...")
    #     time.sleep(random.randrange(41, 59))
    #     result_data_dict = {}
    #     return result_data_dict
    except TypeError:
        domain_expiration_date = "Error"
    except:
        domain_expiration_date = "Error"


    result_data_dict["Domain Expiration Date"] = domain_expiration_date
    return result_data_dict
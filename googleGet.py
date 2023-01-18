import concurrent.futures
import requests
import random
import json
import time


def googleGet(search_list):
    name_URL_tuple_list = []
    while search_list:
        first_five_elements_list = search_list[:5]
        del search_list[:5]
        # print("The first_five_elements_list: {0} ".format(first_five_elements_list))
        # print("The search_list now: {0} ".format(search_list))
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_string = {executor.submit(getRequestForFirstOrganicURL, query_search_string): query_search_string for query_search_string in first_five_elements_list}
            for future in concurrent.futures.as_completed(future_to_string):
                name_and_first_organic_URL_from_thread = future.result()
                while(name_and_first_organic_URL_from_thread == ()):
                    name_and_first_organic_URL_from_thread = getRequestForFirstOrganicURL(future_to_string[future])
                    time.sleep(1)
                name_URL_tuple_list.append(name_and_first_organic_URL_from_thread)
        time.sleep(1)
    return name_URL_tuple_list

            # first_organic_URL_from_func1 = future1.result()
            # future2 = executor.submit(getRequestForFirstOrganicURL, first_five_elements_list[1])
            # first_organic_URL_from_func2 = future2.result()
            # future3 = executor.submit(getRequestForFirstOrganicURL, first_five_elements_list[2])
            # first_organic_URL_from_func3 = future3.result()
            # future4 = executor.submit(getRequestForFirstOrganicURL, first_five_elements_list[3])
            # first_organic_URL_from_func4 = future4.result()
            # future5 = executor.submit(getRequestForFirstOrganicURL, first_five_elements_list[4])
            # first_organic_URL_from_func5 = future5.result()





        # for query_search_string_to_request in first_five_elements_list:
        #     print("Getting first organic URL for {0} from Google...".format(query_search_string_to_request))
        #     first_organic_URL_from_func = getRequestForFirstOrganicURL(query_search_string_to_request)
        #     while(first_organic_URL_from_func == ""):
        #         first_organic_URL_from_func = getRequestForFirstOrganicURL(query_search_string_to_request)
        #     URL_list.append(first_organic_URL_from_func)
        #     # time.sleep(1)
    # return URL_list


def getRequestForFirstOrganicURL(query_search_string):
    url = "https://real-time-google-search.p.rapidapi.com/search"
    querystring = {"q":query_search_string,"location_name":"Abruzzo,Italy","location_parameters_auto":"true"}
    # querystring = {"q":query_search_string}
    headers = {
    'x-rapidapi-key': "a5ac913853msha6d54736cd1b30dp1b62ffjsnf73d35d4c528",
    'x-rapidapi-host': "real-time-google-search.p.rapidapi.com"
    # 'x-rapidapi-key': "ad534cdc63msh3eb72c2d6ad9437p1c43e3jsna0236f7bb72e", //// Itay's old
    # 'x-rapidapi-key': "8233d28cf0msheacf59b1877413fp1dbdc3jsn318c289fc131",////Roee's
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        print("**********The response for '{0}' from Google is: {1}**********".format(query_search_string,response))
        # print("______________________________________________________________________________________________________________________________________________________________________________________")
        # print("")
        # print("")
        data_dict = response.json()
        print("The data_dict for '{0}' from Google is: {1}".format(query_search_string,data_dict))
        # print("")
        # print("")
        # print("______________________________________________________________________________________________________________________________________________________________________________________")
        if not data_dict['data']['organic_results']:
            # print("The data_dict for '{0}' from Google is: {1}".format(query_search_string,data_dict))
            first_organic_URL = "bbc"
        else:
            first_organic_URL = data_dict['data']['organic_results'][0]['url']
        print("The first organic URL for '{0}' is: {1}".format(query_search_string, first_organic_URL))
    except Exception as e:
        print("There was a problem with the API call, I am waiting 15-30 seconds and trying again...")
        print("The problem was: {0}".format(e))
        # print("The data_dict for '{0}' from Google is: {1}".format(query_search_string,data_dict))
        time.sleep(random.randrange(15, 30))
        first_organic_URL = ()
        return first_organic_URL
    return (query_search_string,first_organic_URL)

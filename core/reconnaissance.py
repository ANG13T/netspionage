import requests 
import json

def recon_choice(choice, target, manual_input):
    if choice == '1':
        choose_mac_address(target)
        return()
    elif choice == '2':
        input_mac_address(manual_input)
        return()
    else:
        exit()

def choose_mac_address(target):
    return()

def input_mac_address(manual_input):
    address_api_call(manual_input)
    return()


def address_api_call(address):
    url = ("https://macvendors.co/api/" + address)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        json_object=result['result']
        print(json_object)
        #json_object = json.loads(final)
        if "error" in json_object:
            print("No MAC Address Found!")
            return()
        transcribe_api_results(json_object)
        print("")
    else:
        print("Error: Something Went Wrong")

def transcribe_api_results(json_object):
    for key in json_object:
        value = json_object[key]
        print("The key and value are ({}) = ({})".format(key, value))

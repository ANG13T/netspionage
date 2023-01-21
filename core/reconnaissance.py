def recon_choice(choice, target, manual_input):
    if choice == '1':
        chooseMACAddress(target)
        return()
    elif choice == '2':
        inputMACAddress(target, manual_input)
        return()
    else:
        exit()

def chooseMACAddress(target):
    return()

def inputMACAddress(target, manual_input):
    AddressAPICall(manual_input)
    return()


def AddressAPICall(address):
    url = ("https://macvendors.co/api/" + address)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        final=result['result']
        print("Vendor:" + final["company"])
        print("Address:" + final["address"])
        print("Country:" + final["country"])
        print("")
    else:
        print("Error: Something Went Wrong")
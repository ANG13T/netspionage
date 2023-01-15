
def scanner_choice(choice):
    if choice == '1':
        network_scanner()
        return()
    elif choice == '2':
        wifi_scanner()
        return()
    elif choice == '3':
        port_scanner()
        return()
    elif choice == '4':
        host_scanner()
        return()
    else:
        exit()

def network_scanner():
    print('network')

def wifi_scanner():
    print('wifi')

def port_scanner():
    print('port')

def host_scanner():
    print('host')

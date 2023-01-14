
def prompt_display():  
    while 1:
        user_input = prompt("\nnetspionage >> ")
        if len(user_input)==0:
            print("\n")
            continue
        try:
            choice = int(user_input)
        except ValueError:
            print("\n")
            continue

        if choice == 1:
            while 1:
                ip = prompt("IP >> ")
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        if choice == 2:
            while 1:
                ip = prompt("IP >> ")
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        if choice == 3:
            while 1:
                ip = prompt("IP >> ")
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        elif choice == 4:
            while 1:
                break
            update()
            continue

        elif choice == 5:
            exit('\nTill next time!')

        else:
            pass

try:
    prompt_display()
except KeyboardInterrupt:
    quit('\nTill next time!')
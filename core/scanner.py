import scapy.all as scapy
from scapy.layers.inet import IP, ICMP

def scanner_choice(choice, target):
    if choice == '1':
        network_scanner(target)
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

def network_scanner(target):
    broadcast_packets = create_packet(target)
    success_packets = transmit_packet(broadcast_packets)
    entries = parse_response(success_packets)
    print_analysis(entries)

def wifi_scanner():
    print('wifi')

def port_scanner():
    print('port')

def host_scanner():
    print('host')


# Network Scanner

def create_packet(ip):
    arp_request = scapy.ARP(pdst=ip)  # create a ARP request object by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # We have set the destination
    arp_request_broadcast = broadcast / arp_request
    return (arp_request_broadcast)


def transmit_packet(packet):
    success_list, failure_list = scapy.srp(packet, timeout=1)
    return success_list

# TODO: handle more OS options
def get_os(ip_addr):
    ttl_values = {32: "Windows", 60: "MAC OS", 64: "Linux", 128: "Windows", 255: "Linux 2.4 Kernal"}
    try:
        ans = scapy.sr1(IP(dst=str(ip_addr)) / ICMP(), timeout=1, verbose=0)
        if ans:
            if ans.ttl in ttl_values:
                return ttl_values.get(ans.ttl)
            else:
                return "could not figure the OS version"
        else:
            return "Packets could not send successfully"
    except:
        return "could not figure the OS version"

def parse_response(success_list):
    print(success_list)
    targets = []
    for success in success_list:
        entry = {'ip': success[1].psrc, 'mac': success[1].hwsrc}
        targets.append(entry)
    return targets

def print_analysis(element_entries):
    print("end")
    print("IP\t\t\tMAC Address\t\t\tOPERATING SYSTEM")
    print("." * 100)
    for element in element_entries:
        print(element["ip"] + "\t\t" + element['mac'] + "\t\t" + get_os(element["ip"]) + "\n")
    print("." * 100)
    print(" Scan Complete!")
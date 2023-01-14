#!bin/bash sudo python
import optparse

import scapy.all as scapy
from scapy.layers.inet import IP, ICMP

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target IP/ IP range")
    args_options, arguments = parser.parse_args()
    return args_options


def createPacket(ip):
    arp_request = scapy.ARP(pdst=ip)  # create a ARP request object by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # We have set the destination
    arp_request_broadcast = broadcast / arp_request
    return (arp_request_broadcast)


def transmitPacket(packet):
    success_list, failure_list = scapy.srp(packet, timeout=1)
    return success_list


def getOS(ip_addr):
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



def parseResponse(success_list):
    targets = []
    for success in success_list:
        entry = {'ip': success[1].psrc, 'mac': success[1].hwsrc}
        targets.append(entry)
    return targets


def print_analysis(element_entries):
    print("end")
    print("IP\t\t\tMAC Address\t\t\tOPERATING SYSTEM")
    print("." * 100)
    for element in entries:
        print(element["ip"] + "\t\t" + element['mac'] + "\t\t" + getOS(element["ip"]) + "\n")


options = getArguments()

if options.target is not None:
    print("str")
    broadcast_packets = createPacket(options.target)
    success_packets = transmitPacket(broadcast_packets)
    entries = parseResponse(success_packets)
    print_analysis(entries)
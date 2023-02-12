import scapy.all as scapy
from scapy.layers.inet import IP, ICMP
from threading import Thread
import pandas
import socket
from core.print_output import print_output
import os
import time

def scanner_choice(choice, target):
    if choice == '1':
        network_scanner(target)
        return()
    elif choice == '2':
        wifi_scanner()
        return()
    elif choice == '3':
        port_scanner(target)
        return()
    else:
        exit()

# Wifi Scanner Configs
# Change to the appropriate interface
interface = "wlan0"
wifi_scan_timeout = 10
networks = networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
networks.set_index("BSSID", inplace=True)

# Port Scanner Configs
scan_start = 1
scan_end = 1025

def network_scanner(target):
    broadcast_packets = create_packet(target)
    success_packets = transmit_packet(broadcast_packets)
    entries = parse_response(success_packets)
    print_analysis(entries)

# TODO: test with wifi adapter
def wifi_scanner():
    initiate_wifi_scan()

def port_scanner(target):
    scan_ports(target)

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
    print_output(success_list)
    targets = []
    for success in success_list:
        entry = {'ip': success[1].psrc, 'mac': success[1].hwsrc}
        targets.append(entry)
    return targets

def print_analysis(element_entries):
    print_output("end")
    print_output("IP\t\t\tMAC Address\t\t\tOPERATING SYSTEM")
    print_output("." * 100)
    for element in element_entries:
        print_output(element["ip"] + "\t\t" + element['mac'] + "\t\t" + get_os(element["ip"]) + "\n")
    print_output("." * 100)
    print_output("\n Scan Complete!")

# WiFi Scanner

def initiate_wifi_scan():
    # start the thread that prints all the networks
    print("hi")
    printer = Thread(target=print_all_networks)
    printer.daemon = True
    printer.start()
    # start the channel changer
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()
    # start sniffing
    scapy.sniff(prn=extract_network_info, iface=interface)

def extract_network_info(packet):
    if packet.haslayer(scapy.Dot11Beacon):
        # extract the MAC address of the network
        bssid = packet[scapy.Dot11].addr2
        # get the name of it
        ssid = packet[scapy.Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        # extract network stats
        stats = packet[scapy.Dot11Beacon].network_stats()
        # get the channel of the AP
        channel = stats.get("channel")
        # get the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


def print_all_networks():
    while True:
        os.system("clear")
        print_output(networks)
        time.sleep(0.5)


def change_channel():
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        # switch channel from 1 to 14 each 0.5s
        ch = ch % 14 + 1
        time.sleep(0.5)

# Port Scanner

# TODO: make threaded port scanner to increase speed [https://www.thepythoncode.com/article/make-port-scanner-python]
def scan_ports(host):
    open_count = 0
    close_count = 0
    for port in range(scan_start, scan_end):
        if check_port(host, port):
            open_count += 1
            print_output(f"\n [+] {host}:{port} is OPEN!")
        else:
            close_count += 1
            print_output(f"\n [!] {host}:{port} is CLOSED!")
    print_output(f"\n {open_count} OPEN Ports \n {close_count} CLOSED Ports")

def check_port(host, port):
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        # s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        return False
    else:
        # the connection was established, port is open!
        return True
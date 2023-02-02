<p align=center>
<img src="https://github.com/angelina-tsuboi/netspionage/blob/master/assets/banner.png" />
  <br />
  <br />
  <span>
  <b> Network Analysis CLI framework that performs Network Scanning, OSINT, and Attack Detection</b>
  </span>
  <br>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contributing">Contributing</a>
</p>

## Installation

```console
# clone the repo
git clone https://github.com/angelina-tsuboi/netspionage.git

# change the working directory to netspionage
cd netspionage

# install the requirements
pip3 install -r requirements.txt
```

## Usage

ReconSpider is very handy tool and easy to use. All you have to do is just have to pass values to parameter.
In order to start ReconSpider just type:
```
python3 netspionage.py
```

### Banner
```
                __             _                            
    ____  ___  / /__________  (_)___  ____  ____ _____ ____ 
   / __ \/ _ \/ __/ ___/ __ \/ / __ \/ __ \/ __ `/ __ `/ _ \
  / / / /  __/ /_(__  ) /_/ / / /_/ / / / / /_/ / /_/ /  __/
 /_/ /_/\___/\__/____/ .___/_/\____/_/ /_/\__,_/\__, /\___/ 
                    /_/                        /____/  
                    
 Created by Angelina Tsuboi [angelinatsuboi.net] V.0.0.1

 https://github.com/angelina-tsuboi/netspionage
 ----------------------------------------------------------------------------
 
 ENTER 1 - 4 TO SELECT OPTIONS

 1.  SCANNING                   Scan for IPs, nearby APs, ports, hosts, and more

 2.  RECONNAISSANCE             Gather  information  about nearby MAC addresses

 3.  DETECTION                  Detect for ARP Spoofing and SYN Flood attacks

 4.  EXIT                       Exit from netspionage to your terminal
 
```

**NETWORK SCANNER**

Gather information abuot devices connected to network such as IP address, MAC address, and OS.
```
netspionage >> 1
SCAN INPUT >> 1
NET IP ADDRESS (Eg: 192.168.1.1/24) >> 192.168.1.1/24
```

**WiFi SCANNER**

Gather information about nearby WiFi access points such as dBm Signal, SSID, channel, and encryption.
```
netspionage >> 1
SCAN INPUT >> 2
```

**PORT SCANNER**

Scan ports on a specified network to check if they are open or closed.
```
netspionage >> 1
SCAN INPUT >> 3
NET IP ADDRESS (Eg: 192.168.1.1/24) >> 192.168.1.1/24
```

**MAC ADDRESS RECON (CHOOSE)**

This option allows you to gather data about a selected device on the network via MAC address.
```
netspionage >> 2
RECON INPUT >> 1
NET IP ADDRESS (Eg: 192.168.1.1/24) >> 192.168.1.1/24
```

**MAC ADDRESS RECON (INPUT)**

This option allows you to gather data about a device via an inputted MAC address.
```
netspionage >> 2
RECON INPUT >> 2
MAC ADDRESS (Eg:08:00:69:02:01:FC) >> 08:00:69:02:01:FC
```

**DETECT ARP SPOOFING**

Detect for ARP Spoofing Attacks on your network.
```
netspionage >> 3
DETECT INPUT >> 1
NET IP ADDRESS (Eg: 192.168.1.1/24) >> 192.168.1.1/24
```

**DETECT TCP FLODDING**

Detect for TCP Flood Attacks on your network.
```
netspionage >> 3
DETECT INPUT >> 2
NET IP ADDRESS (Eg: 192.168.1.1/24) >> 192.168.1.1/24
```

**EXIT**

Exit netspionage from current terminal.
```
netspionage >> 4
Till next time!
```

## Contributing
We would love to have you help us with the development of Sherlock. Each and every contribution is greatly valued!

Here are some things we would appreciate your help on:
- Addition of new site support ¹
- Bringing back site support of [sites that have been removed](removed_sites.md) in the past due to false positives

[1] Please look at the Wiki entry on [adding new sites](https://github.com/sherlock-project/sherlock/wiki/Adding-Sites-To-Sherlock)
to understand the issues.

TODO:
- test on VM with PAU06
- fix tcp flood attack and arp spoof detection
- upload to pypi


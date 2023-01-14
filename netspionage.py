import sys

def print_banner():
       return ("""
                  __             _                            
      ____  ___  / /__________  (_)___  ____  ____ _____ ____ 
     / __ \/ _ \/ __/ ___/ __ \/ / __ \/ __ \/ __ `/ __ `/ _ \\
    / / / /  __/ /_(__  ) /_/ / / /_/ / / / / /_/ / /_/ /  __/
   /_/ /_/\___/\__/____/ .___/_/\____/_/ /_/\__,_/\__, /\___/ 
                      /_/                        /____/           
""")

def print_details():
    return("   Created by Angelina Tsuboi [angelinatsuboi.net] V.0.0.1")


def print_menu():
    return ("""
ENTER 0 - 13 TO SELECT OPTIONS

1.  IP                           Enumerate  information  from  IP Address
2.  DOMAIN                       Gather  information  about  given DOMAIN
3.  PHONENUMBER                  Gather  information  about   Phonenumber
4.  DNS MAP                      Map DNS  records associated  with target
5.  METADATA                     Extract all metadata of  the  given file
6.  REVERSE IMAGE SEARCH         Obtain domain name or IP address mapping
7.  HONEYPOT                     Check if it's honeypot or a real  system
8.  MAC ADDRESS LOOKUP           Obtain information about give Macaddress
9.  IPHEATMAP                    Draw  out  heatmap  of  locations  of IP
10. TORRENT                      Gather torrent download  history  of  IP
11. USERNAME                     Extract Account info. from social  media
12. IP2PROXY                     Check whether  IP  uses  any VPN / PROXY
13. MAIL BREACH                  Checks given domain  has  breached  Mail
99. UPDATE                       Update ReconSpider to its latest version

0. EXIT                         Exit from  ReconSpider  to your terminal
       """)

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           try:
                  print(print_banner())
                  print(print_details())
                #   from core import repl_prompt
           except ModuleNotFoundError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version, Please install using: python3 setup.py install')
                  quit()
    else:
           try:
                #   from core import repl_prompt
                print('hi')
           except ImportError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version,, Please install using: python3 setup.py install')
                  quit()
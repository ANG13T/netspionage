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
    return("""
 Created by Angelina Tsuboi [angelinatsuboi.net] V.0.0.1

 https://github.com/angelina-tsuboi/netspionage
 ----------------------------------------------------------------------------
       """)


def print_menu():
    return ("""
ENTER 0 - 5 TO SELECT OPTIONS

1.  SCANNING                           Enumerate  information  from  IP Address
2.  RECONNAISSANCE                       Gather  information  about  given DOMAIN
3.  DETECTION                  Gather  information  about   Phonenumber
4.  UPDATE                      Map DNS  records associated  with target

5. EXIT                         Exit from  ReconSpider  to your terminal
       """)

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           try:
                  print(print_banner())
                  print(print_details())
                  print(print_menu())
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
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

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           try:
                  print(print_banner())
                  print(print_details())
                  from core import prompts
           except ModuleNotFoundError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version. Please install using: python3 setup.py install')
                  quit()
    else:
           try:
                from core import prompts
           except ImportError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version. Please install using: python3 setup.py install')
                  quit()
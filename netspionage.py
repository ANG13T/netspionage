import sys
import configparser

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           config = configparser.ConfigParser()
           config.read('configuration.ini')
           log_text = config.get('Settings', 'LogToTextFile')

           try:
                  if log_text == "True":
                     with open("output.txt", 'w') as sys.stdout:
                            from core import prompts
                  else:
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
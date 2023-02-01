import sys

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           try:
              from core import prompts
           except ModuleNotFoundError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version.')
                  quit()
    else:
           try:
                from core import prompts
           except ImportError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version.')
                  quit()
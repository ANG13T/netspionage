import configparser

def print_output(text):
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    log_text = config.get('Settings', 'LogToTextFile')

    print(text)
    if log_text == "True":
        with open("output.txt","a") as f:  # appends to file and closes it when finished
            print(text, file=f)
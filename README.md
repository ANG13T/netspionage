# netspionage
`python -m pip install -rpip install scapy requirements.txt --user`
`python3 netspionage/main.py -t 10.18.248.181/24`

via virtualenv
`python3 -m pip install virtualenv`
`virtualenv --python=3.8 netspionage_env`
`source netspionage_env/bin/activate`
`sudo ./netspionage_env/bin/python python -m pip install -r requirements.txt --use`
`sudo ./netspionage_env/bin/python python3 netspionage/main.py -t 10.18.248.181/24`



# Installaction
`pip install -r requirements.txt`

TODO:
- config file with vars: iface, global colors
- add terminal colors
- upload to pypi
- make shortform command of netspionage
- fix tcp flood attack
- test on VM with PAU06
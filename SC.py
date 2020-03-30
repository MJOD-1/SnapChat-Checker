import requests
from hashlib import sha256
from time import time, sleep
from colorama import Fore

print(Fore.LIGHTGREEN_EX+"""

 _____                   _____ _           _
/  ___|                 /  __ \ |         | |
\ `--. _ __   __ _ _ __ | /  \/ |__   __ _| |_
 `--. \ '_ \ / _` | '_ \| |   | '_ \ / _` | __|
/\__/ / | | | (_| | |_) | \__/\ | | | (_| | |_
\____/|_| |_|\__,_| .__/ \____/_| |_|\__,_|\__|
                  | |
                  |_|
 _____ _               _
/  __ \ |             | |
| /  \/ |__   ___  ___| | _____ _ __
| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| \__/\ | | |  __/ (__|   <  __/ |
 \____/_| |_|\___|\___|_|\_\___|_|
            Info :
                Virsion : 1.0
                Program By : 0xZoRo
                Github : https://www.github.com/0xZoRo/
                instagram : @9du
""")
print(Fore.LIGHTRED_EX+"please enter the key :")
Key='5}_tWt2V='
while True:
    _key = input('Key: ')
    if _key =="".join('{0}'.format(chr(ord(i) -5 %26))for i in Key):
        print('Enjoy !')
        break
    else:
        print('Key Error.')
        break
FielUser = open('users.txt' , 'r').read().splitlines()

req = requests.session()

def token():
    for i, c in enumerate("0001110111101110001111010101111011010001001110011000110001000110"):
        if c == "0":
            yield sha256(("iEk21fuwZApXlz93750dmW22pw389dPwOk"+"m198sOkJEn37DjqZ32lpRu76xmw288xSQ9").encode('utf-8')).hexdigest()[i]
        else:
            yield sha256((str(int(round(time() * 1000.0))) + "iEk21fuwZApXlz93750dmW22pw389dPwOk").encode('utf-8')).hexdigest()[i]



for user in FielUser:

    if user:
        user = user.strip()

        url = 'https://app.snapchat.com/loq/suggest_username_v2'

        headers = {'User-Agent':'Snapchat/10.25.0.0 (Agile_Client_Error; Android 5.1.1#500181103#22; gzip)'}

        data = {
            'req_token': "".join(list(token())),
            'requested_username': user,
            'timestamp': int(round(time() * 1000.0)),
            'status_code': ''
        }

        res = req.post(url, headers=headers, data=data)

        if res:
            JSON = res.json()
            #print(JSON)

            if JSON.get('requested_username') and JSON.get('status_code') == 'OK':
                with open('Found.txt', "a+") as file_save:
                    file_save.write(user + '\n')
                print('Found ->', user)
                sleep(1)
            else:
                print('Not Found ->', user)
                sleep(1)

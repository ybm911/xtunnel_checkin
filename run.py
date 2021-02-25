import requests, ast, yaml, sys
from alive_progress import alive_bar
from colorama import Fore, Back, Style

if sys.argv[1] == "-c":
    pass
else:
    sys.exit()
config_file = sys.argv[2]

with open(config_file, 'r') as config:
    information = yaml.load(config.read(), Loader=yaml.FullLoader)
    email = information['email']
    password = information['password']
    cookie = information['cookie']

if __name__ == '__main__':
    UI = """

               __  ___            __       __      ___     //
         \\ / /  / /   //   / / //   ) ) //   ) ) //___) ) //
         \/ /  / /   //   / / //   / / //   / / //       //
         / /\ / /   ((___( ( //   / / //   / / ((____   //



            ___     / __      ___      ___     / ___       ( )   __
          //   ) ) //   ) ) //___) ) //   ) ) //\ \       / / //   ) )
         //       //   / / //       //       //  \ \     / / //   / /
        ((____   //   / / ((____   ((____   //    \ \   / / //   / /


    """
    print(Fore.CYAN + UI)
    print(Fore.GREEN + "功能：xtunnel 自动签到，每日获取50 MB 流量")


print(Style.RESET_ALL, end = "")

session = requests.session()

items = range(1)
with alive_bar(len(items)) as bar:
    for item in items:
        burp0_url = "https://xtunnel.fun:443/"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
        re = session.get(burp0_url, headers=burp0_headers)
        # print("3…")
        #   print(re.status_code)
        #   print(re.text)

        burp0_url = "https://xtunnel.fun:443/cdn-cgi/bm/cv/result?req_id=60982d4e8d0fa312"
        #   burp0_cookies = {"__cfduid": "de75c24d3862f9bfff5d081fd65b6816c1609293729", "lang": "zh-cn"}
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://xtunnel.fun", "Connection": "close", "Referer": "https://xtunnel.fun/", "Cache-Control": "max-age=0"}
        burp0_json={"fp": {"e": {"ar": [1417, 2492], "cd": 24, "ch": False, "pr": 1, "r": [2560, 1440], "wb": False, "wd": False, "wn": False, "wp": False, "ws": False}, "id": 3}, "m": "e892463a9fce479807414733737b8fb6d3590d81-1609293729-1800-AdrqdMkgvaYVcXYXXCIhZCkLVdRbKmAAaDDI/zMtTttbRlgFRHyowJWoXTesHGrBxYGKJRNQsGkXSh0DRfEBvKRiykCa8MZytoZTv1VX8bRjsiKBMAxs59bSkVesGYdCWg==", "results": ["57358b3c10163d9e63f053c6db08f61a", "9458d535f8ee00831c917859be89efc3"], "timing": 38}
        #   re = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
        re = session.post(burp0_url, headers=burp0_headers, json=burp0_json)
        # print("2…")
        #   print(re.status_code)


        burp0_url = "https://xtunnel.fun:443/auth/login"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "https://xtunnel.fun/", "Upgrade-Insecure-Requests": "1"}
        re = session.get(burp0_url, headers=burp0_headers)
        #print("1…")
        #   print(re.status_code)
        #   print(re.text)
        bar()


burp0_url = "https://xtunnel.fun:443/auth/login"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://xtunnel.fun", "Connection": "close", "Referer": "https://xtunnel.fun/auth/login"}
burp0_data = {"email": email, "passwd": password,"code": '', "remember_me": "on"}
re = session.post(burp0_url, headers=burp0_headers, data=burp0_data)
#   print(re.status_code)
Login_info = ast.literal_eval(re.text)
print(Fore.GREEN + Login_info['msg'])
print(Style.RESET_ALL, end = "")

items = range(1)
with alive_bar(len(items)) as bar:
    for item in items:
        burp0_url = "https://xtunnel.fun:443/user"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "https://xtunnel.fun/auth/login", "Upgrade-Insecure-Requests": "1"}
        re = session.get(burp0_url, headers=burp0_headers)
        #print("3…")
        #   print(re.status_code)


        #   get trafficlog
        burp0_url = "https://xtunnel.fun:443/user/trafficlog"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Connection": "close", "Referer": "https://xtunnel.fun/user"}
        re = session.get(burp0_url, headers=burp0_headers)
        #print("2…")
        #   print(re.status_code)


        burp0_url = "https://xtunnel.fun:443/cdn-cgi/bm/cv/result?req_id=609863028b830bd6"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://xtunnel.fun", "Connection": "close", "Referer": "https://xtunnel.fun/user"}
        burp0_json={"fp": {"e": {"ar": [1417, 2492], "cd": 24, "ch": False, "pr": 1, "r": [2560, 1440], "wb": False, "wd": False, "wn": False, "wp": False, "ws": False}, "id": 3}, "m": "76d0c30f5723abdd8c73df4fcb898d4065cbc955-1609295928-1800-AYkl7AyUAKWBorQtT/r6WvlzFOv2kETuE8B/RTkb4DF09i917Z/L6XbtbdJbZwCpb6AH6g13s/GB/YbkBcp1jKQzQylhs0uI6oMxkvAR0i9l+pitTRyfHDCVc/xjjHfyQA==", "results": ["f69de87d9ccc68823ef4b8e52335a295", "73d7df8393e0feffb87c44fe37586e87"], "timing": 32}
        re = session.post(burp0_url, headers=burp0_headers, json=burp0_json)
        #print("1…")
        #   print(re.status_code)
        bar()

#   checkin
burp0_url = "https://xtunnel.fun:443/user/checkin"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Origin": "https://xtunnel.fun", "Connection": "close", "Referer": "https://xtunnel.fun/user"}
re = session.post(burp0_url, headers=burp0_headers)
checkin_info = ast.literal_eval(re.text)
print(Fore.GREEN + checkin_info['msg'])
print(Style.RESET_ALL, end = "")

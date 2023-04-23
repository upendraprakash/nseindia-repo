import requests
import sys

n = len(sys.argv)
print("Total arguments passed:", n)

startDate=sys.argv[1]
endDate=sys.argv[2]
symbol=sys.argv[3]

## Authentication
cookies=''
headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

s =requests.Session()
output = s.get("http://www.nseindia.com",headers=headers)

for cookie in output.cookies:
   cookies=cookies+cookie.name+'='+cookie.value+';'
   
print('Authentication tokens from cookies ====  ',cookies)

## downloading Security-wise Price Volume Archives (Equities) 
print("\nstartDate = "+ startDate+"\nendDate= "+endDate+'\nsymbol: '+symbol)


params = {'from': startDate,'to':endDate,'symbol':symbol,'dataType':'priceVolumeDeliverable','series':'ALL'}
url="https://www.nseindia.com/api/historical/securityArchives"
#url = "https://www.nseindia.com/api/historical/securityArchives?from=20-03-2023&to=20-04-2023&symbol=SBIN&dataType=priceVolumeDeliverable&series=ALL"

payload={}

headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Cookie': cookies
}

response = requests.request("GET", url,params=params, headers=headers, data=payload)
print(response.text)
#python test.py 10-04-2023 20-04-2023 SBIN
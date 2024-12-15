import sys
import requests
url=sys.argv[1]
wordlist=sys.argv[2]
extension=sys.argv[3]

with open ("dirbuster.txt","r") as f:
    wordlist=f.read().split()
    for w in wordlist:
      fullurl=f"{url}{w}{extension}"
      response=requests.get(fullurl)
      if 200<=response.status_code>400:
          print(f"{w}{extension}\t{response.status_code}")
      else :
          print(f"Bele extension yoxdur {w}{extension}\t{response.status_code}")
        



    
import requests
from bs4 import BeautifulSoup

address = "0x1d6978D76Ad9e3E4A0bdA4658B068443D2A3fCf4"
apiKey = "2YI2Z481C8IDX7R68DDYYU3NMEF6IKVF24"
contract = "0x7d647b1a0dcd5525e9c6b3d14be58f27674f8c95"
url = "http://api.etherscan.io/api?module=account&action=tokenbalance" \
      "&contractaddress="+contract+ \
      "&address="+address+ \
      "&tag=latest&apikey="+apiKey

response = requests.get(url)
address_content = response.json()
result = address_content.get("result")
balance = (int(result)/(10**18))
print(balance)

urlAccount = "https://etherscan.io/tokenholdings?a="+address
page = requests.get(urlAccount)
soup = BeautifulSoup(page.content, "html.parser")

listOfCryptos = soup.find_all("table", attrs={"class": "table table-align-middle table-md-x table-hover dataTable no-footer"})

#for listOfCrypto in listOfCryptos :
#      print(listOfCrypto, end="\n"*2)

print(soup)
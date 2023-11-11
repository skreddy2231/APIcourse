import requests
import pandas
from bs4 import BeautifulSoup

# step1: send api request call
response = requests.get("https://www.bol.com/nl/nl/ra/nieuw-apple-watch-series-9/275182?promo=https://www.bol.com/nl/ra/nieuw-apple-watch-series-9/275182&bltgh=lKlmtEk9tp2s6WZ56PNEHA.5_16.17.Banner")
print("Get response_code:", response.status_code)
assert response.status_code == 200

# step2: grab website content
parser_soup = BeautifulSoup(response.content,'html.parser')

# step3: keep it in structured way
product_names = parser_soup.find_all('a', role='heading')
print(len(product_names))
products_list_app = []
for product in product_names[0:len(product_names)]:
    print(product.getText(), "\n")
    products_list_app.append(product.getText())

# [Step 3]: dataFrame means, data maintains in table(rows & columns) format.
'''df = pandas.DataFrame()
print("Create empty table using DataFrame:", df)'''
data = {'Product Name': products_list_app}

# Workaround: incase any error comes:
# way2:[ line #24]
# data = {'Product Name': pandas.Series(products_list_app)}

# print("Dictionary data>> \n",data)
# same information write it in table.
df = pandas.DataFrame(data)
df.to_csv("retaildata.csv")


######### This is called WebScrapping from any websites, whose site return 200 response only it works ########################
import requests
from bs4 import BeautifulSoup

# make a GET request to the URL
# example on a digikey page
url = "https://www.digikey.it/it/products/filter/transistor-bipolari-singoli/276?s=N4IgTCBcDaIC4CcCGA7AzgSzXA9gkAugL5A"
response = requests.get(url)

# parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# find all the rows in the table containing the electronic parts information
rows = soup.find_all("tr", {"class": "js-sku-item"})

# loop through each row and extract the information we need
for row in rows:
    # find the name of the electronic part
    part_name = row.find("td", {"class": "js-sku-title"}).text.strip()

    # find the technical specifications
    technical_specifications = row.find("td", {"class": "js-sku-attributes"}).text.strip()

    # print the information we've collected
    print("Part Name:", part_name)
    print("Technical Specifications:", technical_specifications)

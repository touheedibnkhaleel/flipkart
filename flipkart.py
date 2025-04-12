import pandas as pd
import requests
from bs4 import BeautifulSoup

based_url = "https://www.flipkart.com/search?q=phone%20under%2050000&page="
content = []
for i in range(2,10):
    url = based_url + str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="DOjaWF gdgoEp")
    next_link = box.find("a",class_="_9QVEpD")

    if not box:
        print(f"NO product container is found on page {i}")
        continue

    phone_name = box.findAll("div",class_="KzDlHZ")
    phone_prices = box.findAll("div",class_="Nx9bqj _4b5DiR")
    phone_reviews = box.findAll("div",class_="XQDdHH")


    if next_link:
        comp_next  = "https://www.flipkart.com" + next_link.get("href")
        print(comp_next)
    else:
        print(f"No link found page{i}")


    for phone,price,review in zip(phone_name,phone_prices,phone_reviews):
        phones = phone.text
        prices = price.text
        reviews = review.text

        content.append({"Phones":phones,"Prices":prices,"Reviews":reviews})


df = pd.DataFrame(content)
print(df)
df.to_csv("C:\\Users\\HM Laptops\\Desktop\\Web Scrapping\\flipkart.csv")

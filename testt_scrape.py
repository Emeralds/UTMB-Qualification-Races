from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq=")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    print(name)
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    print(price)
    rating=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})   #a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    print(rating)
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


#setting up lists
Race=[] #List to store name of the race
Distance=[] #List the distances
Location=[] #List to store price of the race
Date=[] #List to store rating of the race
Points=[] #List to store the points of the race
Race_url=[] #List to store the url for the race

#open the page
driver.get("https://utmbmontblanc.com/en/page/87/courses_qualificatives_liste.html")

# finding and filling out the search box
element = driver.find_element_by_xpath("//*[@id='ct87']/div[2]/form") #initial search form 
#print (element)
select = Select(driver.find_element_by_name('annee'))
select.select_by_visible_text("2021")
select = Select(driver.find_element_by_name('pays'))
select.select_by_visible_text("United States")
element.submit()

""" Waiting for page to load """
time.sleep(3)

"""filling content"""
#driver.switch_to_default_content()
content = driver.page_source
#content = driver.switch_to_default_content()
#content = driver.find_elements_by_xpath("//*[@id='resSearchRace']")
soup = BeautifulSoup(content, features="html.parser" )

#soup = BeautifulSoup(content, "lxml" )
""" #writing html to file
with open("test2.xml", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
    f.close
"""
i=0     #using i to show increment

print(soup.findAll('div', attrs={'class':'nc'}))

for div in soup.findAll('div', attrs={'class':'nc'}):
    print(i)
    i = i+1
    race=div.find('a', href=True)                          # this one works     #attrs={'class':'nc'} 
    #race=div.find('//*[@id="resSearchRace"]/div[6]') 
    #race=div.find('//*[@id="resSearchRace"]/div') 
    print(race.text)
    #print(race)
    print(race.get('href'))
    #distance=div.find('a', href=True, attrs={'target':'_blank'})
    #distance=div.find('div', attrs={'class':'tbed'}) #'_1vC4OE _2rQ-NK'
    #print(distance.text)
    #location=div.find('div', attrs={'class':'hGSR34 _2beYZw'}) #'hGSR34 _2beYZw'
    Race.append(race.text)
    #Distance.append(distance.text)
    #Location.append(location.text)

#df = pd.DataFrame({'Race Name':Race,'Distance':Distance,'Location':Location}) 
df = pd.DataFrame({'Race Name':Race}) 
df.to_csv('Races.csv', index=False, encoding='utf-8')


# Going to need some way to pull out the nested values of the race distances while still also having the name of the race 

#resSearchRace > div:nth-child(2)
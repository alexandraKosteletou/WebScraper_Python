from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

mobile_models=[]
specs=[]
stars=[]
reviews_count=[]
prices=[]
memory=[]
year=[]
screen=[]
battery=[]

page=1

while page<=17:
    url = 'https://www.skroutz.gr/c/40/kinhta-thlefwna/f/852219/Smartphones.html?o=smartphones&page={page}'
    
    request=requests.get(url)
    data = request.text
    soup=bs(data, 'html.parser')
    mobiles= soup.find_all('div',class_= 'card-content')

    for container in mobiles:
        
    #model
        model= container.h2.a.text
        mobile_models.append(model)
        

    #specs
        characteristics = container.p.text
        specs.append(characteristics)
        
            
    #stars
        rate = container.span.text
        stars.append (rate)
    
    #reviews_count
        rev_count = container.find('div', class_='actual-rating').text
        reviews_count.append(rev_count)
    
    #price
        price = container.find('a', class_='js-sku-link sku-link').text
        price = re.sub(r'(?<=([α-ω|ό]))(?=(\d))', ' ', price) 
        prices.append(price)

    page+=1

    
    #memory feature
for element in mobile_models:
    match = re.search(r'\d+GB.+\d+GB', element, re.IGNORECASE)
    memory.append(match.group())
    
    #year
for element in specs:
    match = re.search('(?<=Μοντέλο:\s)\d{4}', element, re.IGNORECASE)
    year.append(match.group())    
    
    #screen
for element in specs:
    match = re.search('(?<=Οθόνη:\s).+["]', element, re.IGNORECASE)
    screen.append(match.group()) 
    
    #battery
for element in specs:
    match = re.search('(?<=Μπαταρία:\s)\d+mAh', element, re.IGNORECASE)
    battery.append(match.group())  
    
print(len(mobile_models))

print(len(year))
print(len(screen))
print(len(battery))
print(len(memory))

print(len(stars))
print(len(reviews_count))
print(len(prices))

mobile_phones = pd.DataFrame({
    'Model':mobile_models,
    'Year':year,
    'Screen':screen,
    'Battery':battery,
    'Memory':memory,
    'Star_Rating':stars,
    'Reviews_Count':reviews_count,
    'Prices':prices, 
    

})

mobile_phones.to_csv('Mobile_Features.csv', encoding='utf-8-sig')






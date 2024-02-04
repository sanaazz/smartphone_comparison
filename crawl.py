import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd
import time



def res(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    while True :
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            break
        else:
            time.sleep(3)
    return res


        
        
class Crawl():
    
    def __init__(self):
        self.phone_links = list()
        self.brands = ['alcatel','Apple','Asus','BLU','HTC','Huawei','Infinix','Lenovo','LG','Nokia','Sony','Xiaomi','ZTE','Samsung']
        self.brands_link = list()
        self.url = 'https://www.gsmarena.com/'
        self.crawl_brands()
        self.phone_crawl()
    
    
    def create_csv_file(self,name,listofeverything):
        with open('./{}.csv'.format(name),'+a') as f:
            for line in listofeverything:
                f.write(line+'\n')
    
    def crawl_brands(self):
        response = res(self.url)
        soup = BeautifulSoup(response.content,'html.parser')
        soup = soup.find_all('ul')[2]
        soup = soup.find_all('li')
        
        for i in soup:
            if i.text in self.brands :
                print(i.text , 'Link crawled')
                self.brands_link.append(self.url+i.find('a')['href'])
                
        self.create_csv_file('brands_link',self.brands_link)
                
                
    def phone_crawl(self):
        for brand in self.brands_link:
            response = res(brand)
            soup = BeautifulSoup(response.content,'html.parser')
            soup = soup.find('div',class_='makers')
            soup = soup.find_all('li')
            for i in soup:
                self.phone_links.append(self.url+i.find('a')['href'])

        self.create_csv_file('phone_links',self.phone_links)
            
            

        
            
    
if __name__ == '__main__':
    Crawl()
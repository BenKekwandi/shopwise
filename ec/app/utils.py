from bs4 import BeautifulSoup
import requests 
import lxml

def get_boravin_link_data(url):
    # Request the page
    page = requests.get(url)
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Extract the product name
    name = soup.find('h1', class_='urun_ismi').get_text()
    
    # Extract the product price
    price = soup.find_all(class_='urun_fiyati')
    print_price = [title.text for title in price]
    
    # Convert the price to float
    price_str = print_price[0].split()[0].replace('.', '').replace(',', '.')
    price_float = float(price_str)
    
    # Convert the price to USD
    conversion_rate = 0.031 
    price_usd = price_float * conversion_rate
    
    # Format the price to two decimal places
    price_usd = round(price_usd, 2)
    
    # Print the name and price in USD
    print(f"{name}")
    print(f"{price_usd:.2f} USD")
    
    # Return the name and price in USD
    return name, price_usd

def get_beyaz_link_data(url):
    # Request the page
    page = requests.get(url)
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Extract the product price
    price = soup.find_all(class_='woocommerce-Price-amount amount')
    current_price = price[1].text
    
    # Convert the price to float
    current_price_value = float(current_price.replace('$', '').replace(',', '').strip())
    
    return current_price_value
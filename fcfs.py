import smtplib
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from config import *

# Mongo Connection
client = MongoClient('localhost:27017')

# Properties Database
db = client.Properties


def scrape_all():
    scrape_lyon()
    scrape_rnb()
    scrape_vienna()
    scrape_furgeson()
    scrape_cornette()
    scrape_action()
    scrape_sacdelt()


def scrape_furgeson():
    print("Scraping Furgeson\n")
    url = "https://showmojo.com/d654722075/listings/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('div',attrs={'class':'iframeListing'})

    for listings in data:
        links = listings.findAll('a')

        for a in links:
            link = "https://showmojo.com" + a['href']
            exists = db.rentals.find_one({"link": link})
            if(exists):
                print("Already exists")
            else:
                print("New Listing: " + link)
                db.rentals.insert_one({"link": link})
                send_notification(link)


def scrape_vienna():
    print("Scraping Vienna")
    url = "https://secure.rently.com/api/properties/searchQuery?pc=1&bathrooms=&bedrooms=&min=&max=&managerID=6830"
    response = requests.get(url).json()  # NO SOUP FOR YOU!
    for dispensary in response["property_data"]:
        link = "https://homes.rently.com/homes-for-rent/properties/" + str(dispensary['id'])
        exists = db.rentals.find_one({"link": link})
        if(exists):
            print("Already exists")
        else:
            print("New Listing: " + link)
            db.rentals.insert_one({"link": link})
            send_notification(link)


def scrape_rnb():
    print("Scraping RNB\n")
    url = "http://rnb2day.com/include/searchHomesList.php?colTitle=default&colPos=Up&antelope_v=no&auburn_v=no&carmichael_v=no&citrusHeights_v=no&davis_v=no&galt_v=no&graniteBay_v=yes&lincoln_v=no&loomis_v=yes&elDoradoHills_v=no&elkGrove_v=no&fairOaks_v=no&folsom_v=no&natomas_v=no&newcastle_v=yes&northHighlands_v=no&orangevale_v=no&penryn_v=yes&rocklin_v=yes&ranchoCordova_v=no&ranchoMurieta_v=no&roseville_v=yes&sacramento_v=yes&walnutGrove_v=no&westSacramento_v=no&woodland_v=no&propertyType_v=Any&bedrooms_v=-1&bathrooms_v=0&rentMin_v=0&rentMax_v=0&pets_v=Yes&poolSPA_v=NoPref&dummy=1562813835116"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('tr')

    # Check for new listings and insert them into the database
    for listings in data:
        links = listings.findAll('a')

        for a in links:
            if(a['href'] != "javascript: void(0);"):
                exists = db.rentals.find_one({"link": "http://rnb2day.com/" + a['href']})
                if(exists):
                    print("Already exists")
                else:
                    print("New Listing: http://rnb2day.com/" + a['href'])
                    db.rentals.insert_one({"link": "http://rnb2day.com/" + a['href']})
                    send_notification("http://rnb2day.com/" + a['href'])


def scrape_lyon():
    print("Scraping Lyon\n")
    url = "https://golyonpm.appfolio.com"       # Lyon Property Management
    response = requests.get(url+"/listings")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('div',attrs={'class':'listing-item','class':'result'})

    # Check for new listings and insert them into the database
    for listings in data:
        links = listings.findAll('h2',attrs={'class':'listing-item__title'})

        for h2 in links:
            a = h2.find('a',href=True)
            exists = db.rentals.find_one({"link": url + a['href']})
            if(exists):
                print("Already exists")
            else:
                print("New Listing: " + url + a['href'])
                db.rentals.insert_one({"link": url + a['href']})
                send_notification(url + a['href'])


def scrape_sacdelt():
    print("Scraping SacDelt\n")
    url = "https://sacdelta.appfolio.com/"       # Sacramento Delta
    response = requests.get(url+"/listings")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('div',attrs={'class':'listing-item','class':'result'})

    # Check for new listings and insert them into the database
    for listings in data:
        links = listings.findAll('h2',attrs={'class':'listing-item__title'})

        for h2 in links:
            a = h2.find('a',href=True)
            exists = db.rentals.find_one({"link": url + a['href']})
            if(exists):
                print("Already exists")
            else:
                print("New Listing: " + url + a['href'])
                db.rentals.insert_one({"link": url + a['href']})
                send_notification(url + a['href'])


def scrape_action():
    print("Scraping Action Properties\n")
    url = "https://actionproperties.appfolio.com"       # Action Property Management
    response = requests.get(url+"/listings")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('div',attrs={'class':'listing-item','class':'result'})

    # Check for new listings and insert them into the database
    for listings in data:
        links = listings.findAll('h2',attrs={'class':'listing-item__title'})

        for h2 in links:
            a = h2.find('a',href=True)
            exists = db.rentals.find_one({"link": url + a['href']})
            if(exists):
                print("Already exists")
            else:
                print("New Listing: " + url + a['href'])
                db.rentals.insert_one({"link": url + a['href']})
                send_notification(url + a['href'])


def scrape_cornette():
    print("Scraping Cornette\n")
    url = "https://cornette.appfolio.com"       # Cornette Property Management
    response = requests.get(url+"/listings")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('div',attrs={'class':'listing-item','class':'result'})

    # Check for new listings and insert them into the database
    for listings in data:
        links = listings.findAll('h2',attrs={'class':'listing-item__title'})

        for h2 in links:
            a = h2.find('a',href=True)
            exists = db.rentals.find_one({"link": url + a['href']})
            if(exists):
                print("Already exists")
            else:
                print("New Listing: " + url + a['href'])
                db.rentals.insert_one({"link": url + a['href']})
                send_notification(url + a['href'])

def send_notification(rental_link):
    msg = "\nNew Rental Listed:" + rental_link
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_gmail, sender_password)
    server.sendmail(sender_gmail, recipient_email, msg)
    server.quit()


def main():
    scrape_all()

if __name__ == "__main__":
    main()

"""
File name: main.py
Author: faelb (faelb@gmx.at)
Date created: 22/12/2020
Date last modified: 22/12/2020
Python Version: 3.9
This program crawls website data from Mjam.net
to find out wether a restaurant is down or available.
If it is currently down, the program will poll the website every 5 seconds
and play an alarm sound if it is available again.
"""
import getpass #just to get username from system
# to check if URL is a valid URL
import validators
# to get the html text from requests
import requests
# to parse specific stuff out of html from requests
from bs4 import BeautifulSoup
# für alarmsound wiedergabe
from playsound import playsound
# file for alarmsound
from time import sleep

mamacitaURL = "https://www.mjam.net/restaurant/wien/mamacita-california-burritos-1100/?origin=list"
mp3File = "src/security.mp3"
global restaurantURL


def getRestaurantLoop():
    print(f'Hi, {getpass.getuser()}!\n'
          f'Please copy the URL of your MJAM restaurant and paste it in here - then press enter')
    while True:
        restaurantURL = input("...waiting for input:")
        cleanURL = checkURL(restaurantURL)

        if cleanURL:
            print("program is now trying to find Restaurant status...")
            html = getResponseContent(cleanURL)
            statusParagraph = getParagraphContent(html)
            if statusParagraph is None:
                print("something went wrong - please try again, maybe check your URL")
            elif not statusParagraph:
                print("------------------------------------")
                print("Restaurant available - why did you even ask me?")
                print("------------------------------------")
                exit(1)
            elif statusParagraph == "Momentan keine Lieferung oder Vorbestellung möglich.":
                print("momentan down - wir alarmieren dich wenn das Lokal wieder Bestellungen annimmt")
                sleep(2)
                while True:
                    sleep(15)
                    html = getResponseContent(cleanURL)
                    statusParagraph = getParagraphContent(html)
                    if not statusParagraph:
                        print("------------------------------------")
                        print("Restaurant available - make your order!")
                        print("------------------------------------")
                        playsound(mp3File)
                    else:
                        print("still not available - asking again in 15 seconds")

        else:
            print("something with your URL was wrong (not mjam, invalid URL...) - please try again\n")


def checkURL(url):
    # first get rid of spaces, then if the url doesnt contain mjam.net or
    # it contains it but the url isnt valid (validators), it will not return a clean url to work with
    cleanURL = url.replace(" ", "")
    if validators.url(cleanURL):
        if "mjam.net" in cleanURL:
            return cleanURL
    else:
        return False


def getResponseContent(url):
    return requests.get(url).text


def getParagraphContent(htmlText):
    soup = BeautifulSoup(htmlText, "html.parser")
    for text in soup.findAll("div", {"class": "ZurKassaButton Cart__Button"}):
        return str(text.find("p")).replace("<p>", "").replace("</p>", "")


if __name__ == '__main__':
    getRestaurantLoop()

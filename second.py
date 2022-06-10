from bs4 import BeautifulSoup
import requests
import gspread

url = input("Please paste page's link: ")
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
gc = gspread.service_account(filename="creds.json")
sh = gc.open('scrapetosheets').sheet1

if 'facebook' in html_text:
    name = soup.find('h1', class_='title style-scope ytd-video-primary-info-renderer')
    about = soup.find('div', id='title style-scope ytd-video-primary-info-renderer')
    print(name)
    print(about)
    sh.append_row([name, about])
    sh.update('A2', input("Note: "))
else:
    print("Sorry, this isn't a facebook page!")



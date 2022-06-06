from bs4 import BeautifulSoup
import requests

url = input("Please paste page's link: ")
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html5lib')

if 'youtube' in html_text:
    name = soup.find('h1', class_='title style-scope ytd-video-primary-info-renderer')
    about = soup.find('div', id='title style-scope ytd-video-primary-info-renderer')
    print(name)
    print(about)
else:
    print("Sorry, this isn't a youtube page!")


# Importing beautiful soup library and requests
from bs4 import BeautifulSoup
import requests

# Anime Scraper class to scrape the anime from source
class AnimeScraper:
    # fetch anime method is scraping anime from MyAnimeLists.com
    # It fetches the anime title, type, genre, number of episodes and year it has been aired from
    # Time Complexity => O(n) + Request time from url => Might take a while depending on internet connectivity
    # Space Complexity => O(n), n is the number of anime fetched from the source
    def fetchAnime(self, url, param):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        anime_list = {}
        index = 1
        for sub_heading in soup.find_all('a', class_="hoverinfo_trigger fl-l fs14 fw-b"):
            anime_list[index] = [sub_heading.text]
            index += 1
        
        index = 1
        if param == 'upcoming':
            for sub_heading in soup.find_all('div', class_="information di-ib mt4"):
                n = " ".join(sub_heading.text.split())
                l = n.split()
                anime_list[index].append(l[0])
                anime_list[index].append(l[1][1:])
                anime_list[index].append(" ".join(l[3:4]))
                index += 1
            
            return anime_list

        elif param == 'airing':
            for sub_heading in soup.find_all('div', class_="information di-ib mt4"):
                n = " ".join(sub_heading.text.split())
                l = n.split()
                anime_list[index].append(l[0])
                anime_list[index].append(l[1][1:])
                anime_list[index].append(" ".join(l[3:5]))
                index += 1
        
        return anime_list

    
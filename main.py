import urllib3
from tqdm import tqdm
from bs4 import BeautifulSoup

year = input("Enter the year: ")
genre = input("Enter your desired Genre: ")
url = "https://www.imdb.com/search/title?title_type=feature&release_date=" + year + "," + year + "&genres=" + genre
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "html.parser")
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
counter = 1
for div in tqdm(movieList):
    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

    for items in header:
        title = header[0].findChildren('a')
        print(f"{counter}. " + str(title[0].contents[0]))
        print(f"https://www.imdb.com/{str(title[0].attrs['href'])}")
    genre = div.findChildren('span', attrs={'class': 'genre'})
    genre_text = genre[0].text
    print('Genre: ' + genre_text + '\n')
    p_all = div.findAll('p', attrs={'class': 'text-muted'})
    desc = p_all[1].text
    print('Description: ' + desc + '\n')
    counter += 1
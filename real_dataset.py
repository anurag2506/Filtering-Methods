import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/moviemeter/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles, years, ratings = [], [], []
    movie_items = soup.find_all('div', class_='ipc-metadata-list-summary-item__tc')

    for movie in movie_items:
        title_element = movie.find('h3', class_='ipc-title__text')
        title = title_element.text.strip() if title_element else 'N/A'
        titles.append(title)

        year_element = movie.find('span', class_='sc-ab348a5d-8')
        year = year_element.text.strip() if year_element else 'N/A'
        years.append(year)

        rating_element = movie.find('div', {'data-testid': 'ratingGroup-container'})
        rating = rating_element.text.strip() if rating_element else 'N/A'
        ratings.append(rating)

    if len(titles) == len(years) == len(ratings):
        movies_data = pd.DataFrame({'Title': titles, 'Year': years, 'IMDb Rating': ratings})
        movies_data.to_csv('movie_recommendations.csv', index=False)
        print("Data scraped and saved to 'movie_recommendations.csv'")
    else:
        print(f"Error: The lengths of the data arrays do not match. Titles: {len(titles)}, Years: {len(years)}, Ratings: {len(ratings)}")


import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb URL for most popular movies
url = 'https://www.imdb.com/chart/moviemeter/'

# Add headers to avoid potential blocking
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the IMDb website with headers
response = requests.get(url, headers=headers)

# Check for successful request
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lists to store the scraped data
    titles = []
    years = []
    ratings = []

    # Find the movie items on the page
    movie_items = soup.find_all('div', class_='ipc-metadata-list-summary-item__tc')

    # Iterate over each movie in the list
    for movie in movie_items:
        # Extract movie title
        title_element = movie.find('h3', class_='ipc-title__text')
        if title_element:
            title = title_element.text.strip()
            titles.append(title)

        # Extract year of release
        year_element = movie.find('span', class_='sc-ab348a5d-8')
        if year_element:
            year = year_element.text.strip()
            years.append(year)

        # Extract IMDb rating
        rating_element = movie.find('div', {'data-testid': 'ratingGroup-container'})
        if rating_element:
            rating = rating_element.text.strip()
        else:
            rating = 'N/A'  # Assign 'N/A' if rating is not available
        ratings.append(rating)

    # Create a DataFrame to store the scraped data
    movies_data = pd.DataFrame({
        'Title': titles,
        'Year': years,
        'IMDb Rating': ratings
    })

    # Save the DataFrame to a CSV file
    movies_data.to_csv('movie_recommendations.csv', index=False)

    print("Data scraped and saved to 'movie_recommendations.csv'")
else:
    print(f"Failed to retrieve IMDb page. Status code: {response.status_code}")

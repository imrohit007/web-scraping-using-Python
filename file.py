import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the website
url = "https://www.imdb.com/chart/top"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the movie data
table = soup.find("table", {"class": "chart full-width"})

# Open a CSV file for writing with UTF-8 encoding
with open("top_movies.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Title", "Year", "Rating"])

    # Iterate over each row in the table
    for row in table.tbody.find_all("tr"):
        # Find the title and year of the movie
        title_column = row.find("td", {"class": "titleColumn"})
        title = title_column.a.text
        year = title_column.span.text.strip("()")

        # Find the rating of the movie
        rating_column = row.find("td", {"class": "ratingColumn imdbRating"})
        rating = rating_column.strong.text

        # Write the data for the movie to the CSV file
        writer.writerow([title, year, rating])

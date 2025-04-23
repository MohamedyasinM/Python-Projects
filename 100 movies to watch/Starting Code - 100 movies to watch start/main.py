import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL).text


soup = BeautifulSoup(response,"html.parser")

all_= soup.find_all(name="h3" , class_="title")

for i in range (len(all_) -1 , -1 , -1):
    movie = all_[i]
    movie1 = movie.getText()
    with open("movies.txt",mode="a" , encoding="utf-8") as file:
        file.write(movie1 + "\n")





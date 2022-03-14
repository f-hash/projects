"""Get movie data method."""
import os
import requests

from dotenv import find_dotenv, load_dotenv  # import the dotenv file

load_dotenv(find_dotenv())
api_key = os.getenv("movie_key")
BASE_URL = "https://api.themoviedb.org/3/movie/"
query_params = {"api_key": os.getenv("movie_key")}


def getmovie(index):
    """This is the function that gets the movie"""
    movie_id = index
    url = BASE_URL + str(movie_id)
    img_url = "http://image.tmdb.org/t/p/w500"
    response = requests.get(url, query_params)

    picpath = response.json()["poster_path"]
    pic = img_url + picpath
    title = response.json()["title"]
    tag = response.json()["tagline"]
    genlist = []
    for i in response.json()["genres"]:
        genlist.append(i["name"])
    # print(genlist)
    wiki_url = "https://en.wikipedia.org/w/api.php"
    para = {
        "action": "opensearch",
        "namespace": "0",
        "search": title,
        "limit": "1",
        "format": "json",
    }
    response = requests.get(wiki_url, para)
    wiki = response.json()
    wikipage = wiki[3][
        0
    ]  # if this happens refresh the page the list has ran out so refresh to see a new movie
    print(wikipage)
    print(title, tag, pic, genlist, pic, wiki)
    # print(wikipage)

    return {
        "wikipage": (wikipage),
        "title": (title),
        "tag": (tag),
        "genlist": (genlist),
        "pic": (pic),
        "movieid": (movie_id),
    }

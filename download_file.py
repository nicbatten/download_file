#!/usr/bin/env python
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(get_response.content)
    print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://media1.tenor.com/images/fa395dfc3172219eee7bc528b07f29b4/tenor.gif")

#!/usr/bin/env python
import requests

def download(url):
    get_response = requests.get(url)
    print(get_response.content)
    with open("sample.txt", "w") as out_file:
        out_file.write("This is a test")

download("https://media1.tenor.com/images/fa395dfc3172219eee7bc528b07f29b4/tenor.gif?itemid=4420482")

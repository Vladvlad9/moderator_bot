import json

data_words = []

with open("cenz.txt", encoding="utf-8") as file:
    for i in file:
        word = i.lower().split("\n")[0]
        if word != "":
            data_words.append(word)

with open("cenz.json", "w", encoding="utf-8") as fileJSon:
    json.dump(data_words, fileJSon)
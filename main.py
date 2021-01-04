
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла

def get_top_ten(text):
    words = text.split(" ")
    words = [word.lower() for word in words if len(word) >= 6]

    unique_words = list()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    def sort_by_most_common(word):
        counter = 0
        for i in words:
            if i == word:
                counter += 1
        return (counter)

    unique_words.sort(key=sort_by_most_common, reverse=True)
    top_ten = unique_words[:10]
    print(top_ten)

# JSON
import json

with open("newsafr.json", "r") as f:
    json_data = json.load(f)
    json_items = json_data["rss"]["channel"]["items"]
    text = ""
    for jsoni in json_items:
        text += jsoni["title"] + " "
        text += jsoni["description"] + " "
    get_top_ten(text)


# XML
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item")

text = ""
for xmli in xml_items:
   text += xmli.find("title").text + " "
   text += xmli.find("description").text + " "
get_top_ten(text)
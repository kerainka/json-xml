import xml.etree.ElementTree as ET
import json

def get_top_news(text, min_len_word=6, top_number=10):
    words = text.split(" ")
    words = [word.lower() for word in words if len(word) >= min_len_word]
    frequency = dict()
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1

    def sort_by_most_common(word):
        return frequency[word]

    unique_words = set(words)
    unique_words_list = list(unique_words)
    unique_words_list.sort(key=sort_by_most_common, reverse=True)
    top_news = unique_words_list[:top_number]
    print(top_news)


def get_top_news_json():
    with open("newsafr.json", "r") as f:
        json_data = json.load(f)
        json_items = json_data["rss"]["channel"]["items"]
        text = ""
        for jsoni in json_items:
            text += jsoni["title"] + " "
            text += jsoni["description"] + " "
        get_top_news(text)


def get_top_news_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")

    text = ""
    for xmli in xml_items:
        text += xmli.find("title").text + " "
        text += xmli.find("description").text + " "
    get_top_news(text)


get_top_news_xml()
get_top_news_json()

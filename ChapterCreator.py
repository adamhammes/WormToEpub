__author__ = 'adamhammes'

import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import re

class Chapter:
    def __init__(self, url = None, fileName = None):
        """
        Constructs a Chapter from a URL or file name
        """
        chunk = SoupStrainer(name = re.compile(r"article|meta|link"))
        if url:
            r = urllib2.urlopen(url)
            html = r.read()
            self.soup = BeautifulSoup(html, parse_only = chunk)
            self.setData()
        elif fileName:
            self.soup = BeautifulSoup(open(fileName), parse_only = chunk)
        self.soup.encode(formatter = "minimal")
        self.setData()

    def setData(self):
        self.setText()
        self.setMetadata()
        self.setNextLink()

    def setNextLink(self):
        tag = self.soup.find("a", {"title": "Next Chapter"})
        if not tag:
            tag = self.soup.find("link", {"rel": "next"})
        self.nextLink = tag["href"]

    def setText(self):
        self.textList = []
        article = self.soup.find("article")
        for tag in article.findAll("a"):
            tag.replaceWith(tag.text)

        for paragraph in article.findAll("p"):
            text = paragraph.encode("UTF-8")
            text.strip()
            self.textList.append(text)

        self.textList.pop(0)
        self.textList.pop(-1)

    def setMetadata(self):
        arcList =  ["Gestation", "Insinuation", "Agitation", "Shell", "Hive",
                    "Tangle", "Buzz", "Extermination", "Sentinel", "Parasite",
                    "Infestation", "Plague", "Snare", "Prey", "Colony", "Monarch",
                    "Migration", "Queen", "Scourge", "Chrysalis", "Imago", "Cell",
                    "Drone", "Crushed", "Scarab", "Sting", "Extinction",
                    "Cockroaches", "Venom"]

        tag = self.soup.find("meta", {"property": "og:title"})
        self.title = tag["content"].encode("UTF-8")

        index = self.title.find(" ")
        str = self.title[:index]
        if str == "Interlude":
            arcNum = int(re.findall("\d+", self.title)[0]) -1
            self.arc = arcList[arcNum]
        else:
            self.arc = str


    def writeRawToFile(self, name, delimiter):
        f = open(name, "w")
        for paragraph in self.textList:
            f.write(delimiter + paragraph)
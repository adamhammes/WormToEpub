__author__ = 'adamhammes'

import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import re

class Chapter:
    def __init__(self, url = None, fileName = None):
        """
        Constructs a Chapter from a URL
        """
        chunk = SoupStrainer(name = re.compile(r"article|meta"))
        if url:
            r = urllib2.urlopen(url)
            html = r.read()
            self.soup = BeautifulSoup(html, parse_only = chunk)
            self.setData()
        if fileName:
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
            # Newer chapters don't store the next link as nicely
            tag = self.soup.find("a", {"rel": "next"})
        if tag:
            self.nextLink = tag["href"]
        else:
            self.nextLink = None

    def setText(self):
        self.textList = []

        for paragraph in self.soup.findAll("p"):
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
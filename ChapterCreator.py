__author__ = 'adamhammes'

import urllib2
from BeautifulSoup import BeautifulSoup

class Chapter:


    def __init__(self, url = None):
        """
        Constructs a Chapter from a URL
        """
        if url is not None:
            r = urllib2.urlopen(url)
            html = r.read()
            self.soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)
            self.setData()

    def fromFileName(self, name):
        self.soup = BeautifulSoup(open(name), convertEntities=BeautifulSoup.HTML_ENTITIES)
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
        chapter = self.soup.find("article")
        self.text_list = []

        for paragraph in chapter.findAll("p"):
            text = paragraph.getText().encode("UTF-8")
            text.strip()
            self.text_list.append(text)

        self.text_list.pop(0)
        self.text_list.pop(-1)

    def setMetadata(self):
        tag = self.soup.find("meta", {"property": "og:title"})
        self.title = tag["content"]

        index = self.title.find(" ")
        self.arc = self.title[:index].strip()


    def writeRawToFile(self, name, delimiter):
        f = open(name, "w")
        for paragraph in self.text_list:
            f.write(delimiter + paragraph)







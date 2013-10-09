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
        self.setTitle()
        self.setNextLink()


    def setNextLink(self):
        self.nextLink = self.soup.find("a", {"rel": "next"})["href"]

    def setText(self):
        self.soup.prettify()
        chapter = self.soup.find("article")
        self.text_list = []

        for paragraph in chapter.findAll("p"):
            text = paragraph.getText().encode("UTF-8")
            text.strip()
            self.text_list.append(text)

        self.text_list.pop(0)
        self.text_list.pop(-1)

    def setTitle(self):
        raw_title = self.soup.title.string
        index = raw_title.index("|")
        self.title = raw_title[:index-1]


    def writeRawToFile(self, name, delimiter):
        f = open(name, "w")
        for paragraph in self.text_list:
            f.write(delimiter + paragraph)







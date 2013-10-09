__author__ = 'adamhammes'

from ChapterCreator import Chapter

c = Chapter()
c.fromFileName("foo.txt")

links = c.soup.find("a", {"rel": "next"})

print links["href"]

__author__ = 'adamhammes'
from ChapterCreator import Chapter

c = Chapter("http://parahumans.wordpress.com/2013/09/17/interlude-28/")
f = open("foo.txt", "w")

print c.arc

c.writeRawToFile("foo.txt", "\n\n")
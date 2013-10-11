__author__ = 'adamhammes'

from ChapterCreator import Chapter

c = Chapter("http://parahumans.wordpress.com/2011/06/11/1-1/")

f = open("html.html", "w")
f.write("<meta charset = \"UTF-8\"/>")
f.write("<h1><center>" + c.title + "</center></h1>\n")

for paragraph in c.text_list:
    f.write("\t<p>" + paragraph + "</p>\n")

f.write("</h1")











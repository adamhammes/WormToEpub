__author__ = 'adamhammes'

from ChapterCreator import Chapter

f = open("html.html", "w")
f.write("<meta charset = \"UTF-8\"/>")

nextLink = "http://parahumans.wordpress.com/2011/06/11/1-1/"

while nextLink:
    c = Chapter(nextLink)
    print c.arc
    f.write("<h1><center>" + c.title + "</center></h1>\n")

    for paragraph in c.textList:
        f.write("\t" + paragraph + "\n")

    f.write("</h1>")
    nextLink = c.nextLink










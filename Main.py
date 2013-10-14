__author__ = 'adamhammes'

from ChapterCreator import Chapter

f = open("Worm.html", "w")
f.write("<meta charset = \"UTF-8\">")
f.write("<title>Worm Arcs 1-10</title>")
f.write("<meta name = \"author\" content = \"Wildbow\">")

nextLink = "http://parahumans.wordpress.com/2012/05/19/infestation-11-1/"
title = ""
while title != "Interlude 20":
    c = Chapter(url = nextLink)
    print c.title
    f.write("<h1><center>" + c.title + "</center></h1>\n")

    for paragraph in c.textList:
        f.write("\t" + paragraph + "\n")

    f.write("</h1>")
    nextLink = c.nextLink
    title = c.title
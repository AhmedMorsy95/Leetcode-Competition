import codecs
from bs4 import BeautifulSoup
import collections

f=codecs.open("leetcode.html", 'r')
page = f.read()

soup = BeautifulSoup(page,"html.parser")
soup = soup.findAll('tbody')
soup = soup[0]
soup = soup.findAll('tr')

easy = {}
medium = {}
hard = {}

counter = 0
for tr in soup:
    lst =  list(tr.children)
    number = int(lst[1].text)
    link = lst[2]
    link = link.find('a')['href']
    level = lst[5].text
    if level == "Hard":
        hard[number] = link
    elif level == "Easy":
        easy[number] = link
    else:
        medium[number] = link        
    
easy = collections.OrderedDict(sorted(easy.items()))
medium = collections.OrderedDict(sorted(medium.items()))
hard = collections.OrderedDict(sorted(hard.items()))


f = open("hard.md","w")
f.write("| Problem Numer | Name | Solved | Category |\n")
f.write("| :-----------: | :--: | :----: | -------- |\n")
for key,val in hard.items():
    name = val.split("/")
    line = "| " + str(key) + "| [" + name[-1] + "](" + val + ")  | " + ":x: | ??? |\n"
    f.write(line)

f.close
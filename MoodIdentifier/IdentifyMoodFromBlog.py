'''
Identify the impact of mood based on the positivity and negativity of words present in text of blog/website

Mood polatity is identified based on the word-mood list mentioned in below web page
https://espierspectives.wordpress.com/2010/09/26/list-of-tone-and-mood-words/

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
#import numpy as np
import pandas as pd
import string 
from matplotlib import pyplot as plt


url = str(input("Enter the blog url: ")) #"https://althouse.blogspot.com/"
try :
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
except :
    print ("Invalid url ")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)
mood = pd.read_csv('Mood_list.csv')
mood=mood[["Polarity","Words"]].drop_duplicates()

worddf=pd.DataFrame (columns=["Words"])
for word in text.split():    
    word=word.translate(str.maketrans('', '', string.punctuation)).lower()
    worddf=worddf.append({'Words': word} , ignore_index=True)

mooddf=pd.merge(mood,worddf,on="Words", how="inner" )
moodDf=mooddf.groupby('Polarity')['Words'].value_counts()
print(moodDf)

#plot Pie chart
moodDf.groupby("Polarity").sum().plot(kind='pie',autopct='%.2f%%')
plt.title("Mood generation")
plt.show()


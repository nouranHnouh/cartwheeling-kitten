import requests
from bs4 import BeautifulSoup 

#get the html of a webbrowser using requests 
url='https://www.nytimes.com/'
r=requests.get(url)
#acesss the text-based content 
r_html=r.content
#print r_html
#page downloaded sucessfullt 
#print r.status_code

#pulling data out of html files 
soup=BeautifulSoup(r_html,'html.parser')

#show the contents of the page 
#print (soup.prettify)

#print the article titles of new york times 
#loop through all the elements on the page with class
#name "story-heading"
for story_heading in soup.find_all('h2',class_="story-heading"):
	# if the story headings that are links, print out the text
    # and format it nicely
	if story_heading.a:
		#acess only the text related to the links 
		print (story_heading.a.text.replace('/n'," ").strip())
    # otherwise, take the contents out and format it nicely
	else:
		#access the title 
		print (story_heading.contents[0].strip())




#returns information that is associated with specific tag 
#print(soup.find_all('h2',class_="story-heading"))

#print text relate with tag p at index 2
#print(soup.find_all('p')[2].get_text())

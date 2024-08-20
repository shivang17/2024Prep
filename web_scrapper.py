# Let's scrap the html of the given webpage
"""
    Parse all the html content behind a webpage. Get rid of the html tags and extract the actual data. 

    Let's write a program to extract the contents of top questions of stackoverflow. 

    First step is to install beautifulsoup4 to extract html   
"""

import requests

response = requests.get("https://www.stackoverflow.com/questions")
# print(response.text) # This will give raw HTML of the above URL. However, we can use beautiful soup to have a visually appealing data. 

from bs4 import BeautifulSoup
# Pass the html content to the BeautifulSoup class.

soup = BeautifulSoup(response.text, "html.parser")
#print(soup) #This will return the html, now soup object will contain the select method that can take a css selector. So, let's pass the selector after finding the class name by inspecting

questions = soup.select(".s-post-summary")
# print(questions[0].select(".s-post-summary--stats-item")[0])
print(questions)
for question in questions:
    print(question.select_one(".s-post-summary--stats-item").getText())
# We can instead use, select_one
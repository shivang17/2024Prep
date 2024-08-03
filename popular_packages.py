# excel_spreadsheets, pdf, browser_automation, website_scraping, 

# What is an API?

# It is a way to interact with another system which has certain business data that you may need access for. The business can give certain information for free and above certain calls to their server, it might cost some money. Irrespective, let's try to understand the technical side of things. 


import requests
import config

# requests.get(url)
# response = requests.get("https://api.nasa.gov/planetary/apod")
# Any requests of the API has two sections, header and payload section.
url = "https://api.nasa.gov/planetary/apod"
api_key = config.api_key
headers = {
    "Authorization": api_key
}
params = {
    "api_key": api_key,
    "thumbs": True,
    "date": "2024-04-21"
}
response = requests.get(url, params=params)

print(response.json())
# If above was an array, we can make similar changes. 
# List comprehension -> [item for item in list if someCondition]

# In order to hide the API key, we will need to have the value in a separate file and do not commit to the git
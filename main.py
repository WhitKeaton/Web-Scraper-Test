# the following line goes into the shell to create a virtual environment 
# python -m pip install requests
import requests


# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

# creating a URL object
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# retrieving the URL 

# printing the .text attributes
#print(page.text)
# successful retrieval and print of static HTML data  

# Note: Keep in mind that every website will look different. 
#It’s necessary to inspect and understand the structure of the site

# the object BeautifulSoup takes in the content that was scraped earlier
# the second argument "html.parser" enforces that the correct parser 
# is used for HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Note: You’ll want to pass page.content instead of page.text to avoid 
# problems with character encoding

# all job listings are contained in this ID
results = soup.find(id="ResultsContainer")

# not sure what prettify does, but it cleans up the format somehow?
print(results.prettify())

# now I'd like to sort by each card using the following
job_elements = results.find_all("div", class_="card-content")
# .find_all() returns an iterable of all job listings

# function that runs through the previously created iterable
for job_element in job_elements:
	print(job_element, end="\n"*2)

for job_element in job_elements:
	title_element = job_element.find("h2", class_="title")
	company_element = job_element.find("h3", class_="company")
	location_element = job_element.find("p", class_="location")
	print(title_element.text.strip())
	print(company_element.text.strip())
	print(location_element.text.strip())
	print()

# you can use python_jobs = results.find_all("h2", string="Python")
# to search for job listings that contain the keyword "python", 
# but the function only looks for that EXACT string

# this function will manipulate formatting and look for the string 
python_jobs = results.find_all(
	"h2", string=lambda text: "python" in text.lower()
)
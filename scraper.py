import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# Creating Function that takes url from command line and extracts title, body text and outlinks from that page using selenium 
def get_page_data(url):
    
    # Starting chrome browser
    driver = webdriver.Chrome()
    
    # Opening the given url
    driver.get(url)

    # Getting title of page
    if driver.title:
        title = driver.title
    else:
        title = "No title"

    # Getting body text safely
    elements = driver.find_elements(By.TAG_NAME, "body")
    if elements:
        body_text = elements[0].text
    else:
        body_text = ""

    # Collecting all links from page
    links = []
    link_elements = driver.find_elements(By.TAG_NAME, "a")
    for e in link_elements:
        href = e.get_attribute("href")
        if href:
            links.append(href)

    # Closing browser after work is done
    driver.quit()

    return title, body_text, links     # Returning title, body_text and outlinks


# Checking correct number of command line arguments
if len(sys.argv) != 2:
    print("Command line arguments should be like: python scraper.py url")
    sys.exit(1)

url = sys.argv[1]

# Calling function to fetch page data
title, body_text, links = get_page_data(url)

print()          # For better readability in output
print("TITLE:", title)
print()    
print("BODY_TEXT:", body_text)
print()
print("OUTLINKS:")

# Printing links one by one
for link in links:
    print(link)
print()

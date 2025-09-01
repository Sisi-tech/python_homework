# The program should import from selenium and webdriver_manager, as shown in your lesson.  You also need pandas and json.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import pandas as pd 
import json 

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size-1920,1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)


# Task 1: Review robots.txt to Ensure Policy Compliance
robots_url = "https://durhamcountylibrary.org/robots.txt"
driver.get(robots_url)
print(driver.page_source)

# Task 2 Understanding HTML and the DOM for the Durham Library Site
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
first_result_li = driver.find_element(By.CSS_SELECTOR, "li.cp-search-result-item")
title = first_result_li.find_element(By.CSS_SELECTOR, ".title-content").text 
authors = [a.text for a in first_result_li.find_elements(By.CSS_SELECTOR, ".author-link")]
info = first_result_li.find_element(By.CSS_SELECTOR, ".cp-format-info").text

print("\nFirst Search Result:")
print("Title:", title)
print("Authors:", authors)
print("Format & Year:", info)

# Task 3: Write a Program to Extract this Data
results = []
results_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print(f"Found {len(results_items)} search results")

for li in results_items:
    title = li.find_element(By.CSS_SELECTOR, ".title-content").text
    authors = [a.text for a in li.find_elements(By.CSS_SELECTOR, ".author-link")]
    text = "; ".join(authors) if authors else "N/A"
    try:
        info = li.find_element(By.CSS_SELECTOR, ".cp-format-info").text 
    except:
        info = "N/A"

    book = {
        "Title": title,
        "Author": authors,
        "Format-Year": info
    }
    results.append(book)

df = pd.DataFrame(results)
print("\nDataFrame of the results: ", df)

# Task 4: Write out the Data
df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By 
import csv 
import time 

driver = webdriver.Chrome()

try:
    driver.get("https://owasp.org/www-project-top-ten/")
    time.sleep(3)
    elements = driver.find_elements(By.XPATH, "//li/a[contains(@href, 'Top10')]")
    top_10 = []
    for element in elements[:10]:
        title = element.text
        href = element.get_attribute("href")
        top_10.append({"title": title, "link": href})
    
    print(top_10)
    
    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(top_10)
finally:
    driver.quit()
    
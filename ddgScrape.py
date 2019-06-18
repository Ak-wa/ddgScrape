import os
import sys
import time
print("""
-	ddgScrape - A Duckduckgo scraper	-
[ ] Usage: python ddgScrape.py <search term> <search result amount>
[ ] Make sure to have chromedriver.exe in the same folder!
[ ] If you find any bug, feel free to contact me on github:
[ ] https://github.com/ak-wa

""")
search_term = ""
if len(sys.argv) <= 1:
	print("[-] You forgot to add a search term!")
	sys.exit()
else:
	pass
if len(sys.argv) <= 2:
	print("[-] You forgot to add an amount of search results!")
else:
	search_term = str(sys.argv[1])

try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from bs4 import BeautifulSoup
except ImportError as error:
	print("[+] One or more modules not found, installing them with pip...")
	os.system("pip install selenium")
	os.system("pip install bs4")
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from bs4 import BeautifulSoup
links =[]
output_list = open("ddg_output.txt","a")
page_counter = 0
def duckduckgo(query, needed):
    global page_counter
    options = Options()
    options.headless = False
    browser = webdriver.Chrome("chromedriver.exe", options=options)
    browser.get("https://duckduckgo.com/")
    search = browser.find_element_by_name('q')
    search.send_keys(query + Keys.RETURN)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    while len(links) < int(sys.argv[2]):
        for text in soup.find_all('a', {'class': 'result__a'}):
            href = text.get('href')
            links.append(href)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            page_counter += 1
            xpath_string = "//*[@id="+"rld"+"-"+str(page_counter)+"]/a"
            try:
                browser.find_element_by_class_name('result--more__btn').click()
            except:
                pass
if search_term == "":
	pass
else:
	duckduckgo(search_term, sys.argv[2])
	for link in links:
		print(link)
		output_list.write(link+"\n")
	print("[+] Wrote output into ddg_output.txt")

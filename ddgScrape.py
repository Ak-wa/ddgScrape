import os
import sys
print("""
-	ddgScrape - A Duckduckgo scraper	-
[ ] Usage: python ddgScrape.py <search term>
[ ] Make sure to have chromedriver.exe in the same folder!
[ ] If you find any bug, feel free to contact me on github:
[ ] htps://github.com/ak-wa

""")
search_term = ""
if len(sys.argv) < 2:
	print("[-] You did not provide a search term!")
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
output_list = open("ddg_output.txt","w+")
def duckduckgo(query, needed):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome("chromedriver.exe", options=options)
    browser.get("http://duckduckgo.com")
    search = browser.find_element_by_name('q')
    search.send_keys(query + Keys.RETURN)
    html = browser.page_source

    soup = BeautifulSoup(html, "lxml")
    while len(links) < needed:
        for text in soup.find_all('a', {'class': 'result__a'}):
            href = text.get('href')
            links.append(href)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
if search_term == "":
	pass
else:
	duckduckgo(search_term, 200)
	for link in links:
		print(link)
		output_list.write(link+"\n")
	print("[+] Wrote output into ddg_output.txt")

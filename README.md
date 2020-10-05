# ddgScrape [deprecated project]
![python](https://img.shields.io/pypi/pyversions/Django.svg)
![size](https://img.shields.io/github/size/ak-wa/ddgScrape/ddgScrape.py.svg)
![lastcommit](https://img.shields.io/github/last-commit/ak-wa/ddgScrape.svg)
![follow](https://img.shields.io/github/followers/ak-wa.svg?label=Follow&style=social)

A tool for scraping search query results from DuckDuckGo.com
* Written in Python3 with Selenium, using Chromedriver, tested with Python v3.7.3.
* Results are automatically saved into ddg_output.txt in the same folder.
* To make this work, make sure to place Chromedriver.exe in the same path!
* If required modules are not installed, the script will attempt to install them with pip.
### Usage:
`python ddgScrape.py <search term> <result amount>` 

![](preview_2.gif)

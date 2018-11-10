# Description

This is a web scraping program, that collects names of random things from https://www.randomlists.com/things


# How it works 
1. It visits the page https://www.randomlists.com/things
2. Scraping the names of the random things listed on the webpage
3. Using Selenium and Chrome Driver (headless) to select, and programatically "click" the Return button to generate new random things
4. Repeat these procedures for 100 times
5. Finally, the datas are saved to a json file


# Installation Requirement
- python3
- beautifulSoup
- selenium
- progress


# How to use
```
python random_things_scraper.py 
```

# Demo data
- Check out the file data.json


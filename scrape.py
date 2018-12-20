from bs4 import BeautifulSoup
from splinter import Browser
import requests
import time
import pandas as pd
import re


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    #call to browser path
    browser = init_browser()

    #target site
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find(class_='content_title').text
    print(news_title)
    news_p = soup.find(class_='rollover_description_inner').text
    print(news_p)

    #Visit the url for JPL Featured Space Image here.
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #storing sites html in the html var
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #clicking the full image button on the main page
    browser.click_link_by_partial_text('FULL IMAGE')

    #waiting
    time.sleep(2)

    #clicking the more info button on second page
    browser.click_link_by_partial_text('more info')

    #waiting
    time.sleep(2)

    # Make sure to find the image url to the full size .jpg image.
    browser.click_link_by_partial_href('/spaceimages/images/largesize')

    #wating
    time.sleep(2)

    # Make sure to save a complete url string for this image.
    featured_image_url = browser.url

    print(featured_image_url)

    # Visit the Mars Weather twitter account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    #storing sites html in the html var
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # scrape the latest Mars weather tweet from the page

    mars_weather = soup.find(class_='js-tweet-text-container').text

    # Save the tweet text for the weather report as a variable called mars_weather.
    print(mars_weather)

    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    url = 'http://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables

    type(tables)

    df = tables[0]
    df.columns = ['Measuremnet','Value']
    df

    # Use Pandas to convert the data to a HTML table string.
    html_table = df.to_html()
    html_table

    #clean table a bit
    html_table.replace('\n', '')

    # Save the table, better off just doing it I guess?
    df.to_html('table.html')


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    #storing sites html in the html var
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #waiting
    time.sleep(1)


    ######################################### Valles Marineris Hemisphere
    browser.click_link_by_partial_text('Valles Marineris')

    #waiting
    time.sleep(1)

    #click on sample button to go to full image
    browser.click_link_by_text('Sample')

    #waiting
    time.sleep(1)

    #activate second window
    browser.windows.current = browser.windows[1]

    #grab image url 
    Valles_Marineris = browser.windows.current.url
    print(Valles_Marineris)

    #go back to main window
    browser.windows.current = browser.windows[0]

    #waiting
    time.sleep(1)

    #go back to main site
    browser.back()

    #waiting
    time.sleep(1)

    ######################################## Valles Cerberus Hemisphere

    browser.click_link_by_partial_text('Cerberus Hemisphere')

    #waiting
    time.sleep(1)

    #click on sample button to go to full image
    browser.click_link_by_text('Sample')

    #waiting
    time.sleep(1)

    #activate second window
    browser.windows.current = browser.windows[2]

    #grab image url 
    Cerberus_Hemisphere = browser.windows.current.url
    print(Cerberus_Hemisphere)

    #go back to main window
    browser.windows.current = browser.windows[0]

    #waiting
    time.sleep(1)

    #go back to main site
    browser.back()

    ######################################## Valles Schiaparelli Hemisphere

    browser.click_link_by_partial_text('Schiaparelli Hemisphere')

    #waiting
    time.sleep(1)

    #click on sample button to go to full image
    browser.click_link_by_text('Sample')

    #waiting
    time.sleep(1)

    #activate second window
    browser.windows.current = browser.windows[3]

    #grab image url 
    Schiaparelli_Hemisphere = browser.windows.current.url
    print(Schiaparelli_Hemisphere)

    #go back to main window
    browser.windows.current = browser.windows[0]

    #waiting
    time.sleep(1)

    #go back to main site
    browser.back()

    ######################################## Valles Schiaparelli Hemisphere

    browser.click_link_by_partial_text('Syrtis Major')

    #waiting
    time.sleep(1)

    #click on sample button to go to full image
    browser.click_link_by_text('Sample')

    #waiting
    time.sleep(1)

    #activate second window
    browser.windows.current = browser.windows[4]

    #grab image url 
    Syrtis_Major = browser.windows.current.url
    print(Syrtis_Major)

    #go back to main window
    browser.windows.current = browser.windows[0]

    #waiting
    time.sleep(1)

    #go back to main site
    browser.back()

    # create blank list and dictonary
    hemisphere_image_urls = []

    # create keys for dictonary
    keys = ['title', 'img_url']

    # create each list that will be appended to dict 
    hem1 = ['Valles_Marineris', Valles_Marineris ]
    hem2 = ['Cerberus_Hemisphere',  Cerberus_Hemisphere]
    hem3 = ['Schiaparelli_Hemisphere', Schiaparelli_Hemisphere]
    hem4 = ['Syrtis_Major', Syrtis_Major]

    #append each list item to hemisphere list as dict
    hemisphere_image_urls.append(dict(zip(keys, hem1)))
    hemisphere_image_urls.append(dict(zip(keys, hem2)))
    hemisphere_image_urls.append(dict(zip(keys, hem3)))
    hemisphere_image_urls.append(dict(zip(keys, hem4)))
    
    print (hemisphere_image_urls)

    return(hemisphere_image_urls)

init_browser()
scrape()

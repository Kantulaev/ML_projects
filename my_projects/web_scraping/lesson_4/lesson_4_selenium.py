from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.adamchoi.co.uk/bttsresult/detailed')

all_match_button = driver.find_element_by_xpath('//label[@analytics-event = "All matches"]')
all_match_button.click()

dropdown = Select(driver.find_element_by_id('season'))
dropdown.select_by_visible_text('17/18')

time.sleep(3)

matches = driver.find_elements_by_tag_name('tr')
date = []
home_team = []
score = []
guest_team = []

for match in matches[:100]:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    guest_team.append(match.find_element_by_xpath('./td[4]').text)

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'guest_team': guest_team})

print(df)
df.to_csv('matches.csv', index=False)

driver.quit()


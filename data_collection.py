from selenium import webdriver

website = 'https://adamchoi.co.uk/teamgoals/detailed'
path = '/Users/micha/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath(
    '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

for match in matches:
    print(match.text)

driver.quit()
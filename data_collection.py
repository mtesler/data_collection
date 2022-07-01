from selenium import webdriver

website = 'https://adamchoi.co.uk/teamgoals/detailed'
path = '/Users/micha/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()

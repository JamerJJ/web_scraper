from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

#URL starting from the first page
URL_1 = "https://www.glassdoor.ie/Reviews/index.htm?overall_rating_low=3.5&page=1&locId=2739035&locType=C&locName=Dublin,%20Co.%20Dublin%20(Ireland)&filterType=RATING_OVERALL"

#URL used to alterate page nums.
URL_2 = "https://www.glassdoor.ie/Reviews/index.htm?overall_rating_low=3.5&page=796&locId=2739035&locType=C&locName=Dublin,%20Dublin&filterType=RATING_OVERALL"




driver = webdriver.Chrome()
driver.get(URL_2)
sleep(20)

#Setting window for a specific value
driver.set_window_size(1920,1080)
sleep(10)

#Finding the path for the 'cookies' button
accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
accept_cookies_button.click()
sleep(10)

#Setting a stop for the loop so i will run for 50 pages (over 50 was taking too long) 
stop = 50
name_list = []

while stop != 0:
    #Path for the company name, the information that I wanted to scrap
    company_name = driver.find_elements(By.XPATH, "//div[@data-test = 'employer-card-single']//span[contains(@class, 'align-items-center mb-xsm')]//h2")

    for company in company_name:
        name_list.append(company.text)

    next_button = driver.find_element(By.XPATH, '//*[@id="Explore"]/div[3]/div[1]/div[4]/div[3]/div/div/div[1]/button[7]')
    next_button.click()
    sleep(10)

    stop -= 1

    with open("company_names.txt", "w") as file:
        for name in name_list:
            file.write(name + "\n")


driver.quit()



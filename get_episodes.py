from selenium import webdriver
import time

def log_url(url):
    f = open("IDs.txt", "a")
    f.write((str((url + "\n"))))
    f.close()

driver = webdriver.Chrome('/home/user/Downloads/chromedriver')
driver.get("https://www.netflix.com/watch/80002472/")

# Really really hacky way of getting credentials set. User has 42 seconds to
# log in and return to ep1 URL.
time.sleep(40)
print("I AM AWAKE. 2 seconds remaining.")
time.sleep(2)

# During this stage, the mouse must be kept active over the browser window.
# Recommend having terminal on top and moving mouse between the 2 windows.
for i in range(206):
    time.sleep(3)
    button = driver.find_element_by_xpath('//*[@id="netflix-player"]/div[4]/section[2]/div[5]/div[1]')
    button.click()
    log_url(driver.current_url)

driver.quit()

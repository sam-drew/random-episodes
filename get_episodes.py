from selenium import webdriver
import time

def log_id(ID):
    f = open("IDs.txt", "a")
    f.write((str((ID + "\n"))))
    f.close()
    print("Logging ID: " + ID)

def strip_id(url):
    splitString = url.rsplit("?", 1)
    splitString = splitString[0].rsplit("/")
    ep_id = splitString[len(splitString) - 1]
    return(ep_id)

driver = webdriver.Chrome('/home/user/Downloads/chromedriver')
last_id = "80006978"
driver.get("https://www.netflix.com/watch/80006978")

# Really really hacky way of getting credentials set. User has 42 seconds to
# log in and return to ep1 URL.
time.sleep(40)
print("I AM AWAKE.\n2 seconds remaining.\nMake sure you're on ep1 page.")
time.sleep(2)

# User manualy clicks through the episodes until reaches S9E24. Logs as url
# changes.
while last_id != "80144357":
    if strip_id(driver.current_url) != last_id:
        log_id(strip_id(driver.current_url))
        last_id = strip_id(driver.current_url)

driver.quit()

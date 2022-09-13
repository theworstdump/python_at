from selenium import webdriver
import time

url = "https://dev.metal-archives.com"
driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject_AT\\venv\\chromedriver\\chromedriver.exe")
try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


#teeeeest2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#url of home page to fill the school code
baseurl = "http://schoolreportcards.in/src-new/AboutDISE/Aboutdise.aspx"
driver = webdriver.Firefox(executable_path = '/home/priyank/gecko/geckodriver')
driver.get(baseurl)

#Filling school code in textbox using send_keys
driver.find_element(By.ID, "txtSearchSchool").send_keys('29271204402')
time.sleep(1)

#clicking on the button Go to move to actual PDF
button = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div[2]/a[2]/img")
button.click()

# button2 = driver.find_element(By.ID, "IconImg_CRViewReport_toptoolbar_export")
# button2.click()

driver.close()

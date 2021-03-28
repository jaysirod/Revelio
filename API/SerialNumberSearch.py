# SerialNumberSearch.py

# NetGear Warranty Information Page Scraper
# For RowdyHacks 2021

#Import Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Identify Netgear products
def getNetGearProduct( product_id ):
	# Needed code for website execution
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
	try:
		# Get to Netgear Warranty Website
		driver.get("https://www.netgear.com/mynetgear/registration/Product_WarrantyCheck.aspx")
		
		# Locate certain attributes
		serialNumber = driver.find_element_by_id("MainContent_inputSerialNumber")
		serialNumEnter = driver.find_element_by_id( "MainContent_btnCheck")
		serialNumber.send_keys(str(product_id) )
		# Send product id and await
		serialNumEnter.click()
		delay = 3
		
		# Return product ID
		getProdID = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'MainContent_lblProduct')))
		return getProdID.text
	
	# Catch TimeOut
	except TimeoutException:
		# Check if its not an actual timeout
		try:
			error = driver.find_element_by_class_name('active')				
			return str(error.text)
		except:
			try:
				error = driver.find_element_by_id("MainContent_errorSection")
				return str(error.text)
			except:
				return None
	# Exit gracefully
	finally:
		try:
			driver.quit()
		except:
			pass


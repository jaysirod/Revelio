#Import Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import json, requests, urllib.parse


def getProductsByBrand( vendor ):
	QUERY = str(vendor)
	API_URL = "https://cve.circl.lu/api/browse/" + QUERY
	
	try:
		data = requests.get(API_URL)
		rData = ""
		for d in data.text:
			if d is not "\n":
				rData += d
				continue
				
			if d is "\"":
				rData += "\'"
				
		
		return rData
	except:
		return "Invalid Query"
		
	finally:
		try:
			driver.quit()
		except:
			pass


def getCVEs( vendor, product ):
	QUERY = str(vendor) + "/" + str(product)
	API_URL = "https://cve.circl.lu/search/" + QUERY
	
	# Needed code for website execution
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
	try:
			# Get to CVE Website
			driver.get( API_URL )
		
			# Return product ID
			
			getCVETable = driver.find_elements_by_xpath("//table/tbody/tr/td")
			QUERY_LIST = []
			for CVEs in getCVETable:
				if CVEs.text is not "":
					QUERY_LIST.append( CVEs.text )
			
			return QUERY_LIST
	except:
		return "Invalid Query"
		
	finally:
		try:
			driver.quit()
		except:
			pass

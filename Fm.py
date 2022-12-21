from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"C:\Users\puneet\Downloads\chromedriver.exe")       #initializing the chrome driver as a agent
browser.get('http://www.screener.in/company/TCS/consolidated/')                             

el=browser.find_element_by_id("peers")                  #getting the data of peers table
peers=el.find_element_by_class_name("table-responsive")

ql=browser.find_element_by_id("quarters")               #getting the data of the quaters table
quarters=ql.find_element_by_class_name("table-responsive")

wl=browser.find_element_by_id("annuals")                 #getting the data of the annuals table
annuals=wl.find_element_by_class_name("table-responsive")

xl=browser.find_element_by_id("balancesheet")           #getting the data of the balancesheet table
balancesheet=xl.find_element_by_class_name("table-responsive")

al=browser.find_element_by_id("cashflow")               #getting the data of the cashflow table
cashflow=al.find_element_by_class_name("table-responsive")

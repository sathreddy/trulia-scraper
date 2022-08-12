from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages/webdriver_manager')
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.trulia.com/c/il/urbana/710-w-california-ave-1-710-w-california-ave-urbana-il-61801--2437274287")

# print(driver.title)
address_el = driver.find_element(By.CLASS_NAME, 'Text__TextBase-sc-1cait9d-0.ifMipu')
city_state_el = driver.find_element(By.CLASS_NAME, 'HomeSummaryShared__AddressH1-mmeem6-1.jfWpXg')
print(city_state_el.text)
# address = address_el.text
# city = city_state_el.text.split(', ')[0]
# state = city_state_el.text.split(', ')[1].split(' ')[0]
# zip_code = city_state_el.text.split(', ')[1].split(' ')[1]
# rent=""
# year_built=""
# Days_on_Trulia=""
# Type=""
# Sqft=""
# Phone_Number=""
# Bedroom_min=""
# Bedroom_max=""
# Bathroom_min=""
# Bathroom_max=""
# Assault=""
# Arrest=""
# Theft=""
# Vandalism=""
# Burglary=""
# Crime_Other=""
# Elementary_School_Count=""
# Elementary_School_Avg_Score=""
# Middle_School_Count=""
# Middle_School_Avg_Score=""
# High_School_Count=""
# High_School_Avg_Score=""
# Driving=""
# Transit=""
# Walking=""
# Cycling=""
# Restaurant=""
# Groceries=""
# Nightlife=""
# Cafe=""
# Shopping=""
# Entertainment=""
# Beauty=""
# Active_life,Latitude,Longitude,EPA_Region,Population,Input_area(sq. miles),Particulate_Matter,Ozone,NATA*_Diesel_PM,NATA*_Air_Toxics_Cancer_Risk,NATA*_Respiratory_Hazard_Index,Traffic_Proximity_and_Volume,Lead_Paint_Indicator,Superfund_Proximity,RMP_Proximity,Hazardous_Waste_Proximity,Wastewater_Discharge_Indicator,Demographic_Index%,Minority_Population%,Low_Income_Population%,Linguistically_Isolated_Population%,Population_with_Less_Than_High_School_Education%,Population_under_Age_5%,Population_over_Age_64%,URL,Short_form_ID
# print(driver.page_source)
driver.quit()
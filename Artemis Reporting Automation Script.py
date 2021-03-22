from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains


def crop_screenshot(element,driver, filename='cropped.png'):
	location = element.location_once_scrolled_into_view
	size = element.size
	png = driver.get_screenshot_as_png() # saves screenshot of entire page
	im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']
	im = im.crop((left, top, right, bottom)) # defines crop points
	im.save(filename) # saves new cropped image


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://app.artemishealth.com/auth/login')

#Logging in
username = driver.find_element_by_id('username')
username.clear()
username.send_keys('daniel.lee@marshmma.com')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/button').click()
time.sleep(1)
password = driver.find_element_by_id('password')
password.clear()
password.send_keys('Laugh13!')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/button').click()
time.sleep(30)

#Setting the Time Periods
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[3]/app-analysis-settings-display').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/app-analysis-settings-picker/div/div/div/div[1]/div[1]/select').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/app-analysis-settings-picker/div/div/div/div[1]/div[1]/select/option[3]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/app-analysis-settings-picker/div/toolbar/div/div[3]/button').click()
#current_time_period = driver.find_element_by_class_name('extent')
#action = ActionChains(driver)
##action.move_to_element_with_offset(current_time_period,10,10).click_and_hold().move_by_offset(-10,0).release().perform()

#Selecting the right client
client_name = input('Client Name: ').upper()
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[3]/div[1]').click()
select_client = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[3]/div[1]/ul/li[2]/div/input')
select_client.send_keys(str(client_name))
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'{0}')]".format(client_name)).click()

#Click into Standard Stories from main page
time.sleep(20)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/div').click()

#Click into Executive Summary in Standard Stories
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-standard-story-list/app-standard-story-layout/div[1]/div[2]/dashboard-card[1]').click()

#Screenshot and save image
driver.fullscreen_window()
time.sleep(15)
#Screenshot Executive Summary Demographics
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-executive-summary/app-standard-story-layout/div[1]/div[2]/section[1]')
crop_screenshot(element,driver,'Executive Summary-Demographics.png')

#Scrolling down to financial summary and screenshotting
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-executive-summary/app-standard-story-layout/div[1]/div[2]/section[2]')
driver.execute_script('arguments[0].scrollIntoView(true);',element)
crop_screenshot(element,driver,'Executive Summary-FinancialSummary.png')
#Scrolling down and screenshotting Clinical Profile
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-executive-summary/app-standard-story-layout/div[1]/div[2]/section[3]')
driver.execute_script('arguments[0].scrollIntoView(true);',element)
crop_screenshot(element,driver,'Executive Summary-Clinical Profile.png')
#Scrolling down and screenshotting Utilization Metrics
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-executive-summary/app-standard-story-layout/div[1]/div[2]/section[4]')
driver.execute_script('arguments[0].scrollIntoView(true);',element)
crop_screenshot(element,driver,'Executive Summary-Utilization Metrics.png')
#clicking "Standard Stories" Button to go to main page
driver.find_element_by_xpath('//a[@href="/standard-stories/list"]').click()
#click on High Cost Medical + Rx Card
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-standard-story-list/app-standard-story-layout/div[1]/div[2]/dashboard-card[5]').click()
#Clicking into and Screenshot HCC Med+Rx
time.sleep(20)
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-hcc-med-rx/app-standard-story-layout/div[1]/div[2]/section/div[1]')
crop_screenshot(element,driver,'HCC Med+Rx-First Half.png') #screenshots the first half of the HCC Med+RX
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-hcc-med-rx/app-standard-story-layout/div[1]/div[2]/section/div[2]')
crop_screenshot(element,driver,'HCC Med+Rx-Second Half.png') #screenshots the second half of HCC Med+Rx
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-hcc-med-rx/app-standard-story-layout/div[1]/div[2]/section/div[4]/div[1]/app-hcc-table/app-simple-table-chart/table')
crop_screenshot(element,driver,'HCC Med+Rx-Top 10 HCC List.png') #screenshots HCC Top 10 List of HCC Med+Rx
#Back to Main Page of Standard Story
driver.find_element_by_xpath('//a[@href="/standard-stories/list"]').click()
#Clicking into and Screenshotting Actionable Overspending
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-standard-story-list/app-standard-story-layout/div[1]/div[2]/dashboard-card[2]').click()
time.sleep(5)
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]')
crop_screenshot(element,driver,'Actionable Overspending.png') #screenshots Actionable Overspending
#Back to Main Page of Standard Story
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
#Clicking into and Screenshot Pharmacy Story
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-standard-story-list/app-standard-story-layout/div[1]/div[2]/dashboard-card[7]').click()
time.sleep(10)
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-pharmacy/app-standard-story-layout/div[1]/div[2]/section/div[1]')
crop_screenshot(element,driver,'Pharmacy-First Part.png') #screenshots the First part of Pharmacy Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-pharmacy/app-standard-story-layout/div[1]/div[2]/section/div[2]')
crop_screenshot(element,driver,'Pharmacy-Second Part.png') #screenshots the Second part of Pharmacy Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-pharmacy/app-standard-story-layout/div[1]/div[2]/section/div[3]')
crop_screenshot(element,driver,'Pharmacy-Third Part.png') #screenshots the Third part of Pharmacy Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-pharmacy/app-standard-story-layout/div[1]/div[2]/section/div[4]')
crop_screenshot(element,driver,'Pharmacy-Top 5 Drugs by Paid.png') #screenshots the Top 5 Drugs by Paid Table in Pharmacy Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-pharmacy/app-standard-story-layout/div[1]/div[2]/section/div[5]')
crop_screenshot(element,driver,'Pharmacy-Top 5 Drugs by Utilization.png') #screenshots the Top 5 Drugs by Utilization Table in Pharmacy Story
#Back to Main Page of Standard Story
driver.find_element_by_xpath('//a[@href="/standard-stories/list"]').click()
#Clicking into and Screenshotting Population Health Story
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-standard-story-list/app-standard-story-layout/div[1]/div[2]/dashboard-card[8]').click()
time.sleep(10)
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-population-health/app-standard-story-layout/div[1]/div[2]/section[1]/div[2]')
crop_screenshot(element,driver,'Population Health-First Part.png') #screenshots the First part of Population Health Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-population-health/app-standard-story-layout/div[1]/div[2]/section[1]/div[3]')
crop_screenshot(element,driver,'Population Health-Second Part.png') #screenshots the Second part of Population Health Story
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/app-population-health/app-standard-story-layout/div[1]/div[2]/section[2]')
crop_screenshot(element,driver,'Population Health-Clinical Profile Section.png') #screenshots the Clinical Profile section of Population Health Story
#Going to Visualize app to get Top 10 CMS Chronic Diagnosis
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/a[8]').click()
#Click on CMS Top 10 Chronic Diagnosis
driver.find_element_by_xpath("//*[@class='entity-item-piece large entity-item-name']/div[contains(text(),'CMS Top 10 Chronic Diagnosis')]").click()
time.sleep(15)
element = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/table')
crop_screenshot(element,driver,'CMS Top 10 Chronic Diagnosis.png') #screenshots the CMS Top 10 Chronic Diagnosis
print('Job Done!!!')
driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
driver.get('https://formy-project.herokuapp.com/form')
job = driver.find_element(By.ID, 'job-title' )
job.send_keys('IT')

educatie = driver.find_element(By.ID, 'radio-button-1')
educatie.click()

gender = driver.find_element(By.ID, 'checkbox-3')
gender.click()
driver.quit()

# ● Link text
driver.get('https://www.apple.com/')
driver.find_element(By.LINK_TEXT, 'AirPods').click()
driver.find_element(By.LINK_TEXT, 'AirPods Max').click()
driver.find_element(By.LINK_TEXT, 'Tech Specs').click()
driver.quit()

# ● Parțial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'Only on').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'News').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'TV').click()
driver.quit()
# ● Name
driver.get('https://altex.ro/contact/')

driver.find_element(By.NAME, 'fullName').send_keys('Popescu Cristian')
driver.find_element(By.NAME, 'phone').send_keys('0700123654')
driver.find_element(By.NAME, 'search').send_keys('nimic')
driver.quit()
# ● Tag*
driver.get('https://altex.ro/contact/')
input_list = driver.find_elements(By.TAG_NAME,'input')
input_list[6].send_keys('alabalaportocala')
input_list[5].send_keys('alabalaportocala')
input_list[4].send_keys('alabalaportocala')

# ● Class name*
driver.get('https://phptravels.net/')

driver.find_element(By.CLASS_NAME, 'select2-selection__arrow').click()
driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys('Bucharest')
sleep(7)
driver.find_element(By.CLASS_NAME, 'select2-results__options').click()
driver.find_element(By.CLASS_NAME, 'ladda-label').click()

# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)

driver.get('https://phptravels.net/')
driver.find_element(By.CSS_SELECTOR, 'input#checkin').click()
driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.CSS_SELECTOR, 'input[class="validate[required,custom[email]]"]').send_keys('email.emailEMAIL123890@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Name *"]').send_keys('Macovei')
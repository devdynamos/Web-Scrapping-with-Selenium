import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create or open an Excel file with a specific filename and path
def create_or_open_workbook(filename):
    try:
        workbook = openpyxl.load_workbook(filename)
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        workbook.active.title = 'Doctor Data'
    return workbook

# Save data to the Excel file
def save_in_excel(workbook, pic, name, dtype, number, highlight, bio, points):
    sheet = workbook['Doctor Data']
    row = [pic, name, dtype, number, highlight, bio, points]
    sheet.append(row)

# Your scraping function
def scrape_doctor(profile_link, workbook, browser):
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    browser.get(profile_link)
    time.sleep(2)

    profile_picture = browser.find_element(By.XPATH, '//div[@class="pic-stats--pic"]//img').get_attribute('src')
    name = browser.find_element(By.XPATH, '//div[@class="name-bio--name"]//h2').text
    doc_type = browser.find_element(By.XPATH, '//div[@class="name-bio--name"]//h4').text
    phone_number = browser.find_element(By.XPATH, '//a[@id="btn-profile_phone-view"]').get_attribute('data')

    try:
        highlights = browser.find_element(By.XPATH, '//div[@class="result-highlights"]//ul').text
    except:
        highlights = None

    try:
        bio = browser.find_element(By.XPATH, '//div[@class="name-bio--bio__text  "]//a').get_attribute('data-modal')
    except:
        bio = None

    profile_points = browser.find_element(By.XPATH, ' //span[@class="current-count"]').get_attribute('data-to')

    print(name, phone_number, profile_points)

    save_in_excel(workbook, pic=profile_picture,
                      name=name,
                      dtype=doc_type,
                      number=phone_number,
                      highlight=highlights,
                      bio=bio,
                      points=profile_points)

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

# Main program
if __name__ == "__main__":
    # Specify the path and filename where you want to save the Excel file
    workbook = create_or_open_workbook('path/to/your/excel_file.xlsx')

    browser = webdriver.Chrome()
    browser.get('https://www.doctor.com/90033/Family-Doctors')

    while True:
        cards = browser.find_elements(By.XPATH, '//hgroup//a[@class="result-provider-name"]')
        for card in cards:
            profile_link = card.get_attribute("href")
            scrape_doctor(profile_link, workbook, browser)

        time.sleep(2)
        next_button = browser.find_element(By.XPATH, '//li[@class="next"]')

        if next_button:
            next_button.click()
            time.sleep(4)
        else:
            break

    # Save the Excel file after scraping all data
    workbook.save('C:/Users/Taha/OneDrive/Desktop/beautifulsoap/doctor.xlsx')

    browser.quit()

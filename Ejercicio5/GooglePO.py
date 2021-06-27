from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePO:
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def goToGoogle(self):
        self.driver.get("http://www.google.com")

    def clickOnSearchButton(self, element):
        searchButton = element.find_element_by_class_name("gNO89b")
        self.driver.execute_script("arguments[0].click();", searchButton)
    
    def clickOnLuckyButton(self, element):
        luckyButton = element.find_element_by_class_name("RNmpXc")
        self.driver.execute_script("arguments[0].click();", luckyButton)

    def typeAndSearch(self, query, mode = 'normal'):
        searchInput = self.driver.find_element_by_name("q")
        searchInput.clear()
        searchInput.send_keys(query)
        searchList = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "UUbT9"))
        )

        if(mode == 'normal'):
            self.clickOnSearchButton(searchList)
        if(mode == 'lucky'):
            self.clickOnLuckyButton(searchList)
        if(mode == 'return'):
            searchInput.send_keys(Keys.RETURN)
            
    
    def getTitle(self):
        return self.driver.title

    def getResultsStats(self):
        return self.driver.find_element_by_id("result-stats").text

    def goToPage(self, page):
        querySelector = f"a[aria-label='Page {page}']"
        pageTwoButton = self.driver.find_elements_by_css_selector(querySelector)[0]
        pageTwoButton.click()

    def goToImageSection(self):
        imageLink = self.driver.find_elements_by_css_selector("a[class='hide-focus-ring']")[0]
        imageLink.click()

    def getFirstImage(self):
        firstImage = self.driver.find_element_by_class_name("rg_i")
        firstImage.click()

    def getImagePreview(self):
        return self.driver.find_element_by_id('islsp')

    def getImagePreviewStatus(self):
        imagePreviewer = self.getImagePreview()
        return imagePreviewer.is_displayed()
    
    def closeImagePreview(self):
        imagePreviewerCloseButton = self.getImagePreview().find_element_by_class_name('YSqQ6e')
        imagePreviewerCloseButton.click()
    
    def close(self):
        input()
        self.driver.quit()
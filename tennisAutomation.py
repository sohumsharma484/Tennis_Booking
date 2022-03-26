# Program first tested to work 4/12/2021
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pause
import time
import traceback

class Tennis:
    
    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.otherCourt = False
    
        self.driver.get("https://canyoncreekhoa.tennisbookings.com/LoginX.aspx")
    
    def book(self, month, day, startTime, endTime, court="c2"):
        self.login()
        self.makeReservation(month, day, startTime, endTime, court)
        

    def login(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsername"))
        )
        element.clear()
        element.send_keys("ronikasharma@yahoo.com")
    
        element = self.driver.find_element_by_id("txtPassword")
        element.clear()
        element.send_keys("908dad")
    
        element = self.driver.find_element_by_id("btnLogin")
        element.click()
    
        time.sleep(0.2)
    
        try:
            element = self.driver.find_element_by_xpath("//*[starts-with(@id, 'btnCancelConf')]")
            element.click()
        except Exception as e:
            error_message = traceback.format_exc()
            with open("errors.txt", "a") as fileObject:
                fileObject.write(error_message + "\n\n")
        
        time.sleep(0.1)
        self.driver.save_screenshot("loggedIn.png")
    
    def makeReservation(self, month, day, startTime, endTime, court):
        # Wait till desired time
        dt = datetime.datetime(2021, int(month), int(day), 7, 0, 0, 1)
        now = datetime.datetime.now()
        try:
            self.driver.switch_to.frame("ifMain")
    
            # element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located(By.XPATH, f'//*[text()="{day}"]')
            # )
            elements = self.driver.find_elements_by_xpath(f"//*[text()='{day}']")
            for element in elements:
                if "sel" in element.get_attribute("class"):
                    element.click()
                    break
                # self.driver.find_element_by_xpath(f"//a[starts-with(@class, 'calendarsel') and text()='{day}']")
                # self.driver.find_element_by_xpath(f"//*[@class='calendarsel' and text()='{day}']")
    
            time.sleep(0.5)
            self.driver.save_screenshot("bookingPage.png")
    
            self.driver.switch_to.frame("mygridframe")

            try:
                element1 = self.driver.find_element_by_id(f"r{startTime}{court}")
                element1.click()
                print(f"end {endTime} start {startTime}")
                if not endTime == startTime:
                    element = self.driver.find_element_by_id(f"r{endTime}{court}")
                    if element.get_attribute('class') == "x":
                        element1.click()
                        alkfjsal
                    element.click()
            except:
                if self.otherCourt == False:
                    self.otherCourt = True
                    court = "c1"
                    #self.makeReservation(month, day, startTime, endTime, "c1")
                    print("past")
                    element = self.driver.find_element_by_id(f"r{startTime}{court}")
                    element.click()
                    print(f"end {endTime} start {startTime}")
                    if not endTime == startTime:
                        element = self.driver.find_element_by_id(f"r{endTime}{court}")
                        element.click()


    
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("ifMain")
            try:
                element = self.driver.find_element_by_id("btnnext")
                element.click()

                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("dialogIF")

                element = self.driver.find_element_by_id("btnConfirmAndPay")
                self.driver.save_screenshot("bef oreClick.png")

                if dt.day - now.day == 3 and dt.hour < 7:
                    pause.until(dt)
                print("22")
                element.click()
                time.sleep(1)
                self.driver.save_screenshot("afterClick.png")
            except:
                print("in except")
                if self.otherCourt == False:
                    self.otherCourt = True
                    # element = self.driver.find_element_by_xpath("//*[starts-with(@id, 'btnCloseAlert')]")
                    # print(element)
                    # element.click()
                    # element.click()
                    self.book(month, day, startTime, endTime, "c1")
    
            #self.driver.quit()
        except Exception as e:
            error_message = traceback.format_exc()
            with open("errors.txt", "a") as fileObject:
                fileObject.write(error_message + "\n\n")


if __name__ == '__main__':
    with open("errors.txt", "a") as fileObject:
        fileObject.write("will it work \n")
        fileObject.close()

    import sys
    with open("errors.txt", "a") as fileObject:
        fileObject.write(f"{str(sys.argv)} \n")
        fileObject.close()
    book = Tennis()
    print(sys.argv)
    date = str(sys.argv[1]).split("-")
    year, month, day = int(date[0]), int(date[1]), int(date[2])
    book.book(month, day, sys.argv[2], sys.argv[3])











from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException




class UnilagBallot:

    def __init__(self, data):
        # Parameter initialization
        self.email = data['matric']
        self.password = data['password']
        self.driver =  webdriver.Chrome()
    
    def login (self):
        print("loading website..")
    
        success = False
        while not success:
            delay = 5
            # to keep trying infinitly even when the browser times out.
            try:
                self.driver.get("https://studentportal.unilag.edu.ng/login")
                success = False
                while not success:
                    #to keep trying to load the website infinitly until the log-in form loads
                    try:
                        # to check if the user is already logged it 
                        try:
                            print("checking if alreday logged it..")
                            user_prof= self.driver.find_element(By.ID,'user-profile')
                            if user_prof:
                                print("already logged in..") 
                        except NoSuchElementException:
                            print("not logged in, so logging in now")
                            print("checking to see if the page has loaded..")
                            # Wait for the email element to be present.
                            wrapper = WebDriverWait(self.driver, delay).until(
                            EC.presence_of_element_located((By.ID, 'email'))
                            )
                            print("Email is present in the DOM now")
                            # Enter the email and password.
                            print("logging in..")
                            time.sleep(5) #change
                            login_email = self.driver.find_element(By.ID,'email')
                            login_email.clear()
                            login_email.send_keys(self.email)
                            password = self.driver.find_element(By.ID,'password')
                            password.clear()
                            password.send_keys(self.password)
                            password.send_keys(Keys.RETURN)  
                            print("logged in")
                            
                        wrapper = WebDriverWait(self.driver, delay).until(
                        EC.presence_of_element_located((By.ID, 'user-profile'))
                        )
                        time.sleep(5)
                        print("going to the accomodation page")
                        accomodation_page = self.driver.find_element(By.XPATH, "//a[@href='/accommodation']").click()
                        #print(accomodation_page)
                        
                        
                        #self.driver.get("https://studentportal.unilag.edu.ng/accommodation")
                        
                        print("getting the accomodation button")
                        accomodation_button = self.driver.find_element(By.XPATH, "//*[@class='bg-white rounded-md cursor-pointer h-full border-2 text-left p-6 transform duration-200 group hover:border-primary hover:scale-105 pb-2']")
                       # print(accomodation_button)
                        
                        print("clicking the button")
                        accomodation_button.click()
                        print("click successful") 
                        time.sleep(5)
                        
                        accomodation_ended = self.driver.find_element(By.XPATH, "//*[@class='text-sm mb-0']")
                        print(accomodation_ended.text)
                        
                        time.sleep(1) 
                                       
                    except TimeoutException:
                        print("Element did not show up, trying again...")
                        self.driver.refresh()
                        continue
                    else:
                        success = True
            except WebDriverException:
                print("Driver time out trying again...")
                continue
                # print(message_button)
            else:
                success = True

                
            print("End of Script")
     
   

     
        


                
                
                
                
                
                
                
        
        
if __name__ == '__main__':

    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = UnilagBallot(data)
    bot.login()

#encoding:utf-8
'''
Created on 2015年10月18日

@author: weiqinmeng
'''
from selenium import webdriver
import os
from macpath import pardir
      
class Tests():
    
    
    
#     def getDrvier(self):
#         self.driver = webdriver.Chrome(self.paths)
#         self.driver.get("http://www.baidu.com")
    
#     def getDriverPath(self):
#         
#         self.obPath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,os.pardir))
#         self.paths ='r' + '"' + os.path.join(self.obPath,'chromedriver.exe') + '"'
#         
#    
# #     def __init__(self):
# # #         self.driver = webdriver.Chrome(r"D:\jd\ObjectMobile\chromedriver.exe")
# #         self.driver = webdriver.Chrome(self.paths)
# #         self.driver.get("http://www.baidu.com")
           
    def __init__(self):
        
        self.driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.join(os.path.abspath('.'),os.pardir,os.pardir)),"chromedriver.exe"))
        self.driver.get("http://www.baidu.com")
        print "__init__"
           
    def maxi(self):
        driver = self.driver
        #浏览器最大化
#         driver.find_element_by_id('TANGRAM__PSP_4__userNameWrapper').clear()
#         driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('weimegn')
#         driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("java.1988")
#         driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
        
        print driver.title
        print driver.current_url



t = Tests()
# t.maxi()

# t.driver.quit()


# class JDTest():
#     global drivers
#     def __init__(self):
#         
#         self.drivers = webdriver.Chrome(r"D:\jd\ObjectMobile\chromedriver.exe")
#         self.drivers.get("http://m.jd.com")
#         
#         
#     def shouYe(self):
#         
#         self.drivers.find_element_by_id('index_search_submit').click()
#         num = self.drivers.find_elements_by_class_name("list-descriptions-wrapper")
# #         self.drivers.find_element_by_id("searchlist2559").find_elements(By.CLASS_NAME, "list-thumb")
#         lis = self.drivers.find_element_by_class_name("list_body").find_elements_by_class_name("list-thumb")
#         lis[0].click()
#          
#         time.sleep(4)
#         self.drivers.navigate.go_back(1)
#         self.drivers.maximize_window()
#         time.sleep(4)
#         self.drivers.navigate.go_forward(1)
#         time.sleep(4)
         
# t = JDTest() 
# t.shouYe()
# t.drivers.quit() 
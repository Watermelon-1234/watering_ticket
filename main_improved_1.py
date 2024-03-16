from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from selenium.webdriver.support.wait import WebDriverWait



def watering(i = 100000):
    # 建立 Edge 瀏覽器
    # i = int(input("how many times?"))
    # i = 100000
    try:
        driver = webdriver.Edge()
        WebDriverWait(driver,5)
        # 開啟 Google 表單
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3haC7-79blroBOJT5hY_9zRmZT13Qvgs8iMcKRjbIFaUIcg/viewform")
        WebDriverWait(driver,5)
        for j in range(i):
            print(j+1,"/",i);
            # 填寫表單
            driver.find_element(By.XPATH,'//*[@id="i36"]/div[2]').click()
            WebDriverWait(driver,5)
            driver.find_element(By.XPATH,'//*[@id="i69"]/div[2]').click()
            WebDriverWait(driver,5)
            # time.sleep(2)
            ##景美://*[@id="i69"]/div[2]
            # driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]').click()
            # WebDriverWait(driver,5)
            # driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]').click()
            # WebDriverWait(driver,5)

            # 提交表單
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()

            WebDriverWait(driver,5)
            driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()
            WebDriverWait(driver,5)
        # 關閉瀏覽器
        driver.quit()
    except Exception as e:
        driver.quit()
        print("error: " + str(e))
        watering(i-j+1)
        driver.quit()
        return False


i = int(input("how many times do you want to do?"))
watering(i)
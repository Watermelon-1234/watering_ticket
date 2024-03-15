from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from selenium.webdriver.support.wait import WebDriverWait

def watering(i = 100000):
    # 建立 Edge 瀏覽器
    # i = int(input("how many times?"))
    # i = 100000

    driver = webdriver.Edge()
    WebDriverWait(driver,5)
    # 開啟 Google 表單
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3haC7-79blroBOJT5hY_9zRmZT13Qvgs8iMcKRjbIFaUIcg/viewform")
    WebDriverWait(driver,5)
    for j in range(i):
        # 填寫表單
        driver.find_element(By.XPATH,'//*[@id="i36"]/div[2]').click()
        WebDriverWait(driver,5)
        driver.find_element(By.XPATH,'//*[@id="i69"]/div[2]').click()
        WebDriverWait(driver,5)
        ##景美://*[@id="i69"]/div[2]
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]').click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]').click()

        WebDriverWait(driver,5)

        # 提交表單
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()

        WebDriverWait(driver,5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()
        WebDriverWait(driver,5)
    # 關閉瀏覽器
    driver.quit()

def run_watering(num_threads,i):
    threads=[]
    for i in range(num_threads):
        thread = threading.Thread(target=watering,args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
i = int(input("how many times do you want to do?"))
j = int(input("how many threads?"))

run_watering(j,i)

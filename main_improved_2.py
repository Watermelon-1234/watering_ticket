from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from selenium.webdriver.support.wait import WebDriverWait



def watering(thread_name,error=-1,t=1):
    # 建立 Edge 瀏覽器
    # i = int(input("how many times?"))
    # i = 100000
    driver = webdriver.Edge()
    driver.set_window_size(500, 400)
    try:
        error+=1
        WebDriverWait(driver,5)
        # 開啟 Google 表單
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3haC7-79blroBOJT5hY_9zRmZT13Qvgs8iMcKRjbIFaUIcg/viewform")
        WebDriverWait(driver,5)
        while True:
            # print(t);
            print("Thread " + str(thread_name)+"=> error times: " + str(error)+" ,runned times: " + str(t))
            t+=1
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
        # driver.quit()
    except Exception as e:
        driver.quit()
        print("error: " + str(e))
        watering(thread_name,error,i)
        driver.quit()
        return False

def run_with_threads(num_threads):
    try:
        threads=[]
        for j in range(num_threads):
            thread = threading.Thread(target=watering,args=(j+1,))
            threads.append(thread)
            thread.start()
            time.sleep(0.5)
        for thread in threads:
            thread.join()
    except Exception as e:
        print("error :"+str(e))
        run_with_threads(num_threads)
        return False;




# i = int(input("how many times do you want to do?"))
j = int(input("how many threads do you want to use?"))
i = input("press enter to start and close terminal window to stop")
run_with_threads(j)
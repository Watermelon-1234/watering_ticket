from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from selenium.webdriver.support.wait import WebDriverWait



def watering(thread_name,error=-1,run_times=1):
    # 建立 Edge 瀏覽器
    # i = int(input("how many times?"))
    # i = 100000
    options = webdriver.EdgeOptions()
    options.add_argument("--window-size=500,400")
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-chrome-browser-cloud-management")
    driver = webdriver.Edge(options=options)
    # driver.set_window_size(500, 400)
    try:
        error+=1
        WebDriverWait(driver,10)
        # 開啟 Google 表單
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3haC7-79blroBOJT5hY_9zRmZT13Qvgs8iMcKRjbIFaUIcg/viewform")
        WebDriverWait(driver,10)
        while True:
            print(type(run_times));
            print("Thread " ,thread_name,"=> error times: ",error," ,runned times: " ,run_times)
            
            
            run_times+=1
            
            # 填寫表單
            driver.find_element(By.XPATH,'//*[@id="i36"]/div[2]').click()
            WebDriverWait(driver,10)
            driver.find_element(By.XPATH,'//*[@id="i69"]/div[2]').click()
            WebDriverWait(driver,10)
            # time.sleep(2)
            ##景美://*[@id="i69"]/div[2]
            # driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]').click()
            # WebDriverWait(driver,10)
            # driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]').click()
            # WebDriverWait(driver,10)

            # 提交表單
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()

            WebDriverWait(driver,10)
            driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()
            WebDriverWait(driver,10)
        # 關閉瀏覽器
        # driver.quit()
    except Exception as e:
        driver.quit()
        print("running error: " + str(e))
        watering(thread_name,error,run_times)
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
        print("threads error :"+str(e))
        run_with_threads(num_threads)
        return False;




# i = int(input("how many times do you want to do?"))
j = int(input("how many threads do you want to use?"))
i = input("press enter to start and close terminal window to stop")
run_with_threads(j)
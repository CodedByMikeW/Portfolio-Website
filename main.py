from flask import Flask, render_template, request
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime,timedelta
from time import sleep,time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
app = Flask(__name__)


@app.route("/")
def page():
    return render_template("index.html")

@app.route('/run-selenium', methods=['POST'])
def run_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    



    driver = webdriver.Chrome(options=chrome_options)



    driver.get('https://ozh.github.io/cookieclicker/')
    wait = WebDriverWait(driver, 15)
    # English = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".langSelectButton.title")))
    # English.click()
    cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    Game_on = True

    now = datetime.now()  # .strftime("%H:%M:%S")
    # current_time=now.minute
    future_time = (datetime.now() + timedelta(minutes=1))
    # .strftime("%H:%M:%S")

    print(f"This is Now Hour {now.hour}")
    print(f"This is Future Hour{future_time.hour}")
    print(f"This is Now Min {now.minute}")
    print(f"This is Future Min{future_time.minute}")
    print(f"This is Now Sec {now.second}")
    print(f"This is Future Sec{future_time.second}")
    print((type(now.hour)))

    wait_time = 15
    timeout = time() + wait_time  # Check for purchases every 5 seconds
    five_min = time() + 60 * 5  # Run for 5 minutes

    while Game_on:

        now = datetime.now()  # .strftime("%H:%M:%S")
        # current_time=now.minute
        future_time = datetime.now() + timedelta(minutes=2)
        # if no+w.hour == future_time.hour:
        print(f"{now.minute},{future_time.minute}")
        print(f"{now.second},{future_time.second}")
        if time() > timeout:
            print("Game Over")
            return render_template("cookie.html")
            #Game_on = False

        else:
            cookie.click()
        #

    # Setup Selenium
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get("https://www.google.com")
    # return "Selenium script has been executed!


if __name__ == "__main__":
    app.run(debug=True)
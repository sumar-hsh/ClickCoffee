from flask import Flask, render_template, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


app = Flask(__name__)

# Setup WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment to run in headless mode
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://erp.fibbee.com/dashboard/view/01GQPPS4DBRJ9VXYZPJZXJRQ65/dashboard.html")

# If the button is inside an iframe, switch to the iframe first
# driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))



def perform_action(action):
#     driver.get("https://erp.fibbee.com/dashboard/view/01GQPPS4DBRJ9VXYZPJZXJRQ65/dashboard.html")
    # if action == "QuickWash":
    #     button = driver.find_element(By.ID, "quick_wash_button_id")  # Use correct button ID
    #     button.click()
    # elif action == "BigWash":
    #     button = driver.find_element(By.ID, "big_wash_button_id")
    #     button.click()
    if action == "Restart":
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[4]/div[1]/div[1]/button[1]"))
        )
        button.click()

@app.route('/')
def home():
    return render_template('index.html')
#
# @app.route('/quickwash')
# def quickwash():
#     perform_action("QuickWash")
#     return redirect(url_for('home'))
#
# @app.route('/bigwash')
# def bigwash():
#     perform_action("BigWash")
#     return redirect(url_for('home'))
#
@app.route('/restart')
def restart():
    perform_action("Restart")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

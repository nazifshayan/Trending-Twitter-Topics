from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = 'nazifshayan22@gmail.com'
password = '9422973992N'
x_id = '@NazifShaya17158'


def main_script():

    driver = webdriver.Chrome()

    driver.get('https://twitter.com/login')

    time.sleep(2)

    username_field = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                                                         "div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]"
                                                         "/div/input")

    username_field.send_keys(username)

    user_button = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                                                      "div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
    user_button.click()

    time.sleep(2)

    twitter_id = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                                                     "div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div"
                                                     "/input")

    twitter_id.send_keys(x_id)

    id_button = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]"
                                                    "/div/div/div[2]/div[2]/div[2]/div/div/div/button")
    id_button.click()

    time.sleep(2)

    twitter_password = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]"
                                                           "/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label"
                                                           "/div/div[2]/div[1]/input")
    twitter_password.send_keys(password)

    password_button = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]"
                                                          "/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
    password_button.click()
    # password_field.send_keys(Keys.RETURN)

    time.sleep(3)

    try:
        trending_section = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div'
                                                         '[2]/div/div/div/div[4]/div/section')
        trending_topics = trending_section.find_elements(By.CLASS_NAME, 'css-175oi2r')[:5]

        # Extract and print the top 5 trending topics
        for i, topic in enumerate(trending_topics, start=1):
            title = topic.find_element(By.XPATH, './/span').text
            print(f"Trending {i}: {title}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(driver.title)

    driver.quit()

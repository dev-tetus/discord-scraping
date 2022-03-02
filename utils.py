from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from clash_data import ClashData


def get_server_names():
    return [
        ('Clash of Clans Français 🇫🇷'),
        ('Clash Community'),
        ('La Souce Family')
    ]


def find_servers(driver, server_names):
    servers_to_send = [()]
    servers_availables = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@role='treeitem']")))

    for server_clickable in servers_availables:
        if server_clickable.get_attribute("aria-label").strip() in server_names:
            servers_to_send.append(server_clickable.get_attribute("aria-label").strip(),server_clickable)
    return servers_to_send

def send_message(driver, text):
    action = webdriver.ActionChains(driver)
    input_box = driver.find_element(by=By.CSS_SELECTOR, value=r'#app-mount > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div > div > div > div.chat-2ZfjoI > div.content-1jQy2l > main > form > div > div > div > div.scrollableContainer-15eg7h.webkit-QgSAqd > div > div.textArea-2CLwUE.textAreaSlate-9-y-k2.slateContainer-3x9zil > div > div > span > span > span')
    action.send_keys_to_element(input_box, text).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


def get_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    ser = Service(executable_path="./msedgedriver.exe")
    return webdriver.Edge(service=ser, options=options)

def do_login(driver):
    driver.find_element(by=By.NAME, value='email').send_keys(get_credentials()['username'])
    driver.find_element(by=By.NAME, value='password').send_keys(get_credentials()['password'])
    for element in driver.find_elements(By.TAG_NAME, "button"):
        if element.text == "Iniciar sesión":
            button = element
    webdriver.ActionChains(driver).click_and_hold(button).perform()
    webdriver.ActionChains(driver).release().perform()





def get_text_with_data():
    cd = ClashData()
    with open("text.txt","r", encoding='UTF-8') as f2:
        return f2.read()\
            .replace(r'{date}',datetime.now()\
            .strftime("%d/%m/%Y"))\
            .replace(r'{clan_members}',str(cd.members))\
        

#Debug
if __name__ == '__main__':
    print(get_text_with_data())
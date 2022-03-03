from datetime import datetime
from os import path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

import utils


if __name__ == '__main__':

    url = "https://www.discord.com/login"
    servers = utils.get_server_names()

    driver=utils.get_driver()
    print(driver)
    driver.quit()
    
    driver.maximize_window()
    driver.get("https://www.discord.com/login")
    
    utils.do_login(driver)
    sleep(2)
    servers_to_access = utils.find_servers(driver,servers)
    # print(servers_to_access)

    for server in servers_to_access:
        if 'https://discord.com/login' in driver.current_url:
            utils.do_login_(driver)
                    #driver.execute_script(f'alert(\'{server[1]}\');')
        sleep(2)
                    #driver.switch_to.alert.accept()
        if server[0] == 'La Souce Family':
            utils.press_server(driver, server[1])
            driver.execute_script(f'alert("Hola mi bombon de melocotón");')
            sleep(2)
            driver.switch_to.alert.accept()

    
    driver.quit()




    
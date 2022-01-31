import time
from selenium import webdriver
from selenium.webdriver.common.by import By

capabilities = {
    "browserName": "chrome",
    "browserVersion": "97.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False,
    }
}
driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
driver.set_window_size(1920, 1080)

try:
    driver.get("https://dev.invest-ra.ru/")
    time.sleep(2)

    logon_button = driver.find_element(By.CLASS_NAME, 'mat-focus-indicator')
    logon_button.click()
    time.sleep(2)

    email = driver.find_element(By.ID, 'email')
    email.send_keys("stuffy.user.0101@gmail.com")
    time.sleep(2)

    password = driver.find_element(By.ID, 'pass')
    password.send_keys("TUnke3RW4gm4YM8")
    time.sleep(2)

    enter_button = driver.find_element(By.ID, 'btn-entrance')
    enter_button.click()
    time.sleep(2)

    calculator_button = driver.find_element(By.CSS_SELECTOR, 'div.nav > a:nth-child(4)')
    calculator_button.click()
    time.sleep(2)

    goals_button = driver.find_element(By.CSS_SELECTOR, 'div.card-list > a')
    goals_button.click()
    time.sleep(2)

    goals = driver.find_elements(By.CSS_SELECTOR, 'div.horizontal-scroll-wrapper tr.mat-row')
    diagram = driver.find_elements(By.CSS_SELECTOR, 'g.highcharts-data-labels g.highcharts-label')

    mons_invest = driver.find_element(By.CSS_SELECTOR, 'div.mat-tab-labels > div.mat-ripple:nth-child(2)')
    mons_invest.click()
    time.sleep(2)

    invests = driver.find_elements(By.CSS_SELECTOR, 'div.horizontal-scroll-wrapper tr.ng-star-inserted')

    all_goals = driver.find_element(By.CSS_SELECTOR, 'div.mat-tab-labels > div.mat-ripple:nth-child(1)')
    all_goals.click()
    time.sleep(2)

    add_goal = driver.find_element(By.CSS_SELECTOR, 'button.mat-primary')
    add_goal.click()
    time.sleep(2)

    input_goal = driver.find_element(By.CSS_SELECTOR, 'div.mat-form-field-infix > input')
    input_goal.clear()
    input_goal.send_keys("Test123")
    time.sleep(2)

    save_button = driver.find_element(By.CSS_SELECTOR, 'mat-dialog-actions > button.mat-focus-indicator')
    save_button.click()
    time.sleep(2)

    new_goals = driver.find_elements(By.CSS_SELECTOR, 'div.horizontal-scroll-wrapper tr.mat-row')
    assert len(new_goals) - len(goals) == 1, 'Цель не добавлена'

    new_diagram = driver.find_elements(By.CSS_SELECTOR, 'g.highcharts-data-labels g.highcharts-label')
    assert len(new_diagram) - len(diagram) == 1, 'Цель не добавлена на диаграмму'

    mons_invest.click()
    new_invests = driver.find_elements(By.CSS_SELECTOR, 'div.horizontal-scroll-wrapper tr.ng-star-inserted')
    assert len(new_invests) > len(invests), 'Цель не добавлена в Ежемесячные инвестиции'


finally:
    driver.quit()
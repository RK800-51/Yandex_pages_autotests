import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # Возвращает экземпляр драйвера браузера Chrome перед прохождением теста, после прохождения теста закрывает браузер.

    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Описывает базовый объект веб-страницы

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://ya.ru/'

    def find_element(self, locator, time=10):
        # Ожидает прогрузки страницы, ищет элемент по заданному локатору и возвращает, если тот был найден.
        # Выбрасывает ошибку с message, если элемент найден не был.

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        # Дает команду драйверу перейти на выбранный URL.

        return self.driver.get(self.base_url)

    def switch_window(self):
        # Дает команду драйверу переключиться на последнюю открытую страницу. Возвращает URL текущей страницы.

        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.driver.current_url



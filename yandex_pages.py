import json

from base_page import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    # Описывает локаторы для поиска элементов в DOM.

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, 'search3__button')
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, "div.services-more-popup__item-title")
    LOCATOR_YANDEX_NAVIGATION_BAR_ALL = (By.CSS_SELECTOR, "a[href='https://yandex.ru/all']")
    LOCATOR_YANDEX_SUGGEST_LIST = (By.CLASS_NAME, 'mini-suggest__popup-content')
    LOCATOR_YANDEX_SEARCH_RESULT_TITLE = (By.CSS_SELECTOR, 'title')
    LOCATOR_YANDEX_FIRST_RESULT_LINK = (By.CSS_SELECTOR, "li.serp-item[data-cid='0'] button")
    LOCATOR_YANDEX_NAVIGATION_PICTURES = (By.CSS_SELECTOR, "a[aria-label='Картинки']")
    LOCATOR_YANDEX_PICTURES_PAGE = (By.TAG_NAME, 'title')
    LOCATOR_YANDEX_PICTURES_PAGE_FIRST_CATEGORY = (By.CLASS_NAME, 'PopularRequestList-Item_pos_0')
    LOCATOR_YANDEX_PICTURES_CATEGORY_SEARCH_INPUT = (By.CSS_SELECTOR, 'input.input__control')
    LOCATOR_YANDEX_FIRST_FOUND_PICTURE = (By.CLASS_NAME, 'serp-item_pos_0')
    LOCATOR_YANDEX_OPENED_PICTURE = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    LOCATOR_YANDEX_NEXT_BUTTON = (By.CLASS_NAME, 'CircleButton_type_next')
    LOCATOR_YANDEX_PREV_BUTTON = (By.CLASS_NAME, 'CircleButton_type_prev')


class SearchHelper(BasePage):
    # Описывает методы для тестовых сценариев.

    def check_result_title(self):
        # Проверяет наличие и выбирает веб-элемент с тэгом 'title'.

        title = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT_TITLE, time=2)
        return title.get_attribute('innerText')

    def find_suggest_list(self):
        # Проверяет, что на странице появилась таблица с подсказками.

        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)

    def find_first_result_link(self):
        # Проверяет наличие и возвращает первую ссылку первого результата поиска.

        first_result = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_RESULT_LINK, time=2)
        data = first_result.get_property('dataset')['vnl']
        return data

    def click_search_field(self):
        # Ищет поле поиска и делает клик по нему.

        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        return search_field

    def enter_word(self, word):
        # Ищет поле поиска, делает клик по нему и вводит строку из тестового сценария.

        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        # Ищет и нажимает на кнопку "Найти".

        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def click_navigation_bar_and_choose_images(self):
        # Проверяет наличие кнопки "Все сервисы", нажимает на нее, находит пункт "Картинки", нажимает на него.

        menu_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR_ALL, time=2)
        menu_button.click()
        pictures_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_PICTURES, time=2)
        pictures_button.click()
        current_url = self.switch_window()
        return current_url

    def choose_first_image_category_and_search(self):
        # Ищет первую категорию на Яндекс картинках, открывает ее, ищет поле поиска на новой странице и проверяет,
        # проставлена ли в поле выбранная категория автоматически.

        request = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PICTURES_PAGE_FIRST_CATEGORY, time=2)
        auto_input = request.get_attribute('outerText')
        request.click()
        self.switch_window()
        input_value = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PICTURES_CATEGORY_SEARCH_INPUT, time=2).\
            get_attribute('value')
        return auto_input, input_value

    def open_first_image_and_get_its_url(self):
        # Ищет элемент первой найденной картинки, нажимает на нее, проверяет наличие элемента открытой в центре картинки,
        # возвращает сгенерированный сайтом уникальный URL для картинки из обоих элементов.

        first_image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_FOUND_PICTURE, time=2)
        first_image.click()
        first_picture_url = json.loads(first_image.get_property('attributes')[1]['nodeValue'])['serp-item']['preview'][0]['url']
        opened_picture_url = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_OPENED_PICTURE, time=2).get_property('attributes')[1]['nodeValue']
        return first_picture_url, opened_picture_url

    def click_next_image_btn(self):
        # Находит и нажимает на кнопку "Следующая картинка", возвращает сгенерированный URL новой картинки.

        next_btn = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_BUTTON, time=2)
        next_btn.click()
        next_image_url = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_OPENED_PICTURE, time=2).get_property('attributes')[1]['nodeValue']
        return next_image_url

    def click_prev_image_btn(self):
        # Находит и нажимает на кнопку "Предыдущая картинка", возвращает сгенерированный URL старой картинки.

        prev_btn = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PREV_BUTTON, time=2)
        prev_btn.click()
        prev_image_url = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_OPENED_PICTURE, time=2).get_property('attributes')[1]['nodeValue']
        return prev_image_url










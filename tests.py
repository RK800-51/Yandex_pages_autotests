from yandex_pages import SearchHelper


def test_yandex_search(browser):
    # Сценарий - поиск в Яндексе:
    # 1) Зайти на https://ya.ru/
    # 2) Проверить наличия поля поиска
    # 3) Ввести в поиск 'Тензор'
    # 4) Проверить, что появилась таблица с подсказками(suggest)
    # 5) Нажать enter
    # 6) Проверить, что появилась страница результатов поиска
    # 7) Проверить 1 ссылка ведет на сайт tensor.ru

    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word('Тензор')
    yandex_main_page.find_suggest_list()
    yandex_main_page.click_on_the_search_button()
    title = yandex_main_page.check_result_title()
    assert 'Тензор — Яндекс' in title, 'Search page did not load successfully'
    href = yandex_main_page.find_first_result_link()
    assert 'https://tensor.ru/' in href, 'First search result URL is not https://tensor.ru/'


def test_yandex_images(browser):
    # Сценарий - картинки на Яндексе:
    # 1) Зайти на ya.ru
    # 2) Проверить, что кнопка меню присутствует на странице
    # 3) Открыть меню, выбрать “Картинки”
    # 4) Проверить, что перешли на url https://yandex.ru/images/
    # 5) Открыть первую категорию
    # 6) Проверить, что название категории отображается в поле поиска
    # 7) Открыть 1 картинку
    # 8) Проверить, что картинка открылась
    # 9) Нажать кнопку вперед
    # 10) Проверить, что картинка сменилась
    # 11) Нажать назад
    # 12) Проверить, что картинка осталась из шага 8

    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_search_field()
    current_url = yandex_main_page.click_navigation_bar_and_choose_images()  # Кнопка "меню" заменена на "все сервисы"
    assert current_url == 'https://yandex.ru/images/', 'Wrong Yandex Images page URL'
    first_category, input_value = yandex_main_page.choose_first_image_category_and_search()
    assert first_category == input_value, 'Search field does not contain chosen category'
    origin_image, opened_image = yandex_main_page.open_first_image_and_get_its_url()
    assert origin_image == opened_image, 'Opened image is not the selected one'
    opened_image = yandex_main_page.click_next_image_btn()
    assert not origin_image == opened_image, 'Image did not change'
    opened_image = yandex_main_page.click_prev_image_btn()
    assert origin_image == opened_image, 'Current image is not previous one'

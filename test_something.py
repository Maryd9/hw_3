from selene import browser, be, have


def test_search_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests '
                                                                         'in Python'))


def test_search_duckduckgo():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="OrganicTextContentSpan"]').should(have.text('Selene - User-oriented Web UI browser tests '
                                                                         'in Python').not_)


def test_search_yandex():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="OrganicTextContentSpan"]').should(have.text('can be built either in a simple '
                                                                         'straightforward "selenide"'))


def test_search_no_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('65745gghhhhhh').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу 65745gghhhhhh ничего не найдено.'))
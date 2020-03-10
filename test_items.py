link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_basket_present(browser):
    browser.get(link)
    assert browser.find_element_by_xpath("//button[@type='submit' \
                                         and \
                                                   @class='btn btn-lg btn-primary btn-add-to-basket']")

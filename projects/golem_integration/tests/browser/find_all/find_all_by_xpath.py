from golem import actions


description = 'Verify that the webdriver.find_all method can find all web elements by xpath'


def test(data):
    actions.navigate(data.env.url+'elements/')
    selector = '//input[@type="checkbox"]'
    checkboxes = actions.get_browser().find_all(xpath=selector)
    assert len(checkboxes) == 2


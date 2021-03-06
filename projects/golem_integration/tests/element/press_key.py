from golem import actions


description = 'Verify webelement.press_key method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#input-one')
    element.press_key('NUMPAD2')
    actions.verify_element_text('#input-one-input-result', 'Welcome 2')
    try:
        element = actions.get_browser().find('#input-one')
        element.press_key('UNDEFINED_KEY')
    except Exception as e:
        assert 'Key UNDEFINED_KEY is invalid' in e.args[0]
    else:
        raise AssertionError('expected an exception')
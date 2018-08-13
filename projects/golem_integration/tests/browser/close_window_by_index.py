from golem import actions


description = 'Verify webdriver.close_window_by_index method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    first_title = actions.get_window_title()
    actions.switch_to_window_by_index(1)
    second_title = actions.get_window_title()
    actions.switch_to_window_by_index(0)
    # close third window by index
    actions.get_browser().close_window_by_index(2)
    actions.verify_amount_of_windows(2)
    actions.verify_title(first_title)
    # close first window by index, from the first window
    actions.get_browser().close_window_by_index(0)
    actions.verify_amount_of_windows(1)
    # second window is now index 0
    actions.verify_title(second_title)

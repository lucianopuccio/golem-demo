from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_page_not_contains_text action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    text = '<button id="button-six"'
    actions.wait_for_page_not_contains_text(text, timeout=5)
    golem_steps.assert_last_step_message("Wait for page to not contain text '{}'".format(text))
    # wait times out waiting for text to be present in page
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for page to not contain '<button id=\"button-six\"'"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_page_not_contains_text('<button id="button-six"', timeout=3)

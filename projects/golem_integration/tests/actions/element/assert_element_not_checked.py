from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_not_checked action'


def test_assert_element_not_checked(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_not_checked('#unselected-checkbox')
    golem_steps.assert_last_step_message('Assert element #unselected-checkbox is not checked')
    with expected_exception(AssertionError, 'element #selected-checkbox is checked'):
        actions.assert_element_not_checked('#selected-checkbox')

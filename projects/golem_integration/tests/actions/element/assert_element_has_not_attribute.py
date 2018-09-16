from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_has_not_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_has_not_attribute('#button-one', 'not-this-one')
    golem_steps.assert_last_step_message('Assert element #button-one has not attribute not-this-one')
    try:
        actions.assert_element_has_attribute('#button-one', 'onclick')
    except AssertionError as e:
        assert 'element #button-one has attribute onclick' in e.args[0]

from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify select_option_by_value action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    select = ('id', 'select-1')
    actions.select_option_by_value(select, 'option-saab')
    actions.verify_selected_option(select, 'Saab')
    golem_steps.assert_last_step_message('Verify selected option value of element #select-1 is option-saab')

from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_cookie_value'

def test(data):
    actions.navigate(data.env.url)
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.assert_cookie_value('foo', 'bar')
    assert golem_steps.get_last_step_message() == "Assert that cookie 'foo' value is 'bar'"
    try:
        actions.assert_cookie_value('foo', 'incorrect')
    except AssertionError as e:
        assert "expected cookie 'foo' value to be 'incorrect' but was 'bar'" in e.args[0]

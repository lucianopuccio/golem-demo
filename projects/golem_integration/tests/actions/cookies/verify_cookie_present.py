from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_cookie_present action'


def test_verify_cookie_present(data):
    actions.navigate(data.env.url)
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.verify_cookie_present('foo')
    golem_steps.assert_last_step_message("Verify that cookie 'foo' exists")
    actions.verify_cookie_present('baz')
    golem_steps.assert_last_error("Cookie 'baz' was not found")

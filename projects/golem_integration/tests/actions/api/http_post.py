from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify http_post action'

def test(data):
    elements_url = data.env.url + 'elements/'
    response = actions.http_post(elements_url)
    golem_steps.assert_last_step_message('Make a POST request to {}'.format(elements_url))
    assert response == data.last_response
    assert response.status_code == 200

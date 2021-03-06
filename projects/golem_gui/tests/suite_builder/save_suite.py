from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder

description = 'Verify the user can make changes to a suite and save it successfully'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_builder')
    api.suite.create_access_suite(data.project)


def test(data):
    actions.clear_element(suite_builder.processes_input)
    actions.send_keys(suite_builder.processes_input, 3)
    suite_builder.save_suite()
    actions.refresh_page()
    suite_builder.assert_processes_value(3)

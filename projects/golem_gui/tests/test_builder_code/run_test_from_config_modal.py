from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder_code
from projects.golem_gui.pages import test_run_modal
from projects.golem_gui.pages import test_run_config_modal


description = 'Verify the user can run a test from the config modal'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')
    api.test.create_access_test_code(data.project)


def test(data):
    actions.click(test_builder_code.run_config_button)
    actions.wait_for_element_displayed(test_run_config_modal.config_modal)
    actions.click(test_run_config_modal.run_button)
    test_run_modal.assert_result('success')

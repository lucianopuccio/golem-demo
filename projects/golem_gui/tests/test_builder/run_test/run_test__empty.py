from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_modal


description = 'Verify the user can run an empty test'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_run')
    data.test = api.test.create_access_test(data.project)


def test(data):
    actions.click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result_log_line(0, 'Test execution started: {}'.format(data.test))
    test_run_modal.assert_result_log_line(1, 'INFO Browser: chrome')
    test_run_modal.assert_result_log_line(2, 'INFO Test started: test')
    test_run_modal.assert_result_log_line(3, 'INFO Test Result: SUCCESS')
    test_run_modal.assert_result('success')
    test_run_modal.assert_result_errors([])
    test_run_modal.assert_result_steps_is_empty()

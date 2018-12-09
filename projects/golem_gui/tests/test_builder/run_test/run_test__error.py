
description = 'Verify the user can run a test with an error'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_' + random('dddd'))
    test_list.create_access_test(data.test_name)

def test(data):
    test_builder.add_action('error', params=["'error message'"])
    click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result_log_line(0, 'Test execution started: {}'.format(data.test_name))
    test_run_modal.assert_result_log_line(1, 'INFO Browser: chrome')
    test_run_modal.assert_result_log_line(2, 'ERROR error message')
    test_run_modal.assert_result_log_line(3, 'INFO Test Result: ERROR')
    test_run_modal.assert_result('error')
    test_run_modal.assert_result_errors(['error message'])
    test_run_modal.assert_result_steps(['ERROR - error message'])

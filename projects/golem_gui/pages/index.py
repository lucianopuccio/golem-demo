from selenium.common.exceptions import TimeoutException
from golem import actions
from golem.browser import elements, get_browser

from projects.golem_gui.pages import common


create_project_button = ('css', "#projectCreationButton button", 'Create Project button')
title = ('css', "#content h3", 'Title')
project_name_input = ('id', "newProjectName", 'Project Name input')
create_button = ('id', "createProjectCreate", 'Create button')
cancel_create_button = ('id', "createProjectCancel", 'Cancel button')
project_list_item = ('css', '#projectList>a')


def project_is_present(project_name):
    items = elements(project_list_item)
    project_names = [x.text for x in items]
    return project_name in project_names


def access_project(project_name):
    actions.step('Access project {}'.format(project_name))
    items = elements(project_list_item)
    for item in items:
        if item.text == project_name:
            item.click()
            return
    raise Exception('Project {} not found'.format(project_name))


def create_project(project_name, ignore_exists=False):
    actions.click(create_project_button)
    actions.wait_for_element_displayed(project_name_input)
    actions.send_keys(project_name_input, project_name)
    try:
        actions.click(create_button)
        actions.wait_for_element_displayed(create_project_button, 2)
    except TimeoutException as e:
        if ignore_exists:
            if common.error_modal_is_displayed():
                get_browser().refresh()
                return
        else:
            raise e


def create_access_project(project_name):
    if not project_is_present(project_name):
        create_project(project_name, ignore_exists=True)
    access_project(project_name)
    actions.get_data().project = project_name

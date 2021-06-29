from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_list')
    common.navigate_menu('Suites')
    data.folder = actions.random_str()
    suite_list.add_folder(data.folder)


def test(data):
    suite_list.delete_folder(data.folder)
    assert not suite_list.folder_exists(data.folder)
    actions.refresh_page()
    assert not suite_list.folder_exists(data.folder)

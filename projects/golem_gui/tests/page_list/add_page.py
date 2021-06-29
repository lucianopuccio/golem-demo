from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can create a new page from the project page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    common.navigate_menu('Pages')


def test_add_page(data):
    # to root
    page_one = actions.random_str()
    page_list.add_page(page_one)
    assert page_list.page_exists(page_one)

    # to folder
    page_two = 'folder1.' + actions.random_str()
    page_list.add_page(page_two)
    assert page_list.page_exists(page_two)

    actions.refresh_page()
    assert page_list.page_exists(page_one)
    assert page_list.page_exists(page_two)

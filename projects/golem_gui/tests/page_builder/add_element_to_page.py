from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import page_builder


description = 'Verify the user can add an element to a page and save it successfully'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_builder')
    api.page.create_access_page(data.project)


def test(data):
    element_def = ['some_element', 'id', 'selector_value', 'display_name']
    page_builder.add_element(element_def)
    page_builder.save_page()
    actions.refresh_page()
    page_builder.assert_element_exists(element_def)

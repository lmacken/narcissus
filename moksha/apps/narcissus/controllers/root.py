from tg import expose, validate, tmpl_context, redirect
from moksha.lib.base import Controller

from moksha.apps.narcissus.decorators import (
    with_moksha_socket,
    with_ui_theme,
    with_menu
)

import docutils.examples

import moksha.utils

import logging
log = logging.getLogger(__name__)


def readme_as_html():
    """ Ridiculous """
    root = '/'.join(__file__.split('/')[:-4])
    fname = root + '/README.rst'
    with open(fname, 'r') as f:
        readme = f.read()
        readme = readme.split('.. split here')[1]
        return docutils.examples.html_body(unicode(readme))

class NarcissusController(Controller):

    @expose()
    def index(self, *args, **kw):
        redirect('/map')

    @expose('mako:moksha.apps.narcissus.templates.widget')
    @with_moksha_socket
    @with_menu
    @with_ui_theme
    def plot(self, *args, **kw):
        tmpl_context.widget = moksha.utils.get_widget('narc_plot')
        return dict(options={})

    @expose('mako:moksha.apps.narcissus.templates.widget')
    @with_moksha_socket
    @with_menu
    @with_ui_theme
    def map(self, *args, **kw):
        tmpl_context.widget = moksha.utils.get_widget('narc_map')
        return dict(options={})

    @expose('mako:moksha.apps.narcissus.templates.widget')
    @with_moksha_socket
    @with_menu
    @with_ui_theme
    def logs(self, *args, **kw):
        tmpl_context.widget = moksha.utils.get_widget('narc_logs')
        return dict(options={})

    @expose('mako:moksha.apps.narcissus.templates.about')
    @with_moksha_socket
    @with_menu
    @with_ui_theme
    def about(self, *args, **kw):
        tmpl_context.readme = readme_as_html()
        return dict(option={})

__author__ = 'ravenoak'

from docutils.parsers import rst
from docutils.core import publish_parts
from docutils.writers import html4css1

writer = html4css1.Writer()
inliner = rst.states.Inliner()
parser = rst.Parser(inliner=inliner)

def render(content):
    parts = publish_parts(content, writer=writer, parser=parser)
    return parts


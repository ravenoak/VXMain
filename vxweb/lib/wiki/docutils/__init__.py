__author__ = 'ravenoak'

from docutils.parsers import rst
from docutils.core import publish_parts


inliner = rst.states.Inliner()
parser = rst.Parser(inliner=inliner)


def render(content):
    parts = publish_parts(content, writer=writer, parser=parser)
    return parts

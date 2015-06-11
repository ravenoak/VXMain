"""
Markdown module
"""
__author__ = 'ravenoak'

from markdown.inlinepatterns import Pattern
from markdown.util import etree
#from vxmain.model.primitives import Image

class ImagePattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('img')

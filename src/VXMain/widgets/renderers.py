'''
Created on Jul 12, 2012

@author: ravenoak
'''

from tw.api import Link
from markdown import markdown
from genshi.core import Markup
import re


class IconLink(Link):
    """
    A link to an icon.
    """
    template = """<img src="$link" alt="$alt" />"""

    params = dict(alt="Alternative text when not displaying the image")

    def __init__(self, *args, **kw):
        super(IconLink, self).__init__(*args, **kw)
        self.alt = kw.get('alt')


def insertResource(text):
    """
    Do a regex?
    """
    resourcePattern = re.compile(r'[?P<resource>(.*):(?P<label>.*)]')
    #resourcePattern.
    
    return text


def bodyMarkup(text):
    """
    Render the encoded body text as HTML
    """
    return Markup(insertResource(markdown(text, output_format='xhtml5')))





#class RenderBodyMarkup(Markup):
#    """
#    Render the encoded body text as HTML
#    """
#    
#    @classmethod
#    def render(cls, text):
#        markdown = Markdown()
#        return cls(markdown.convert(text))

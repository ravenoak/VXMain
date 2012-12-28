'''
Created on Oct 23, 2012

@author: ravenoak
'''

from tw2.core import Link
from markdown import markdown
from genshi.core import Markup as GenshiMarkup
import re

class Markup(object):
    """
    """
    
    def __init__(self):
        pass
    
    def insertResource(self, text):
        """
        Do a regex?
        """
        resourcePattern = re.compile(r'[?P<resource>(.*):(?P<label>.*)]')
        #resourcePattern.
        return text
    
    def render(self, text, output_format='xhtml5'):
        """
        """
        #return GenshiMarkup(text)
        return GenshiMarkup(markdown(text, output_format='xhtml5'))
        #return GenshiMarkup(self.insertResource(markdown(text, output_format='xhtml5')))
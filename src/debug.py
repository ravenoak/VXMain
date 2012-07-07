'''
Created on Jul 21, 2011

@author: ravenoak
'''

from paste.script.serve import ServeCommand
ServeCommand("serve").run(["src/development.ini"])

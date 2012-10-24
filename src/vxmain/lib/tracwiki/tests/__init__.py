import doctest
import unittest

import vxmain.lib.tracwiki.api
import vxmain.lib.tracwiki.formatter
import vxmain.lib.tracwiki.parser
from vxmain.lib.tracwiki.tests import formatter, macros, model, wikisyntax
from vxmain.lib.tracwiki.tests.functional import functionalSuite

def suite():

    suite = unittest.TestSuite()
    suite.addTest(formatter.suite())
    suite.addTest(macros.suite())
    suite.addTest(model.suite())
    suite.addTest(wikisyntax.suite())
    suite.addTest(doctest.DocTestSuite(vxmain.lib.tracwiki.api))
    suite.addTest(doctest.DocTestSuite(vxmain.lib.tracwiki.formatter))
    suite.addTest(doctest.DocTestSuite(vxmain.lib.tracwiki.parser))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')

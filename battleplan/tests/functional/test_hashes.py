from battleplan.tests import *

class TestHashesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='hashes', action='index'))
        # Test response...

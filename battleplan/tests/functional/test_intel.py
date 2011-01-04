from battleplan.tests import *

class TestIntelController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='intel', action='index'))
        # Test response...

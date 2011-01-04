from battleplan.tests import *

class TestTravelController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='travel', action='index'))
        # Test response...

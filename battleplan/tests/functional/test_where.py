from battleplan.tests import *

class TestWhereController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='where', action='index'))
        # Test response...

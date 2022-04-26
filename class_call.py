from error_handling import Thing


class This:

    def __init__(self):
        pass

    def show_thing(self):
        thing = self.test_data['thing']()
        thing.does()

    @classmethod
    def setUpClass(cls):
        cls.test_data = {
            'thing': Thing
        }


this = This()

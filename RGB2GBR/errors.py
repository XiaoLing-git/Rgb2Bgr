

class Rgb2BgrException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

    def __repr__(self):
        return self._msg
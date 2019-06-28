import imp

from check50 import *

class Similarities(Checks):

    @check()
    def exists(self):
        """helpers.py exists"""
        self.require("hello.py")

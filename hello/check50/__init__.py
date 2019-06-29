import imp

from check50 import *

class Similarities(Checks):

    @check()
    def exists(self):
        """hello.py exists"""
        self.require("hello.py")
        
    @check("compiles")
    def hello(self):
        """prints "Hello world!" """
        self.spawn("python3 ./hello.py").stdout("Hello world!", "Hello world!")

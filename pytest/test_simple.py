import pytest

# Simple
def sum (x, y):
        return x + y

def test_sum():
        assert sum(1,3) == 4

# Class
class TestClass(object):
	def test_1 (self):
		assert 'h' in 'hello'
	def test_2 (self):
		assert hasattr('hello', 'upper')





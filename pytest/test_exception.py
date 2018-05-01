import pytest

# Exception 
def raise_exception():
	raise Exception()

def test_raise():
	with pytest.raises(Exception):
		raise_exception()

# Exception - test message
def raise_exception():
	raise Exception('test!')

def test_raise_match():
	with pytest.raises(Exception, match=r'.*test!.*'):
		raise_exception()

def test_raise_assert():
	with pytest.raises(Exception) as exc:
		raise_exception()
	assert 'test!' in str(exc.value)
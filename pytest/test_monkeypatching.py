import pytest
import os.path

# Use monkeypatch fixture to set/del attr, item etc.
# To see available fixtures: pytest --fixtures 
def call_expanduser(path):
	return os.path.expanduser(path)

def test_monkey(monkeypatch):
	def mock(path):
		assert path == 'test'
		return 'monkeyed!'
	monkeypatch.setattr(os.path, 'expanduser', mock)
	output = call_expanduser('test')
	assert output == 'monkeyed!'
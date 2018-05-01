import pytest

# Fixture
x = 0
@pytest.fixture
def i_am_fixture():
	global x
	x += 1
	return x

def test_fixture(i_am_fixture):
	assert i_am_fixture == 1
def test_fixture2(i_am_fixture):
	assert i_am_fixture == 2

# Fixture - conftest.py
def test_fxiture_conftest(conftest_fixture):
	assert conftest_fixture == 'conftest_fixture'

# Fixture - one run per module 
@pytest.fixture(scope='module')
def fixture_once_per_module():
	global x
	x += 1
	return x

def test_fixture_run_count(fixture_once_per_module):
	assert fixture_once_per_module == 3
def test_fixture_run_count2(fixture_once_per_module):
	assert fixture_once_per_module == 3

#Fixture - one run per class test
@pytest.fixture(scope='class')
def fixture_once_per_class():
	global x
	x += 1
	return x

@pytest.mark.usefixtures('fixture_once_per_class')
class TestFixtureClass1(object):
	@pytest.mark.skip
	def test_fixture_class_scope(self):
		assert self.fixture_once_per_class == 4
	@pytest.mark.skip
	def test_fixture_class_scope2(self):
		assert fixture_once_per_class == 4
@pytest.mark.skip
class TestFixtureClass2(object):
	def test_fixture_class_scope3(self):
		assert fixture_once_per_class == 5

# Fixture - cleanup
# Run pytest -q -s --tb=no
@pytest.fixture
def i_cleanup():
	yield 'before cleanup'
	print('cleaned up!')

def test_fixture_cleanup(i_cleanup):
	assert i_cleanup == 'before cleanup'

# Fixture - cleanup handling exception
# pytest -q -s -rxXs
@pytest.fixture
def i_cleanup_handle_exception(request):
	def raise_now():
		raise Exception('oh no!')
	def finalizer():
		print('cleaned up after exception!')
	request.addfinalizer(finalizer)
	return raise_now()
@pytest.mark.xfail
def test_fixture_exception(i_cleanup_handle_exception):
	assert 0


# Fixture - parametized and calling/teardown order
# pytest -v -s test_module.py
@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print ("  SETUP modarg %s" % param)
    yield param
    print ("  TEARDOWN modarg %s" % param)

@pytest.fixture(scope="function", params=[1,2])
def otherarg(request):
    param = request.param
    print ("  SETUP otherarg %s" % param)
    yield param
    print ("  TEARDOWN otherarg %s" % param)

def test_0(otherarg):
    print ("  RUN test0 with otherarg %s" % otherarg)
def test_1(modarg):
    print ("  RUN test1 with modarg %s" % modarg)
def test_2(otherarg, modarg):
    print ("  RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))
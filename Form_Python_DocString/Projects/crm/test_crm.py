import pytest
from crm import User
from tinydb import Storage, TinyDB
from tinydb.storages import MemoryStorage


@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
    user = User(first_name="Patrick", last_name="Martin", address="1 rue de la paix",
                phone_number="0123456789")
    user.save()
    return user


def test_first_name(user):
    assert user.first_name == "Patrick"


def test_full_name(user):
    assert user.full_name == "Patrick Martin"


def test_db_instance():
    assert False


def test__check_phone_number():
    assert False


def test__check_names():
    assert False


def test_exists():
    assert False


def test_delete():
    assert False

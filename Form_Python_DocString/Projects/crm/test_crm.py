import pytest
from crm import User
from tinydb import Storage, TinyDB, table
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


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Patrick"
    assert user.db_instance["last_name"] == "Martin"
    assert user.db_instance["address"] == "1 rue de la paix"
    assert user.db_instance["phone_number"] == "0123456789"


def test_not_db_instance(setup_db):
    user = User(first_name="Not", last_name="Exists", address="no address",
                phone_number="0123456789")
    assert user.db_instance is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Not", last_name="Exists", address="no address",
                     phone_number="0123456789")
    user_bad = User(first_name="Not", last_name="Exists", address="no address",
                    phone_number="abcd")

    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()
    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_names_empty(setup_db):
    user_bad = User(first_name="", last_name="", address="no address",
                    phone_number="abcd")
    with pytest.raises(ValueError) as err:
        user_bad._check_names()
    assert "vides" in str(err.value)


def test__check_names_invalid_char(setup_db):
    user_bad = User(first_name="Patrick***", last_name="Martinù$*", address="no address",
                    phone_number="abcd")
    with pytest.raises(ValueError) as err:
        user_bad._check_names()
    assert "valide" in str(err.value)


def test_exists(user):
    assert user.exists() is True


def test_not_exists(setup_db):
    user = User(first_name="Not", last_name="Exists", address="no address",
                phone_number="0123456789")
    assert user.exists() is False


def test_save(setup_db):
    user_test = User(first_name="Patrick", last_name="Dupont", address="First user",
                     phone_number="0123456789")
    user_test_dup = User(first_name="Patrick", last_name="Dupont", address="Second user",
                         phone_number="0123456789")
    first = user_test.save()
    second = user_test_dup.save()

    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1


def test_delete(setup_db):
    user_test = User(first_name="Didier", last_name="Dupont", address="First user",
                     phone_number="0123456789")
    user_test.save()
    first=user_test.delete()
    second=user_test.delete()
    assert len(first)>0
    assert isinstance(first, list)
    assert len(second)==0
    assert isinstance(second,list)

import pytest
from app.user_service import UserService

@pytest.fixture
def service():
    return UserService()

def test_create_user(service):
    user = service.create_user("u1", "Anshul", "anshul@example.com")
    assert user["id"] == "u1"
    assert user["name"] == "Anshul"
    assert user["email"] == "anshul@example.com"

def test_create_user_duplicate(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    with pytest.raises(ValueError, match="already exists"):
        service.create_user("u1", "Other", "other@example.com")

def test_create_user_missing_fields(service):
    with pytest.raises(ValueError, match="required"):
        service.create_user("", "Anshul", "anshul@example.com")

def test_create_user_invalid_email(service):
    with pytest.raises(ValueError, match="Invalid email"):
        service.create_user("u2", "Test", "invalid-email")

def test_get_user(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    user = service.get_user("u1")
    assert user["name"] == "Anshul"

def test_get_user_not_found(service):
    with pytest.raises(KeyError, match="not found"):
        service.get_user("nonexistent")

def test_update_user_name(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    updated = service.update_user("u1", name="Anshul Updated")
    assert updated["name"] == "Anshul Updated"

def test_update_user_invalid_email(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    with pytest.raises(ValueError, match="Invalid email"):
        service.update_user("u1", email="bad-email")

def test_delete_user(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    assert service.delete_user("u1") is True
    with pytest.raises(KeyError):
        service.get_user("u1")

def test_list_users(service):
    service.create_user("u1", "Anshul", "anshul@example.com")
    service.create_user("u2", "Dev", "dev@example.com")
    assert len(service.list_users()) == 2

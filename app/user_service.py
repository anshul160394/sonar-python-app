class UserService:
    """Service for managing users."""

    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name, email):
        if not user_id or not name or not email:
            raise ValueError("user_id, name, and email are required.")
        if user_id in self.users:
            raise ValueError(f"User with id '{user_id}' already exists.")
        if "@" not in email:
            raise ValueError("Invalid email address.")
        self.users[user_id] = {"id": user_id, "name": name, "email": email}
        return self.users[user_id]

    def get_user(self, user_id):
        if user_id not in self.users:
            raise KeyError(f"User with id '{user_id}' not found.")
        return self.users[user_id]

    def update_user(self, user_id, name=None, email=None):
        user = self.get_user(user_id)
        if name:
            user["name"] = name
        if email:
            if "@" not in email:
                raise ValueError("Invalid email address.")
            user["email"] = email
        return user

    def delete_user(self, user_id):
        self.get_user(user_id)
        del self.users[user_id]
        return True

    def list_users(self):
        return list(self.users.values())

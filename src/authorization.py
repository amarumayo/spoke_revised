import getpass

class Authorization:
    def __init__(self):
        self.allowed_users = ('amaru', 'bob')   

    def get_current_user(self):
        return getpass.getuser()

    def is_user_authorized(self, username):
        return username in self.allowed_users

    # implements security in backend via auth checks in critical methods
    def require_authorization(self):
        user = self.get_current_user()
        if not self.is_user_authorized(user):
            raise PermissionError(f"{user} is not authorized")
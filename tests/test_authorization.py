from src.authorization import Authorization

def test_authorization_success():
    auth = Authorization()
    assert auth.is_user_authorized("amaru")

def test_authorization_fail():
    auth = Authorization()
    assert not auth.is_user_authorized("marty mcfly")
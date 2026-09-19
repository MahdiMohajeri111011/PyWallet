class TokenManager :

    _access_token = None
    _refresh_token = None
    _username = None

    @classmethod
    def set_token(cls , access_token , refresh_token , username):
        cls._access_token = access_token
        cls._refresh_token = refresh_token
        cls._username = username

    @classmethod
    def get_access_token(cls):
        return cls._access_token

    @classmethod
    def get_refresh_token(cls):
        return cls._refresh_token

    @classmethod
    def get_username(cls):
        return cls._username

    @classmethod
    def is_authenticated(cls):
        return cls._access_token is not None
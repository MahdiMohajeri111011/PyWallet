import bcrypt
from pywallet.domain.interfaces.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher) :

    def __init__(self):
        self.hashed_password = None

    def hash(self , password):
        password_bytes = str(password).encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=password_bytes , salt=salt)
        self.hashed_password = hashed_password
        return hashed_password.decode('UTF-8')

    def verify(self , password , hashed_password = None):
        if not hashed_password :
            try :
                hashed_password = self.hashed_password
            except :
                raise ValueError

        password_bytes = str(password).encode('utf-8')
        if isinstance(hashed_password , str) :
           hashed_password = hashed_password.encode('UTF-8')
        return bcrypt.checkpw(password_bytes , hashed_password)

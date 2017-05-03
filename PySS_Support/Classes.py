class Encryption:

    enc_type_list = [
        "rc4-md5",
        "salsa20",
        "chacha20",
        "chacha20-ietf",
        "aes-256-cfb",
        "aes-192-cfb",
        "aes-128-cfb"]
    _enc_index = False

    def __init__(self, str_enc):
        if isinstance(str_enc, str):
            self.set_encryption_type(str_enc)
        else:
            raise ValueError

    def __str__(self):
        if not self._enc_index==False:
            return Encryption.enc_type_list[self._enc_index]
        else:
            raise ValueError

    def get_str_from_index(self, index):

        if index < len(Encryption.enc_type_list) - 1:
            return Encryption.enc_type_list[index]
        else:
            raise IndexError

    def get_index_from_str(self, enc):

        if enc in Encryption.enc_type_list:
            return Encryption.enc_type_list.index(enc)
        else:
            return False

    def set_encryption_type(self, str_enc):

        index = self.get_index_from_str(str_enc)
        if not index == False:
            self._enc_index = index
        else:
            raise ValueError("Encryption not support!")


class SSServer:
    import json
    _ip = ""
    _password = ""
    _port = ""
    _encryption = ""
    _delay = ""

    def __str__(self):

        properties=dict()
        properties["ip"]=self.ip
        properties["port"] = self.port
        properties["password"] = self.password
        properties["encryption"] = str(self.encryption)
        properties["delay"] = str(self.delay)
        return self.json.dumps(properties)

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value):
        self._delay = value

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if isinstance(value, str):
            self._ip = value
        else:
            raise TypeError

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            self._password = value
        else:
            raise TypeError

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self._port = value
        else:
            raise TypeError

    @property
    def encryption(self):
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        if isinstance(value, str):
            self._encryption = Encryption(value)
        else:
            raise TypeError



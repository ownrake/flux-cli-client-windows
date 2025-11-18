import hashlib


class Hasher:
    @staticmethod
    def hash_string(string: str):
        hash_object = hashlib.sha256()
        hash_object.update(string.encode("utf-8"))

        return hash_object.hexdigest()

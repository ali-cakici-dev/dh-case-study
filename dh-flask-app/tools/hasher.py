import hashlib


def urlhasher(string, length=6, oldHash=None):
    if length < len(hashlib.sha256(string.encode('utf-8')).hexdigest()):
        if oldHash:
            newHash = hashlib.sha256(string.encode('utf-8')).hexdigest()[:length]
            if oldHash == newHash or len(oldHash)> len(newHash):
                return urlhasher(string, length=length + 1, oldHash=oldHash)
            else:
                return newHash
        else:
            return hashlib.sha256(string.encode('utf-8')).hexdigest()[:length]
    else:
        return urlhasher(string, length=length - 1)

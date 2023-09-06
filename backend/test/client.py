class SingletonClient:
    _instances = {}

    def __new__(cls, session):
        if session not in cls._instances:
            cls._instances[session] = super().__new__(cls)
            cls._instances[session].session = session
        return cls._instances[session]

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        return response

    def post(self, url, data=None, json=None, **kwargs):
        response = self.session.post(url, data=data, json=json, **kwargs)
        return response

    def put(self, url, data=None, json=None, **kwargs):
        response = self.session.put(url, data=data, json=json, **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.session.delete(url, **kwargs)
        return response

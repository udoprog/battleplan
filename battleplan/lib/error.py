class ErrorDict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None);
    def __setattr__(self, attr, val):
        self[attr] = val;

class ErrorDict(dict):
    def __init__(self):
        self.messages = list()
    def __getattr__(self, attr):
        return self.get(attr, None);
    def __setattr__(self, attr, val):
        self[attr] = val;
    def add(self, message):
        self.messages.append(message)
        

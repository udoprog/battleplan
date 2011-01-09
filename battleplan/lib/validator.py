class Integer:
    def __init__(self, min=0, max=100, optional=False, base=10, default=None):
        self.min = min
        self.max = max
        self.optional = optional
        self.base = base
        self.default = default
    
    def _handle_missing(self):
        if self.default is not None: return self.default
        if not self.optional: raise ValueError, "Is not optional"
    
    def __call__(self, value):
        if value is None: return self._handle_missing(); 
        i = int(value, self.base)
        if self.min is not None and i < self.min: return self.min
        if self.max is not None and i > self.max: return self.max
        return i

class String:
    def __init__(self, **kw):
        self.min = kw.get("min", 0)
        self.max = kw.get("max", 100)
        self.optional = kw.get("optional", False)
        self.default = kw.get("default", None)
        self.empty = kw.get("empty", None)
        self.filter = kw.get("filter", None)

        if self.filter and not hasattr(self.filter, "__call__"):
            raise ValueError, "filter must be callable"
    
    def _handle_missing(self):
        if self.default is not None: return self.default
        if not self.optional: raise ValueError, "Is not optional"
    
    def __call__(self, value):
        if value is None: return self._handle_missing(); 
        if self.filter: value = self.filter.__call__(value)
        if self.empty is not None and not self.empty and len(value) == 0: raise ValueError, "Must not be empty"
        if len(value) < self.min: raise ValueError, "Length must not be less than " + str(self.min)
        if len(value) > self.max: raise ValueError, "Length must not be greater than " + str(self.max)
        return value

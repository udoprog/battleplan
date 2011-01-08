from sqlalchemy import types, Column
from sqlalchemy.types import BINARY, Integer
from sqlalchemy.schema import Column

import uuid
 
class UUID(types.TypeDecorator):
    impl = BINARY
    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self,length=self.impl.length)
 
    def process_bind_param(self,value,dialect=None):
        if value and isinstance(value,uuid.UUID):
            return value.bytes
        elif value and isinstance(value,basestring):
            try:
                return uuid.UUID(value).bytes
            except ValueError:
                return None
        elif value:
            raise ValueError,'value %s is not a valid uuid.UUID' % value
        else:
            return None
 
    def process_result_value(self,value,dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None
 
    def is_mutable(self):
        return False
 
def id_column(id_column_name = "id",*args):
    return Column(id_column_name,UUID(),*args,primary_key=True)

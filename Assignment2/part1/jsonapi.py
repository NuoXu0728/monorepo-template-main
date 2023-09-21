import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {'type': 'complex', 'real': obj.real, 'imag': obj.imag}
        return super().default(obj)

class ComplexDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if dct.get('type') == 'complex':
            return complex(dct['real'], dct['imag'])
        return dct

def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=ComplexEncoder, *args, **kwargs)

def loads(json_string, *args, **kwargs):
    return json.loads(json_string, cls=ComplexDecoder, *args, **kwargs)
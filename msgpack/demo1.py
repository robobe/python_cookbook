import msgpack
import datetime

class MyType():
    def __init__(self):
        self.__a = 1
        self.__b = 2

data = msgpack.packb([1, 2, 3], use_bin_type=True)
raw = msgpack.unpackb(data , raw=False)
print(raw)

useful_dict = {
    "id": 1,
    "created": datetime.datetime.now(),
}

def decode_datetime(obj):
    print(obj)
    if b'__datetime__' in obj:
        obj = datetime.datetime.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
    return obj

def encode_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    return obj

def decode_obj(obj):
    print(obj)
    return obj

packed_dict = msgpack.packb(useful_dict, default=encode_datetime, use_bin_type=True)
this_dict_again = msgpack.unpackb(packed_dict, object_hook=decode_datetime, raw=False)
# this_dict_again = msgpack.unpackb(packed_dict, object_pairs_hook=decode_obj, raw=False)
# print(this_dict_again)

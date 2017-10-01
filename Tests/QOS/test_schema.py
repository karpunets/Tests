import json
from jsonschema import validate


from Data.Make_requests_and_answers import JSON_generator as _
data = _.make_data("test", {'$name' : 'qq',
                            '$description':'desc',
                            '$version':"6"})



schema = _.make_data("test_schm_1", {'$name' : 'qq',
                            '$description':'desc',
                            '$version':"6"})


print(data == schema)
print(type(data))

validate(data, schema)



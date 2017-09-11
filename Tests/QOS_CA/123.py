import pytest, allure, json, requests, random, string
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _



templateCriterias = {"name":"section_name_1","position":1, "templateCriterias":[]}
for i in range(3):
    new_criteria = {'$criteria_id': 111,
                    '$criteria_group_id': "22222",
                    '$weight': 33,
                    }
    data = _.make_data('template_criteria', new_criteria)
    templateCriterias["templateCriterias"].append(data)


print(templateCriterias)
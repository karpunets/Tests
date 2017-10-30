import json, pytest, requests, random, string, time
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data
from Data.Test_data import random_name
import Data.Test_data as get


@pytest.fixture(scope="module")
def setup_add_criterias(send_request):
    criteria_names = make_test_data('criteria_names', default=True)
    group_and_criteria_id = {}
    for criteria_groups in criteria_names:
        payload = {"groups": [{"id": 2}], "name": criteria_groups}
        response = send_request(url=URL.criteria_group, data=payload)
        criteria_group_id = response.json()['id']
        group_and_criteria_id[criteria_group_id] = []
        for names in criteria_names[criteria_groups]:
            criteria_data = {"name": names[0], "description": names[1], "criteriaGroup": {"id": response.json()['id']}}
            response_criteria = send_request(url=URL.criteria, data=criteria_data)
            group_and_criteria_id[criteria_group_id].append(response_criteria.json()['id'])
    yield group_and_criteria_id
    for group in group_and_criteria_id:
        for criteria in group_and_criteria_id[group]:
            data = {'id': criteria}
            send_request(URL.criteria, method='DELETE', params=data)
        data = {"criteriaGroupId": group}
        send_request(URL.delete_criteria_group, data)


@pytest.fixture(scope="module")
def setup_add_template(setup_add_criterias, send_request):
    random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))
    date_now = lambda: round(time.time() * 1000)
    payload = {"$name": random_name(),
               "$description": random_name(),
               "$dateCreate": date_now(),
               "$version": str(random.randint(1, 255))}
    # Получаем сущность template
    template = make_test_data('template', payload)
    # Получаем ID и групы критериев
    group_and_criteria_id = setup_add_criterias
    max_criterias_number = 0
    # Определяем максимальное кол-во критериев, в зависимости от ранее созданных критериев
    for i in group_and_criteria_id:
        max_criterias_number += len(group_and_criteria_id[i])
    number_of_sections = random.randint(1, 8)
    # Рандомим кол-во критериев минимум - кол-во секций, кратно - кол-ву секций
    number_of_criterias = random.choice(range(number_of_sections, max_criterias_number, number_of_sections))
    # Преобразуем из {group:[criterias]} в [group, criteria],[group, criteria]
    group_criteria_id = [[group, criteria] for group in group_and_criteria_id.keys() for criteria in
                         group_and_criteria_id[group]]
    # Рандомим критерии
    randomed_criterias = random.sample(group_criteria_id, k=number_of_criterias)
    templateSections = []
    weight = 100
    count = 1
    # Добавлем секции и наполняем их
    for i in range(1, number_of_sections + 1):
        # Сущность секции
        what_append_1 = {"name": "section_name_1", "position": 1, "templateCriterias": []}
        what_append_1['name'] = random_name()
        what_append_1['position'] = i
        templateSections.append(what_append_1)
        # Если не последняя секция
        if count != number_of_sections:
            # Количество критериев в секции (макс кол-во - кол-во секций)
            randomed_criterias_number = random.randint(1, number_of_criterias - (number_of_sections - i))
            for j in range(1, randomed_criterias_number + 1):
                # Выбираем из списка критерия и удаляем его из списка
                random_criteria_and_group = random.choice(randomed_criterias)
                randomed_criterias.remove(random_criteria_and_group)
                # Рандомим вес (вес - колво критериев минус превыдущие критерии)
                random_weight = random.randint(1, weight - (number_of_criterias - j))
                # Остаточный вес
                weight = weight - random_weight
                new_criteria = {'$criteria_id': random_criteria_and_group[1],
                                '$criteria_group_id': random_criteria_and_group[0],
                                '$weight': random_weight,
                                '$position': j}
                data = make_test_data('template_criteria', new_criteria)
                templateSections[i - 1]["templateCriterias"].append(data)
            number_of_criterias = number_of_criterias - randomed_criterias_number
            count += 1
        else:
            for j in range(1, number_of_criterias + 1):
                # Если не последний критерий
                if j != number_of_criterias:
                    random_criteria_and_group = random.choice(randomed_criterias)
                    randomed_criterias.remove(random_criteria_and_group)
                    random_weight = random.randint(1, (weight - (number_of_criterias - j)))
                    weight = weight - random_weight
                else:
                    random_criteria_and_group = randomed_criterias[0]
                    random_weight = weight
                new_criteria = {'$criteria_id': random_criteria_and_group[1],
                                '$criteria_group_id': random_criteria_and_group[0],
                                '$weight': random_weight,
                                '$position': j}
                data = make_test_data('template_criteria', new_criteria)
                templateSections[i - 1]["templateCriterias"].append(data)
    template["templateSections"] = templateSections
    response = send_request(URL.edit_template, template)
    yield response.json()['id']


@pytest.fixture()
def add_group(send_request):
    payload = {"groups": [{"id": 2}], "name": random_name()}
    response = send_request(URL.criteria_group, payload)
    group_id_name = {'id':response.json()['id'], 'name':response.json()['name']}
    yield group_id_name
    send_request(URL.delete_criteria_group,{"criteriaGroupId": group_id_name['id']})


@pytest.fixture(scope="function")
def delete_group(send_request):
    for_delete = {}
    yield for_delete
    for id in for_delete.values():
        payload = json.dumps({"criteriaGroupId":id})
        send_request(URL.delete_criteria_group, payload)

# @pytest.fixture(scope="function")
# def add_questioner():
#     IDs = get_template()
#     new_random = random.sample(set(IDs), 3)
#     payload_questioner = json.dumps({"name": "for_CA_test",
#                             "templateId": 141383199,
#                             "url": "http://172.22.2.36:9080/qualityout",
#                             "active": True,
#                             "mentor": 68,
#                             "group": 2,
#                             "criterias": [ {
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                  "result": 20},
#                                                                 {"phoneButton": 2,
#                                                                  "result": 40},
#                                                                 {"phoneButton": 3,
#                                                                  "result": 60},
#                                                                 {"phoneButton": 4,
#                                                                  "result": 80},
#                                                                 {"phoneButton": 5,
#                                                                  "result": 100}
#                                                                 ],
#                                             "qosCriteriaId": new_random[0],
#                                             "questionNumber": 1},
#                                             {
#                                             "qosCriteriaId": new_random[1],
#                                             "questionNumber": 2,
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                   "result": 5},
#                                                                  {"phoneButton": 2,
#                                                                   "result": 15},
#                                                                  {"phoneButton": 3,
#                                                                   "result": 30},
#                                                                  {"phoneButton": 4,
#                                                                   "result": 99},
#                                                                  {"phoneButton": 5,
#                                                                   "result": 100}
#                                                                  ]},
#                                             {
#                                             "qosCriteriaId": new_random[2],
#                                             "questionNumber": 3,
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                  "result": 100},
#                                                                 {"phoneButton": 2,
#                                                                  "result": 0}]
#                                             }]})
#     print(payload_questioner)
#     response = requests.post(url,headers=headers, data=payload_questioner)
#     print('QUESTIONER', response.json())
#     return response.json()['id']

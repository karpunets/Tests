import pytest,  json, requests, random, string, time
import Data.URLs_MAP as URL
# from Data.Make_requests_and_answers import make_data



# template = _.make_data('template')



# def test_setup_add_template(setup_add_criterias, send_request):
#     random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))
#     date = lambda: round(time.time() * 1000)
#
#     payload = {"$name": random_name(),
#                "$description": random_name(),
#                "$dateCreate": date(),
#                "$version": str(random.randint(1, 255))}
#     # Получаем сущность template
#     template = _.make_data('template', payload)
#     # Получаем ID и групы критериев
#     group_and_criteria_id = setup_add_criterias
#     max_criterias_number = 0
#     # Определяем максимальное кол-во критериев, в зависимости от ранее созданных критериев
#     for i in group_and_criteria_id:
#         max_criterias_number += len(group_and_criteria_id[i])
#     number_of_sections = random.randint(1, 8)
#     # Рандомим кол-во критериев минимум - кол-во секций, кратно - кол-ву секций
#     number_of_criterias = random.choice(range(number_of_sections, max_criterias_number, number_of_sections))
#     # Преобразуем из {group:[criterias]} в [group, criteria],[group, criteria]
#     group_criteria_id = [[group, criteria] for group in group_and_criteria_id.keys() for criteria in
#                          group_and_criteria_id[group]]
#     # Рандомим критерии
#     randomed_criterias = random.sample(group_criteria_id, k=number_of_criterias)
#     templateSections = []
#     weight = 100
#     count = 1
#     # Добавлем секции и наполняем их
#     for i in range(1, number_of_sections + 1):
#         # Сущность секции
#         what_append_1 = {"name": "section_name_1", "position": 1, "templateCriterias": []}
#         what_append_1['name'] = random_name()
#         what_append_1['position'] = i
#         templateSections.append(what_append_1)
#         # Если не последняя секция
#         if count != number_of_sections:
#             # Количество критериев в секции (макс кол-во - кол-во секций)
#             randomed_criterias_number = random.randint(1, number_of_criterias - (number_of_sections - i))
#             for j in range(1, randomed_criterias_number + 1):
#                 # Выбираем из списка критерия и удаляем его из списка
#                 random_criteria_and_group = random.choice(randomed_criterias)
#                 randomed_criterias.remove(random_criteria_and_group)
#                 # Рандомим вес (вес - колво критериев минус превыдущие критерии)
#                 random_weight = random.randint(1, weight - (number_of_criterias - j))
#                 # Остаточный вес
#                 weight = weight - random_weight
#                 new_criteria = {'$criteria_id': random_criteria_and_group[1],
#                                 '$criteria_group_id': random_criteria_and_group[0],
#                                 '$weight': random_weight,
#                                 '$position': j}
#                 data = _.make_data('template_criteria', new_criteria)
#                 templateSections[i - 1]["templateCriterias"].append(data)
#             number_of_criterias = number_of_criterias - randomed_criterias_number
#             count += 1
#         else:
#             for j in range(1, number_of_criterias + 1):
#                 # Если не последний критерий
#                 if j != number_of_criterias:
#                     random_criteria_and_group = random.choice(randomed_criterias)
#                     randomed_criterias.remove(random_criteria_and_group)
#                     random_weight = random.randint(1, (weight - (number_of_criterias - j)))
#                     weight = weight - random_weight
#                 else:
#                     random_criteria_and_group = randomed_criterias[0]
#                     random_weight = weight
#                 new_criteria = {'$criteria_id': random_criteria_and_group[1],
#                                 '$criteria_group_id': random_criteria_and_group[0],
#                                 '$weight': random_weight,
#                                 '$position': j}
#                 data = _.make_data('template_criteria', new_criteria)
#                 templateSections[i - 1]["templateCriterias"].append(data)
#     template["templateSections"] = templateSections
#     response = send_request(URL.edit_template, template)



def test_setup_add_template(make_test_data):
    random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))
    date = lambda: round(time.time() * 1000)

    payload = {"$name": random_name(),
               "$description": random_name(),
               "$dateCreate": date(),
               "$version": str(random.randint(1, 255))}
    # Получаем сущность template
    template = make_test_data('example', payload)
    print(template)













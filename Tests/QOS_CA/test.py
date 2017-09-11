import pytest,  json, requests, random, string
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _

a = {"ПРАВИЛЬНОСТЬ ПРЕДОСТАВЛЕНИЯ ИНФОРМАЦИИ И РАБОТА С ВОЗРАЖЕНИЯМИ":
                          [["аргументация","Использование правильной, действенной аргументации на основе действующих правил и процедур при работе с возражениями, исключающее повторное обращение к другому сотруднику с тем же вопросом."],
                           ["корректность информации","Специалист предоставил корректную информацию"],
                           ["доп.информация по запросу","Специалист предоставил сопутствующую информацию для решения запроса, чтобы исключить повторные звонки"],
                           ["работа с возражениями","внимательное слушание, конструктивная реакция на критику"]],
                      "ПРОАКТИВНОСТЬ":[["альтернативные решения","Специалист предложил дополнительные или альтернативные варианты решения (при их наличии)"],
                                       ["презентация решения","Специалист эффективно презентовал выгоды и преимущества предлагаемого решения"]],
                        "ЗАИНТЕРЕСОВАННОСТЬ И АКТИВНОЕ СЛУШАНИЕ":
                          [["заинтересованность","Специалист использовал формулировки, показывающие готовность помочь и стремление к сотрудничеству ('конечно, 'чем могу еще помочь'и пр.)"],
                           ["перебивание клиента","Специалист дослушивал абонента до конца (не перебивал)"],
                           ["внимательность","Специалист максимально концентрировался на запросе абонента и не переспрашивал без необходимости озвученную абонентом информацию"],
                           ["активное слушание","Специалист активно слушал абонента, используя одобряющие слова и междометия («да-да», «так» и пр.) либо молча дослушал до конца"]],
                      "ОЖИДАНИЕ, ПАУЗЫ, HOLD, ПЕРЕКЛЮЧЕНИЯ":
                          [["согласие ожидать","Специалист заручился согласием абонента ожидать в виде формулировки 'Будет ли Вам удобно ожидать?' либо аналогичной в вопросительной форме"],
                           ["возврат к клиенту после ожидания","Специалист поблагодарил за ожидание после hold-а либо паузы"],
                           ["продолжительность решения","Время решения запроса было оптимальным, без затягивания и пауз"],
                           ["правильность использования hold","Специалист использовал hold в том случае, если поиск решения не мог быть предоставлен одновременно с диалогом с абонентом"]],
                      "РЕЧЕВЫЕ ХАРАКТЕРИСТИКИ И ГРАМОТНОСТЬ РЕЧИ":
                          [["интонированность речи","Голос Специалиста был интонирован:с акцентом на ключевые слова и лишен монотонности, усталости, 'механических' оттенков"],
                           ["использование деловой лексики","Специалист консультировал без нарушения правил деловой лексики (ударения, уменьшительные слова), без использования слов-паразитов, разговаривал без пауз колебания: «э-ээ», «м-мм», «нуу-у»"]],
                      "УТОЧНЯЮЩИЕ ВОПРОСЫ И ПОНЯТНОСТЬ ПРЕДОСТАВЛЕНИЯ ИНФОРМАЦИИ":
                          [["терминология","Специалист исключил из консультации специфическую терминологию, непонятную абоненту"],
                           ["уточняющие вопросы","Специалист задал уточняющие вопросы для раскрытия запроса абонента до начала консультирования"],
                           ["структурированность изложения","Специалист строил разговор логично и структурировано, делал паузы между блоками информации"]],
                     "ВЕЖЛИВОСТЬ И ДОБРОЖЕЛАТЕЛЬНОСТЬ":
                          [["обращение по имени","Специалист уточнил имя абонента, обращался к абоненту по имени в процессе разговора и при этом обращение было уместно и не повторялось в каждом предложении"],
                           ["интонации","Интонации Специалиста были без раздражения"],
                           ["завершение разговора","Специалист предложил обращаться при возникающих вопросах, прощался доброжелательно"],
                           ["безоценочная консультация","Специалист консультировал без личностной оценки абонента/его действий/решений"],
                           ["формы вежливости","Специалист уместно использовал вежливые формы при обращении к абоненту или при побуждении его к действию ('будьте добры', 'пожалуйста' и п.р."]]}

b = {"dateCreate":1504526486176,"supervisor": {"fname":"Root","lname":"Initiate","pname":"User","id":68},
  "name":"name_1","description":"desc","groups":[{"id":2}],"version":"1",
  "templateSections":[]}

example_id = {11111:[1,2,3,4,5], 22222:[6,7,8], 33333:[9,10,11,12]}
max_criterias_number = 0
for i in example_id:
     max_criterias_number+=len(example_id[i])




number_of_sections = random.randint(1,5)
number_of_criterias = random.choice(range(number_of_sections, max_criterias_number, number_of_sections))


group_criteria_id = [[group, criteria] for group in example_id.keys() for criteria in example_id[group]]


randomed_criterias = random.sample(group_criteria_id, k=number_of_criterias)


templateSections = []
weight = 100
count = 1
for i in range(1, number_of_sections+1):
    what_append_1 = {"name":"section_name_1","position":1, "templateCriterias":[]}
    # what_append_2 = {"templateCriteria":{"id":140530162,"criteriaGroup":{"id":140530159}},"weight":"10","position":1}
    random_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    what_append_1['name'] =random_name
    what_append_1['position'] = i
    templateSections.append(what_append_1)
    # Если не последняя секция
    if count != number_of_sections:
        # Количество критериев в секции (макс кол-во - кол-во секций)
        randomed_criterias_number = random.randint(1,number_of_criterias - (number_of_sections - i))
        for j in range(1,randomed_criterias_number+1):
            # Выбираем из списка критерия и удаляем его из списка
            random_criteria_and_group = random.choice(randomed_criterias)
            randomed_criterias.remove(random_criteria_and_group)
            # Рандомим вес (вес - колво критериев минус превыдущие критерии)
            random_weight = random.randint(1,weight-(number_of_criterias-j))
            #Остаточный вес
            weight = weight - random_weight
            new_criteria = {'$criteria_id':random_criteria_and_group[1],
                            '$criteria_group_id':random_criteria_and_group[0],
                            '$weight':weight,
                            '$position':j}
            data = _.make_data('template_criteria',new_criteria)
            templateSections[i - 1]["templateCriterias"].append(data)
        number_of_criterias = number_of_criterias - randomed_criterias_number
        count += 1
    else:
        for j in range(1,number_of_criterias+1):
            #Если не последний критерий
            if j !=number_of_criterias:
                random_criteria_and_group = random.choice(randomed_criterias)
                randomed_criterias.remove(random_criteria_and_group)
                random_weight = random.randint(1,(weight-(number_of_criterias-j)))
                weight = weight - random_weight
            else:
                random_criteria_and_group = randomed_criterias[0]
                random_weight = weight
            new_criteria = {'$criteria_id': random_criteria_and_group[1],
                                '$criteria_group_id': random_criteria_and_group[0],
                                '$weight': weight,
                                '$position': j}

            data = _.make_data('template_criteria', new_criteria)
            templateSections[i - 1]["templateCriterias"].append(data)


b["templateSections"] = templateSections








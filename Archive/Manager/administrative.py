import allure
import pytest

import Data.URLs_MAP as URL
from bin.common import JSON_generator as _


@allure.feature('Позитивный тест')
@allure.story('Получаем логи')
def test_get_logs(send_request):
    name ="Manager_logs"
    data = _.get_JSON_request(name)
    response = send_request(url=URL.Manager_logs, data = data)
    assert response.status_code == 200


@allure.feature('Позитивный тест')
@allure.story('Изменяем уровень логирования в Менеджере')
@pytest.mark.parametrize('debugLevel', ['3', '2','1','0'])
@pytest.mark.parametrize('logLenght', ['500'])
def test_edit_settings(send_request, debugLevel, logLenght):
    name ="Manager_settings"
    data = _.get_JSON_request(name, **{"debugLevel":debugLevel,"logLength":logLenght})
    response = send_request(url=URL.Manager_settings, data = data)
    assert response.status_code == 200


@allure.feature('Негативный тест')
@allure.story('Изменяем уровень логирования в Менеджере')
def test_edit_settings_to_5_debuglelvel(send_request,):
    name ="Manager_settings"
    data = _.get_JSON_request(name, **{"debugLevel":"5"})
    response = send_request(url=URL.Manager_settings, data = data)
    answer = {'MANAGER_VALIDATION_SETTINGS_DEBUG_LEVEL': 'Debug level must be from 0 to 3!'}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Проверить подключение')
def test_test_domain(send_request):
    name ="test_domain"
    data = _.get_JSON_request(name)
    response = send_request(url=URL.test_domain, data = data)
    assert response.status_code == 200
    assert response.text == "successful"


@allure.feature('Негативный тест')
@allure.story('Проверить подключение, пустые значения')
def test_test_domain_with_empty_fields(send_request):
    data = {}
    response = send_request(url=URL.test_domain, data = data)
    answer = {"ADM_VALIDATION_DOMAIN_IP_LENGTH":"IP length from 1 to 256",
              "ADM_VALIDATION_DOMAIN_PER_PAGE_LENGTH":"PER PAGE more then 1 less then 1500",
              "ADM_VALIDATION_DOMAIN_USER_LOGIN_LENGTH":"USER LOGIN length from 1 to 256",
              "ADM_VALIDATION_DOMAIN_NAME_LENGTH":"NAME length from 1 to 256"}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Добавить и удалить домен')
def test_add_delete_domain(send_request):
    name ="test_domain"
    data = _.get_JSON_request(name)
    response = send_request(url=URL.edit_domain, data = data)
    domain_id = response.json()['id']
    answer = _.get_JSON_response(name, **{'id':domain_id})
    assert response.status_code == 200
    assert response.json() == answer
    #Подготавливаем данные для удаления
    data = {'domainId':domain_id}
    response = send_request(url = URL.delete_domain, data=data)
    assert response.status_code == 200
    assert response.json() == True


@allure.feature('Позитивный тест')
@allure.story('Получаем права ролей для ROOT')
def test_get_task_list(send_request):
    data = {"roleId":3}
    response = send_request(url=URL.get_task_list, data = data)
    assert response.status_code == 200
    assert response.json()['name'] == 'ROOT'


@allure.feature('Негативный тест')
@allure.story('Изменяем права ролей для ROOT(системной роли)')
def test_edit_ROOT_task_list(send_request):
    response = send_request(url=URL.get_task_list, data = {"roleId":3})
    task_list = response.json()
    task_list['tasks'][0]['value'] = 0
    response = send_request(url = URL.set_tasks_to_role, data = task_list)
    answer = {"COMMON_EXCEPTION":"CommonException: System role can't be modified"}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Получаем права ролей для не существующей роли')
def test_get_task_list_for_999999_roleID(send_request):
    data = {"roleId":99999999999999}
    response = send_request(url=URL.get_task_list, data = data)
    answer = {'DATA_ACCESS_NO_RESULT_EXCEPTION': 'javax.persistence.NoResultException: No entity found for query'}
    assert response.status_code == 500
    assert response.json() == answer


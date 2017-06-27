import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


@allure.feature('Позитивный тест')
@allure.story('Получаем логи')
def test_get_logs(make_request):
    name ="Manager_logs"
    data = _.get_JSON_request(name)
    response = make_request(url=URL.Manager_logs, data = data)
    assert response.status_code == 200


@allure.feature('Позитивный тест')
@allure.story('Изменяем уровень логирования в Менеджере')
@pytest.mark.parametrize('debugLevel', ['3', '2','1','0'])
@pytest.mark.parametrize('logLenght', ['500'])
def test_edit_settings(make_request, debugLevel, logLenght):
    name ="Manager_settings"
    data = _.get_JSON_request(name, **{"debugLevel":debugLevel,"logLength":logLenght})
    response = make_request(url=URL.Manager_settings, data = data)
    assert response.status_code == 200


@allure.feature('Негативный тест')
@allure.story('Изменяем уровень логирования в Менеджере')
def test_edit_settings_to_5_debuglelvel(make_request,):
    name ="Manager_settings"
    data = _.get_JSON_request(name, **{"debugLevel":"5"})
    response = make_request(url=URL.Manager_settings, data = data)
    answer = {'MANAGER_VALIDATION_SETTINGS_DEBUG_LEVEL': 'Debug level must be from 0 to 3!'}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Проверить подключение')
def test_test_domain(make_request):
    name ="test_domain"
    data = _.get_JSON_request(name)
    response = make_request(url=URL.test_domain, data = data)
    assert response.status_code == 200
    assert response.text == "successful"

@allure.feature('Негативный тест')
@allure.story('Проверить подключение, пустые значения')
def test_test_domain_with_empty_fields(make_request):
    data = {}
    response = make_request(url=URL.test_domain, data = data)
    answer = {"ADM_VALIDATION_DOMAIN_IP_LENGTH":"IP length from 1 to 256",
              "ADM_VALIDATION_DOMAIN_PER_PAGE_LENGTH":"PER PAGE more then 1 less then 1500",
              "ADM_VALIDATION_DOMAIN_USER_LOGIN_LENGTH":"USER LOGIN length from 1 to 256",
              "ADM_VALIDATION_DOMAIN_NAME_LENGTH":"NAME length from 1 to 256"}
    assert response.status_code == 400
    assert response.json() == answer

@allure.feature('Позитивный тест')
@allure.story('Добавить и удалить домен')
def test_add_delete_domain(make_request):
    name ="test_domain"
    data = _.get_JSON_request(name)
    response = make_request(url=URL.edit_domain, data = data)
    domain_id = response.json()['id']
    answer = _.get_JSON_response(name, **{'id':domain_id})
    assert response.status_code == 200
    assert response.json() == answer
    #Подготавливаем данные для удаления
    data = {'domainId':domain_id}
    response = make_request(url = URL.delete_domain, data=data)
    assert response.status_code == 200
    assert response.json() == True
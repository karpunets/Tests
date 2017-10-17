import pytest, requests
import Data.URLs_MAP as URL

@pytest.fixture(scope='module')
def add_campaign(send_request):
    payload = _.get_JSON_request('add_campaign')
    response = send_request(url=URL.edit_campaign, data=payload)
    assert response.status_code == 200
    campaign_id = response.json()['id']
    yield response.json()
    response = requests.delete(url=URL.delete_campaign, params={'id': campaign_id}, headers=URL.headers)
    assert response.status_code == 200

import requests, responses
import pytest
from requests.models import Response

TESTING_ENV_COMPANIES_URL = 'http://127.0.0.1:8000/companies/'
DOGECOIN_API_URL = 'https://api.cryptonator.com/api/ticker/doge-usd'


def cleanup_company(company_id: str) -> None:
    response: Response = requests.delete(
        url=f'{TESTING_ENV_COMPANIES_URL}{company_id}')
    assert response.status_code == 204


@pytest.mark.skip_in_ci
@pytest.mark.skip(reason='This test needs localhost django server running.')
def test_zero_companies_django_agnostic() -> None:
    response = requests.get(url=TESTING_ENV_COMPANIES_URL)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.skip_in_ci
@pytest.mark.skip(reason='This test needs localhost django server running.')
def test_create_company_with_layoffs_django_agnostic() -> None:
    response: Response = requests.post(
        url=TESTING_ENV_COMPANIES_URL,
        json={
            'name': 'test company name',
            'status': 'Layoffs'
        },
    )
    assert response.status_code == 201
    response_content: dict = response.json()
    assert response_content['status'] == 'Layoffs'

    cleanup_company(company_id=response_content['id'])


@pytest.mark.crypto
def test_dogecoin_api() -> None:
    response = requests.get(url=DOGECOIN_API_URL,
                            headers={'User-Agent': 'Mozilla/5.0'})
    assert response.status_code == 200
    response_content = response.json()
    assert response_content['ticker']['base'] == 'DOGE'
    assert response_content['ticker']['target'] == 'USD'


@responses.activate
@pytest.mark.crypto
def test_mocked_dogecoin_api() -> None:
    responses.add(method=responses.GET,
                  url=DOGECOIN_API_URL,
                  json={
                      "ticker": {
                          "base": "JADECOIN",
                          "target": "JADE-BUCKS",
                          "price": "0.20100142",
                          "volume": "583647324.73704004",
                          "change": "0.00624032"
                      },
                      "timestamp": 1638220142,
                      "success": True,
                      "error": ""
                  },
                  status=200)
    
    assert process_crypto() == 'Mock API call was successful.'
    


def process_crypto() -> str:
    response = requests.get(
        url=DOGECOIN_API_URL,
        headers={'User-Agent': 'Mozilla/5.0'},
    )
    if response.status_code != 200:
        raise ValueError('Request to Crypto API FAILED!')
    
    response_content = response.json()
    if response_content['ticker']['base'] == 'JADECOIN' and response_content['ticker']['target'] == 'JADE-BUCKS':
        return 'Mock API call was successful.'
    return 'Mock API call FAILED!'
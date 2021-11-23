import pytest
from django.urls import reverse

from conftest import track_performance

# FIBONACCI_URL = reverse('fibonacci_api:index')
FIBONACCI_URL = '/fibonacci/'


@pytest.mark.integration_test
def test_fibonacci_api(client):
    def test_argument_nine_should_return_thirty_four():
        response = client.get(FIBONACCI_URL + '?n=9')
        assert response.status_code == 200

        # The below code achieves the same as the following code: json.loads(response.content)
        response_content = response.json()

        assert response_content.get(
            'status') == 'successfully calculated fibonacci number'
        assert response_content.get('value') == '34'

    def test_argument_negative_one_should_fail_and_return_error():
        response = client.get(FIBONACCI_URL + '?n=-1')
        assert response.status_code == 400

        response_content = response.json()
        assert response_content.get(
            'status') == 'Error. Must send an integer 0 or greater'
        assert response_content.get('value') == '-1'

    def test_argument_string_should_fail_and_return_error():
        response = client.get(FIBONACCI_URL + '?n=test-string')
        assert response.status_code == 400

        response_content = response.json()
        assert response_content.get(
            'status') == 'Error. Must send an integer 0 or greater'
        assert response_content.get('value') == 'test-string'

    test_argument_nine_should_return_thirty_four()
    test_argument_negative_one_should_fail_and_return_error()
    test_argument_string_should_fail_and_return_error()


@pytest.mark.stress_test
@track_performance
def test_fibonacci_api_under_stress(client):
    for i in range(1000):
        response = client.get(FIBONACCI_URL + '?n=250')
        assert response.status_code == 200

        response_content = response.json()
        assert response_content.get(
            'status') == 'successfully calculated fibonacci number'
        assert response_content.get(
            'value') == '7896325826131730509282738943634332893686268675876375'

import pytest
from app import app
import json


@pytest.fixture
def client():
    app.config.update({
        'TESTING': True,
    })
    return app.test_client()


# Test for valid currency conversion
def test_valid_exchange(client):
    response = client.get('/?source=USD&target=JPY&amount=$1,525')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['msg'] == 'success'
    assert data['amount'] == '$170,496.53'


# Test when a required parameter is missing
def test_missing_parameters(client):
    response = client.get('/?source=USD&amount=$1,525')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['msg'] == 'error'
    assert data['description'] == 'Missing required parameters'


# Test when no parameters are provided
def test_no_parameters(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['msg'] == 'error'
    assert data['description'] == 'Missing required parameters'


# Test for incorrect amount format
def test_invalid_amount(client):
    response = client.get('/?source=USD&target=JPY&amount=$abc')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['msg'] == 'error'
    assert data['description'] == 'Invalid amount format'


# Test for incorrect amount format without thousand separators
def test_invalid_amount_no_separator(client):
    response = client.get('/?source=USD&target=JPY&amount=$1525')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['msg'] == 'error'
    assert data['description'] == 'Invalid amount format'


# Test for unsupported currency conversion
def test_unsupported_currency(client):
    response = client.get('/?source=JPY&target=EUR&amount=$1,525')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['msg'] == 'error'
    assert data['description'] == 'Unsupported currency'

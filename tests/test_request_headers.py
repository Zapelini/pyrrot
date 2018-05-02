import pytest
from flask import json


def test_with_headers(client, url_example_header):
    response = client(url_example_header).get('/users', headers={'TRACKID': 'abc123456', 'AUTHORIZATION': 'abacaxi'},
                                              content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert 200 == response.status_code
    assert 'abc123456' == response.headers['TRACKID']
    assert 'John Doe' == data['name']
    assert 666 == data['identity']


def test_without_headers(client, url_example_header):
    response = client(url_example_header).get('/companies', content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert 200 == response.status_code
    assert 'abc123456' == response.headers['TRACKID']
    assert 'Oracle' == data['name']
    assert 999 == data['identity']


@pytest.mark.parametrize('header', [{'TRACKID': 'abc123456', 'AUTHORIZATION': 'jaca'},
                                    {'TRACKID': 'abc123456'},
                                    None])
def test_with_wrong_headers(client, url_example_header, header):
    response = client(url_example_header).get('/users', headers=header,
                                              content_type='application/json')
    assert 404 == response.status_code

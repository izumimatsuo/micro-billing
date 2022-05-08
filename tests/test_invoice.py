import pytest


def test_select_all(client):
    res = client.get('/invoices')
    assert res.status_code == 200
    data = res.json()
    assert 1 == len(data['invoices'])


def test_select_one(client):
    res = client.get('/invoices/1')
    assert res.status_code == 200
    data = res.json()
    assert data['period_start'].startswith('2021-01-01')


def test_not_found(client):
    res = client.get('/invoices/5')
    assert res.status_code == 404


def test_all_days(client):
    res = client.get('/invoices/data')
    assert res.status_code == 200
    assert 4 == len(res.content.splitlines())
    assert b'"name","amount","start_date"' in res.content
    assert b'"Taro",980,"2021-01-01 00:00:00"' in res.content
    assert b'"Jiro",1500,"2021-01-31 00:00:00"' in res.content
    assert b'"Hanako",980,"2021-02-28 00:00:00"' in res.content


def test_first_day(client):
    res = client.get('/invoices/data/20210401')
    assert res.status_code == 200
    assert 2 == len(res.content.splitlines())
    assert b'"name","amount","start_date"' in res.content
    assert b'"Taro",980,"2021-01-01 00:00:00"' in res.content


def test_last_day(client):
    res = client.get('/invoices/data/20210430')
    assert res.status_code == 200
    assert 2 == len(res.content.splitlines())
    assert b'"name","amount","start_date"' in res.content
    assert b'"Jiro",1500,"2021-01-31 00:00:00"' in res.content


def test_leap_year(client):
    res = client.get('/invoices/data/20240229')
    assert res.status_code == 200
    assert 2 == len(res.content.splitlines())
    assert b'"name","amount","start_date"' in res.content
    assert b'"Jiro",1500,"2021-01-31 00:00:00"' in res.content


def test_not_leap_year(client):
    res = client.get('/invoices/data/20220228')
    assert res.status_code == 200
    assert 3 == len(res.content.splitlines())
    assert b'"name","amount","start_date"' in res.content
    assert b'"Jiro",1500,"2021-01-31 00:00:00"' in res.content
    assert b'"Hanako",980,"2021-02-28 00:00:00"' in res.content


def test_bad_request(client):
    res = client.get('/invoices/data/20210431')
    assert res.status_code == 400

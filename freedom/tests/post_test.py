from unittest import mock


async def test_post(anonym_client, mocker):
    mocker.patch('aioga.GA')
    r = await anonym_client.get('v1/wind')
    assert r.status == 200, await r.text()

import arcgis_sdk
import json
import pytest
import responses


@responses.activate
def test_refresh_token(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'oauth2/token/',
        body=json.dumps({
            'access_token': 'new!'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.refresh_token(
        client_id='client_id',
        refresh_token='refresh_token'
    )['access_token'] == 'new!'


@responses.activate
def test_self(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'portals/self',
        body=json.dumps({
            'name': 'test'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.self()['name'] == 'test'


@responses.activate
def test_search_users(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'community/users',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.users(q='test')['total'] == 1


@responses.activate
def test_user_detail(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'community/users/test',
        body=json.dumps({
            'username': 'test'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.user_detail('test')['username'] == 'test'


@responses.activate
def test_search_groups(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.groups(q='test')['total'] == 1


@responses.activate
def test_create_group(client):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/createGroup',
        body=json.dumps({
            'success': True
        }),
        status=200,
        content_type='application/json'
    )

    assert client.create_group(
        title='test',
        access='public'
    )['success'] is True


@responses.activate
def test_update_group(client):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test/update',
        body=json.dumps({
            'success': True
        }),
        status=200,
        content_type='application/json'
    )

    assert client.update_group(
        group_id='test',
        title='edit'
    )['success'] is True


@responses.activate
def test_add_users_to_group(client, users):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test/addUsers',
        body=json.dumps({
            'added': users.split(',')
        }),
        status=200,
        content_type='application/json'
    )

    assert 'added' in client.add_users_to_group(
        group_id='test',
        users=users
    )


@responses.activate
def test_invite_to_group(client, users):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test/invite',
        body=json.dumps({
            'success': True
        }),
        status=200,
        content_type='application/json'
    )

    assert client.invite_to_group(
        group_id='test',
        users=users
    )['success'] is True


@responses.activate
def test_server_error(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'error',
        status=500,
        content_type='application/json'
    )

    with pytest.raises(arcgis_sdk.ArcgisAPIError):
        client.request('error')


@responses.activate
def test_exception(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'error',
        body=json.dumps({
            'error': {
                'code': 400,
                'details': [],
                'message': 'buh!'
            }
        }),
        status=200,
        content_type='application/json'
    )

    with pytest.raises(arcgis_sdk.ArcgisAPIError):
        client.request('error')

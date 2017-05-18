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
def test_self_users(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'portals/self/users',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.self_users()['total'] == 1


@responses.activate
def test_self_roles(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'portals/self/roles',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.self_roles()['total'] == 1


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
def test_group_detail(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test',
        body=json.dumps({
            'id': 'test'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.group_detail(
        group_id='test'
    )['id'] == 'test'


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
def test_delete_group(client):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test/delete',
        body=json.dumps({
            'success': True
        }),
        status=200,
        content_type='application/json'
    )

    assert client.delete_group(
        group_id='test'
    )['success'] is True


@responses.activate
def test_add_to_group(client, users):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'community/groups/test/addUsers',
        body=json.dumps({
            'added': users.split(',')
        }),
        status=200,
        content_type='application/json'
    )

    assert 'added' in client.add_to_group(
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
def test_user_items(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'content/users/test',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.user_items('test')['total'] == 1


@responses.activate
def test_group_items(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'content/groups/test',
        body=json.dumps({
            'total': 1
        }),
        status=200,
        content_type='application/json'
    )

    assert client.group_items('test')['total'] == 1


@responses.activate
def test_item_detail(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL + 'content/items/test',
        body=json.dumps({
            'id': 'test'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.item_detail('test')['id'] == 'test'


@responses.activate
def test_add_item(client):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'content/users/test/addItem',
        body=json.dumps({
            'success': True
        }),
        status=200,
        content_type='application/json'
    )

    assert client.add_item(
        username='test',
        title='my item',
        type='Web Mapping Application'
    )['success'] is True


@responses.activate
def test_share_item(client, groups):
    responses.add(
        responses.POST,
        arcgis_sdk.ARCGIS_API_URL + 'content/items/test/share',
        body=json.dumps({
            'itemId': 'test'
        }),
        status=200,
        content_type='application/json'
    )

    assert client.share_item('test', groups)['itemId'] == 'test'


@responses.activate
def test_server_error(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL,
        status=500,
        content_type='application/json'
    )

    with pytest.raises(arcgis_sdk.ArcgisAPIError):
        client.request('')


@responses.activate
def test_exception(client):
    responses.add(
        responses.GET,
        arcgis_sdk.ARCGIS_API_URL,
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
        client.request('')

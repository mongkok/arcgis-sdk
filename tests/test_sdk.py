import arcgis_sdk
import pytest
import responses

from .shortcuts import add_response


@responses.activate
def test_refresh_token(client):
    add_response(
        'GET',
        'oauth2/token/',
        json={'access_token': 'new!'}
    )

    assert client.refresh_token(
        client_id='client_id',
        refresh_token='refresh_token'
    )['access_token'] == 'new!'


@responses.activate
def test_self(client):
    add_response(
        'GET',
        'portals/self',
        json={'name': 'test'}
    )

    assert client.self()['name'] == 'test'


@responses.activate
def test_self_users(client):
    add_response(
        'GET',
        'portals/self/users',
        json={'total': 1}
    )

    assert client.self_users()['total'] == 1


@responses.activate
def test_self_roles(client):
    add_response(
        'GET',
        'portals/self/roles',
        json={'total': 1}
    )

    assert client.self_roles()['total'] == 1


@responses.activate
def test_search_users(client):
    add_response(
        'GET',
        'community/users',
        json={'total': 1}
    )

    assert client.users(q='test')['total'] == 1


@responses.activate
def test_user_detail(client):
    add_response(
        'GET',
        'community/users/test',
        json={'username': 'test'}
    )

    assert client.user_detail('test')['username'] == 'test'


@responses.activate
def test_user_thumbnail(client):
    add_response(
        'GET',
        'community/users/test/info/me.png',
        content_type='image/png',
        body=':)',
        stream=True
    )

    assert client.user_thumbnail('test', 'me.png').data == ':)'


@responses.activate
def test_search_groups(client):
    add_response(
        'GET',
        'community/groups',
        json={'total': 1}
    )

    assert client.groups(q='test')['total'] == 1


@responses.activate
def test_create_group(client):
    add_response(
        'POST',
        'community/createGroup',
        json={'success': True}
    )

    assert client.create_group(
        title='test',
        access='public'
    )['success'] is True


@responses.activate
def test_group_detail(client):
    add_response(
        'GET',
        'community/groups/test',
        json={'id': 'test'}
    )

    assert client.group_detail(group_id='test')['id'] == 'test'


@responses.activate
def test_update_group(client):
    add_response(
        'POST',
        'community/groups/test/update',
        json={'success': True}
    )

    assert client.update_group(
        group_id='test',
        title='edit'
    )['success'] is True


@responses.activate
def test_delete_group(client):
    add_response(
        'POST',
        'community/groups/test/delete',
        json={'success': True}
    )

    assert client.delete_group(group_id='test')['success'] is True


@responses.activate
def test_add_to_group(client, users):
    add_response(
        'POST',
        'community/groups/test/addUsers',
        json={'added': users.split(',')}
    )

    assert 'added' in client.add_to_group(
        group_id='test',
        users=users
    )


@responses.activate
def test_invite_to_group(client, users):
    add_response(
        'POST',
        'community/groups/test/invite',
        json={'success': True}
    )

    assert client.invite_to_group(
        group_id='test',
        users=users
    )['success'] is True


@responses.activate
def test_user_items(client):
    add_response(
        'GET',
        'content/users/test',
        json={'total': 1}
    )

    assert client.user_items('test')['total'] == 1


@responses.activate
def test_group_items(client):
    add_response(
        'GET',
        'content/groups/test',
        json={'total': 1}
    )

    assert client.group_items('test')['total'] == 1


@responses.activate
def test_item_detail(client):
    add_response(
        'GET',
        'content/items/test',
        json={'id': 'test'}
    )

    assert client.item_detail('test')['id'] == 'test'


@responses.activate
def test_add_item(client):
    add_response(
        'POST',
        'content/users/test/addItem',
        json={'success': True}
    )

    assert client.add_item(
        username='test',
        title='my item',
        type='Web Mapping Application'
    )['success'] is True


@responses.activate
def test_share_item(client, groups):
    add_response(
        'POST',
        'content/items/test/share',
        json={'itemId': 'test'}
    )

    assert client.share_item('test', groups)['itemId'] == 'test'


@responses.activate
def test_server_error(client):
    add_response('GET', 'test', status=500)

    with pytest.raises(arcgis_sdk.ArcgisAPIError):
        client.request('test')


@responses.activate
def test_exception(client):
    add_response('GET', 'test', json={
        'error': {
            'code': 400,
            'details': [],
            'message': 'buh!'
        }
    })

    with pytest.raises(arcgis_sdk.ArcgisAPIError):
        client.request('test')

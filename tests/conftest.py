import arcgis_sdk
import pytest


@pytest.fixture(scope='module')
def client(request):
    return arcgis_sdk.ArcgisAPI('access_token')


@pytest.fixture(scope='module')
def users(request):
    return 'alice,bob'
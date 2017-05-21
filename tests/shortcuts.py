import arcgis_sdk
import json
import responses


def add_response(method, path, **kwargs):
    kwargs.setdefault('status', 200)

    if 'body' in kwargs:
        kwargs['body'] = json.dumps(kwargs['body'])

    responses.add(
        getattr(responses, method),
        arcgis_sdk.ARCGIS_API_URL + path,
        content_type='application/json',
        **kwargs
    )

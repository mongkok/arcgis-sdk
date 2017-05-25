import arcgis_sdk
import responses


def add_response(method, path, **kwargs):
    kwargs.setdefault('status', 200)
    kwargs.setdefault('content_type', 'application/json')

    responses.add(
        getattr(responses, method),
        arcgis_sdk.ARCGIS_API_URL + path,
        **kwargs
    )

from django.http import JsonResponse
from rest_framework.response import Response


class HttpCode(object):
    success = 200
    error = 400


# 原生的django的response
def resultHttpRequest(code=HttpCode.success, message='', data=None, kwargs=None):
    json_dict = {'data': data, 'code': code, 'message': message}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})


def successHttpRequest(data=None):
    return result(code=HttpCode.success, message='OK', data=data)


def errorHttpRequest(message='', data=None):
    return result(code=HttpCode.error, message=message, data=data)


# rest_framework的response
def result(code=HttpCode.success, message='', data=None, kwargs=None):
    json_dict = {'data': data, 'code': code, 'message': message}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return Response(json_dict, status=HttpCode.success)


def success(data=None):
    return result(code=HttpCode.success, message='OK', data=data)


def error(message='', data=None):
    return result(code=HttpCode.error, message=message, data=data)

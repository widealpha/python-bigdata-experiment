from django.http import HttpResponse
from group.models import get_relation
import json
import pymssql


# Create your views here.

def qq(request):
    try:
        qq_num = request.GET.get('qqNum')
        result = get_relation(qq_num=qq_num)
        if result is None:
            result = {}
        return HttpResponse(json.dumps(result))
    except pymssql.StandardError as e:
        print(e)
        return HttpResponse('服务器错误')
    except ValueError as e:
        print(e)
        return HttpResponse('数据不合法')


def qun(request):
    try:
        qun_num = request.GET.get('qunNum')
        result = get_relation(qun_num=qun_num)
        if result is None:
            result = {}
        return HttpResponse(json.dumps(result))
    except pymssql.StandardError as e:
        print(e)
        return HttpResponse('服务器错误')
    except ValueError as e:
        print(e)
        return HttpResponse('数据不合法')

from django.http import HttpResponse
import sys
import os
import pandas as pd

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath = os.path.split(rootPath)[0]
sys.path.append(rootPath + '\\contour_map')

from main import solve


# 垃圾python


# Create your views here.

def index(request):
    excel = pd.read_excel(rootPath + '\\contour_map\\data1.xlsx', header=None, nrows=874)
    source = request.GET.get('source')
    mode = request.GET.get('type')
    filename = solve(excel, mode)
    # filename = 'image_2_58.png'
    try:
        with open(filename, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')
    except IOError or Exception:
        return HttpResponse(500)

# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from social.models import RhsUsers


def search_people(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    address = request.GET.get('address')

    if name is None:
        name = '就是找不到这个名字'
    if email is None:
        email = '这个邮箱就是找不到的'
    if address is None:
        address = '这个地址是不可能找到的'
    limit = int(request.GET.get('limit'))
    page = int(request.GET.get('page'))
    rhs_users = RhsUsers.objects.filter(
        Q(use_real_name__contains=name) | Q(use_email__contains=email) | Q(use_address__contains=address)).values(
        'use_real_name', 'use_nation', 'use_email', 'use_astro', 'use_age', 'use_sex', 'use_address',
        'use_school', 'use_birthplace').distinct()
    info_list = []
    ptr = Paginator(rhs_users, limit)
    for i in ptr.page(page).object_list:
        info_list.append(i)
    # data = {'count': ptr.count, 'list': json.loads(serializers.serialize("json", ptr.page(page).object_list)), }
    data = {'count': ptr.count, 'list': info_list, }
    return JsonResponse(data)

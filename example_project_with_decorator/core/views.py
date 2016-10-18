from django.http import HttpResponse
from tasix.decorators import allow_tasix


@allow_tasix
def index_view(request):
    return HttpResponse('Only Tas-IX users can view this')

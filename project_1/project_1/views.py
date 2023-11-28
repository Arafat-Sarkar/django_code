
from django.http import HttpResponse

def Home (request):
    return HttpResponse("This is home page")

def contact (request):
    return HttpResponse("This is contact page")
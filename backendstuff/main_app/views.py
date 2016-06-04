from django.http import HttpResponse
from .models import Report



def index(request):
    return HttpResponse("we are alive!")

def report(request):
    all_reports = Report.objects.all()
    output = ', '.join(['_'.join([rep.lat,rep.lon]) for rep in all_reports])
    return HttpResponse(output)
from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('artwork_gallery/index.html')
    context = {}
    return HttpResponse(template.render(context, request), status=201)
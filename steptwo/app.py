from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms


class ImageForm(forms.Form):
    # Responsible for validate the placeholder image
    width  = forms.IntegerField(min_value=1, max_value=2000)
    height = forms.IntegerField(min_value=1, max_value=2000)


def placeholder(request, width, height):
    # Responsible for returning width and height passed as parameter
    form = ImageForm({'width': width, 'height': height})

    if not form.is_valid():
        return HttpResponseBadRequest('Invalid image request')

    template = '''
        <html>
            <body>
                <h1>Placeholder Image</h1>
                <ul>
                    <li>Width: {}</li>
                    <li>Height: {}</li>
                </ul>
            </body>
        </html>'''.format(width, height)

    return HttpResponse(template)

def index(request):
    return HttpResponse('Hey friend!')

# URLs
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)
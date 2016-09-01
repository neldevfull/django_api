import os
import hashlib
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.cache import cache
from django.views.decorators.http import etag
from django.shortcuts import render
from django.core.urlresolvers import reverse


class ImageForm(forms.Form):
    """Responsible for validate the placeholder image"""
    width  = forms.IntegerField(min_value=1, max_value=2000)
    height = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        width   = self.cleaned_data['width']
        height  = self.cleaned_data['height']
        key     = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)

        if content is None:
            image = Image.new('RGB', (width, height))
            draw  = ImageDraw.Draw(image)
            text  = '{} x {}'.format(width, height)

            textwidth, textheight = draw.textsize(text)

            if textwidth < width and textheight < height:
                texttop  = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))

            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)

        return content

def generate_etag(request, width, height):
    content = 'Placeholder: {} x {}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)
def placeholder(request, width, height):
    """Responsible for returning width and height passed as parameter"""
    form  = ImageForm({'width': width, 'height': height})

    if not form.is_valid():
        return HttpResponseBadRequest('Invalid image request')

    return HttpResponse(form.generate(), content_type='image/png')

def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height': 50})
    print(example)
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)

# URLs
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)
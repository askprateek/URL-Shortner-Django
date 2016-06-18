from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from random import choice
from models import Urldb
from .forms import UrlShortnerForm

# Create your views here.
char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#@csrf_protect
def index(request):
    if request.method =='GET':
        form = UrlShortnerForm()
        variables = RequestContext(request, { 'form':form })

        return render_to_response('short/index.html', variables)
    elif request.method == "POST":
        form = UrlShortnerForm(request.POST)
        if form.is_valid():
            url     = form.cleaned_data['weburl']
            custom  = form.cleaned_data['shortened_link']

            if len(custom)==0:
                shortened_link = ''.join(choice(char_set) for i in range(4))
            else:
                shortened_link = custom

            a = Urldb.objects.create(weburl = url, shortened_link = shortened_link)

            return render_to_response('short/index.html', {'shortened_link':shortened_link , 'given_url':url })
        else:
            form_error = form.errors #(form.weburl.error_messages, form.shortened_link.error_messages)
            form = UrlShortnerForm()
            variables = RequestContext(request, {'form':form , 'form_error' : form_error})
            return render_to_response('short/index.html', variables)


def redirect(request, server_hit_url):
    find_url = Urldb.objects.get(shortened_link = server_hit_url)
    return HttpResponseRedirect(find_url.weburl)

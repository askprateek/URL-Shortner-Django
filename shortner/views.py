from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from random import choice
from models import Urldb
# Create your views here.
#@csrf_protect
def index(request):
    if request.method =='GET':
        return render_to_response('short/index.html')
    elif request.method == "POST":
        url = request.POST['url']
        custom = request.POST['custom']
        if custom =="":
            char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            shortened_link = ''.join(choice(char_set) for i in range(4))
        else:
            shortened_link = custom

        a = Urldb.objects.create(weburl = url, shortened_link = shortened_link)

        return render_to_response('short/index.html', {'shortened_link':shortened_link , 'given_url':url})

def redirect(request, server_hit_url):
    find_url = Urldb.objects.get(shortened_link = server_hit_url)

    return HttpResponseRedirect(find_url.weburl)

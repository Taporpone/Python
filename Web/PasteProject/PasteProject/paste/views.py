from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {'boldmessage':'PasteProject'}
    return render(request,'paste/index.html',context_dict)

def about(request):
    context_dict = {'boldmessage':'About PasteProject'}
    return render(request,'paste/about.html',context_dict)

def handler404(request):
    response = render_to_response('404.html',{},context_instance=RequestContext(request))
    response.status_code = 404
    return response

@login_required
def profile(request):
    return render(request,'paste/profile.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/paste/')

@login_required
def mypastas(request):
    context_dict = {'boldmessage':'My Pastas'}
    return render(request,'paste/mypastas.html',context_dict)

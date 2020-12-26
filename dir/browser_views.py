from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from models import FileDownload
import os

CURRENT_VERSION = 0.9

def index(request):
    return render_to_response('index.htm')

def changelog(request):
    return render_to_response('changelog.htm')

#def screenshots(request):
#    return render_to_response('screenshots.htm')

#def manual(request):
#    return render_to_response('manual.htm')

def getfile(request, filename):
    try:
        record = FileDownload.objects.get(filename=filename, enabled=True)
        record.count = record.count + 1
        record.save()
    except:
        return render_to_response('index.htm')
    response = HttpResponse()
    response['X-Accel-Redirect'] = '/files/' + filename
    response['Content-Type'] = ""
    return response

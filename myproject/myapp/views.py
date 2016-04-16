# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            rfile = str(request.FILES['docfile'])
            extension = rfile[::-1][:rfile[::-1].find('.')][::-1]
            if extension == 'mp3':
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def delete(request, songId):
    song = Document.objects.get(pk=songId)
    song.delete()
    return HttpResponseRedirect(reverse('myproject.myapp.views.list'))

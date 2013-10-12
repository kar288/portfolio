from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from mimetypes import guess_type
from django.conf import settings

def home(request):
	return render(request, 'home.html', {})

def resume(request):
	print 
	with open(settings.MEDIA_ROOT + 'Resume.pdf', 'r') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
		response['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed

	
def get_photo(request, name):
	print name
	content_type = guess_type(name)
	return HttpResponse(name, mimetype=content_type)

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from datetime import datetime
from django.template.loader import render_to_string
import json

def home(request, template="bridal/index.html", context=None):
	return render_to_response(template, context)

def about(request, template="bridal/about.html", context=None):
	return render_to_response(template, context)

def gallery(request, template="bridal/gallery.html", context=None):
	return render_to_response(template, context)

def contact(request, template="bridal/contact.html", context=None):
	return render_to_response(template, context)

# return render_to_response("blog/index.html",RequestContext(request))
# def blog(request):
# 	if request.method == "POST":
# 		email= None
# 		try:
# 			email = request.POST.get("email")
# 		except:
# 			pass
			
# 		return render_to_response("blog/blog.html",{'email': email},RequestContext(request))

# 	return redirect("/login")

# @csrf_exempt
# @require_POST
# def submit(request):
# 	if request.method == "POST":
# 		blog = {}
# 		blog_item = request.POST.get("blog-item")
# 		blog['content'] = blog_item
# 		blog['date'] = str(datetime.now().date())
# 		data = {'data': blog}
# 		return HttpResponse(json.dumps(data))
# 	return HttpResponse('failed')
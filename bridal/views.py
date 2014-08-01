from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils.translation import ugettext as _
from bridal.models import Album

from datetime import datetime
import json


class ExtraContextTemplateView(TemplateView):
    """ Add extra context to a simple template view """
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context

    # this view is used in POST requests, e.g. signup when the form is not valid
    post = TemplateView.get


def home(request, template="bridal/index.html", context=None):
	return render_to_response(template, context)

def about(request, template="bridal/about.html", context=None):
	return render_to_response(template, context)
	
def contact(request, template="bridal/contact.html", context=None):
	return render_to_response(template, context)


class AlbumListView(ListView):
	""" List all albums in the gallery on the platform """
	context_object_name='album_list'
	page=1
	paginate_by=12
	template_name="bridal/album_list.html"
	extra_context=None

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(AlbumListView, self).get_context_data(**kwargs)
		try:
			page = int(self.request.GET.get('page', None))
		except (TypeError, ValueError):
			page = self.page

		if not self.extra_context: self.extra_context = dict()

		context['page'] = page
		context['paginate_by'] = self.paginate_by
		context['extra_context'] = self.extra_context
		return context
	
	def get_queryset(self):
		galleries = Album.objects.all()
		queryset = galleries
		return queryset

class AlbumDetailView(DetailView):
	""" List detail of selected album """
	model = Album
	context_object_name='album'
	template_name="bridal/album.html"
	extra_context=None

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(AlbumDetailView, self).get_context_data(**kwargs)

		if not self.extra_context: self.extra_context = dict()
		context['extra_context'] = self.extra_context
		return context
	


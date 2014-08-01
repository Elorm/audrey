from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from taggit.managers import TaggableManager
import datetime
import os
import uuid

def get_image_path(instance, filename):
    return os.path.join('gallery/%s/%s/'%(instance.album.title.lower(), instance.title), filename)

class Album(models.Model):
	title       = models.CharField(_('album title'), unique=True, null=False, blank=False, max_length=50)
	description = models.TextField(_('album description'), null=True, blank=True)
	pub_date    = models.DateTimeField(_('date created'), auto_now_add=True, default=datetime.date.today())
	mod_date    = models.DateTimeField(_('dated modified'), auto_now=True, default=datetime.date.today())
	slug        = models.SlugField(_('slug'), max_length=255, unique=True, default=datetime.date.today())
	tags        = TaggableManager(blank=True)
	
	class Meta:
		verbose_name        = _('Album')
		verbose_name_plural = _('Albums')
		ordering            = ["title", "pub_date"]

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Album, self).save(*args, **kwargs)


class Photo(models.Model):
	album           = models.ForeignKey(Album)
	title           = models.SlugField(_('photo title'), unique=True, null=True, blank=True, max_length=255)
	description     = models.CharField(_('photo description'), null=True, blank=True, max_length=255)
	pub_date        = models.DateTimeField(_('date created'), auto_now_add=True, default=datetime.date.today())
	mod_date        = models.DateTimeField(_('dated modified'), auto_now=True, default=datetime.date.today())
	photo           = models.ImageField(upload_to=get_image_path, blank=True, null=True, max_length=255)
	photo_thumbnail = ImageSpecField(source='photo', processors=[ResizeToFit(500, 500, None, None, 'c')], format='JPEG', options={'quality': 80})
	tags            = TaggableManager(blank=True)

	class Meta:
		verbose_name        = _('Photo')
		verbose_name_plural = _('Photos')	
		ordering            = ["title", "pub_date"]

	def __unicode__(self):
		return self.title

	def image_tag(self):
		return u'<img src="%s" width="100px" height="100px"/>' % self.photo.url
	image_tag.short_description = 'Photo'
	image_tag.allow_tags = True

	def save(self, *args, **kwargs):
		if not self.id:
			self.title = slugify(unicode(str(uuid.uuid4()), 'utf-8'))
		super(Photo, self).save(*args, **kwargs)


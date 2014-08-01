from django.contrib import admin
from bridal.models import Album, Photo

class PhotoInline(admin.StackedInline):
	model = Photo
	extra = 1
	exclude = ['title']
	readonly_fields = ('image_tag',)

class AlbumAdmin(admin.ModelAdmin):
	fieldsets = [
					('Album Title', {'fields': ['title']}),
					('Description', {'fields': ['description']}),
					('Tags', {'fields': ['tags']}),
					('Slug', {'fields': ['slug']}),
			    ]
	inlines = [PhotoInline]
	list_display = ['title', 'pub_date']

admin.site.register(Album, AlbumAdmin)

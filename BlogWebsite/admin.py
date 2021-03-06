from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Blogpost,Author,Category,Comment,Contact,Subscribe,Logo,Menu, FooterSocial

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_body',)

admin.site.register(Blogpost, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Menu)
admin.site.register(Logo)
admin.site.register(Subscribe)
admin.site.register(FooterSocial)
from .models import Blogpost, Category, Logo, Menu,Subscribe,FooterSocial
from django.shortcuts import redirect
import datetime
def fetchinbase(request):

	post = Blogpost.objects.all()
	get_post_by_time = datetime.date.today() - datetime.timedelta(days = 7)
	popular = Blogpost.objects.filter(posted_date__gte = get_post_by_time).order_by('-posted_date')

	data = {
	'popular': popular,
	'posts':post,
	'cat': Category.objects.all,
	'menu': Menu.objects.all,
	'logo': Logo.objects.get,
	'footersocial': FooterSocial.objects.all

	}
	return data
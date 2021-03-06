from django import forms
from .models import Blogpost
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CreatePostForm(forms.ModelForm):
	class Meta:
		model = Blogpost
		fields = "__all__"
		widgets = {
            'post_body': SummernoteWidget(),
        }


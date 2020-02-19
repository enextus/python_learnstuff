from django.contrib import admin
from .models import Question, Idea
admin.site.register(Question)
admin.site.register(Idea)

# https://docs.djangoproject.com/en/3.0/intro/tutorial01/
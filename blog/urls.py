from django.urls import path
from . import views
from django.conf.urls.i18n import set_language

urlpatterns = [
	path("", views.index, name="index"),
	path('i18n/set_language/', set_language, name='set_language'),
	path('blog/st', views.st, name='st'),
	path('blog/p', views.poems, name='poems')
]
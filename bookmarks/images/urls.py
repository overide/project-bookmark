from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^$',views.image_list,name="list"),
	
	url(r'^create/$',
		views.ImageCreateView.as_view(),
		name = "create"),

	url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
		views.ImageDetailView.as_view(),
		name = "detail"),

	url(r'^like/$',
		views.ImageLikeView.as_view(),
		name = "like"),
]
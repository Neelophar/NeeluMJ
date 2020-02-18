from django.conf.urls import url
from temp_app import views

# template tagging

app_name='temp_app'

urlpatterns =[

	url(r'^reletive/$', views.reletive , name='reletive'),
	url(r'^other/$',views.other,name='other'),
	

 
] 
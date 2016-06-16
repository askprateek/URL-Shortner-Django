from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<server_hit_url>\w+)' , views.redirect)

]

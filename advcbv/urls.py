from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from basic_app import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^basic_app/', include('basic_app.urls', namespace='basic_app')),

]

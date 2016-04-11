from django.conf.urls import url
import views

urlpatterns = [
    url(r'^book$', views.book_info, name='book_info'),
    url(r'^recommedation$', views.book_search, name='recommedation')
]

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^book/isbn/(?P<isbn>97[89](\d{10}))$', views.book_info, name='book_info'),
    url(r'^recommendation$', views.book_recommendation, name='recommendation'),
    url(r'^search$', views.book_search, name='search'),
]

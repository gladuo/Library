from django.conf.urls import url
import views

urlpatterns = [
    url(r'^book/(?P<id>\d+)$', views.book_id_info, name='book_id_info'),
    url(r'^book/isbn/(?P<isbn>97[89](\d{10}))$', views.book_isbn_info, name='book_isbn_info'),
    url(r'^tag/(?P<tag>\w+)$', views.tag_info),
    url(r'^recommendation$', views.book_recommendation, name='recommendation'),
    url(r'^search$', views.book_search, name='search'),
]

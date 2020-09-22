from django.conf.urls import url
from django.urls import path

from sanpham.views import *

app_name = 'sanpham'

urlpatterns = [
	url( r'^$', index, name = 'index' ),
	path("<int:id>", index_th, name = 'index_th' ),
	url( r'^search/$', search, name = 'search' ),
	path( 'search/<id>/', search_thuonghieu, name = 'search_th' ),
]

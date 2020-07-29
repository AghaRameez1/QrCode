from django.conf.urls import url

from webview.views.indexView import indexView, productAdd, logoutView, loginView, deleteView

urlpatterns = [
    url(r'^$', indexView.as_view(), name='index'),
    url('delete/(?P<id>\d+)/$', deleteView.as_view(),name='delete'),
    url('add/', productAdd.as_view(), name='productAdd'),
    url('login/', loginView.as_view(), name='login'),
    url('logout/', logoutView.as_view(), name='logout')
]

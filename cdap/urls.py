from django.conf.urls import url

from . import views

app_name = 'cdap'
urlpatterns = [
    #ListView
    url(r'^locaciones$', views.LocacionList.as_view(), name='locaciones'),
    url(r'^empresas$', views.EmpresaList.as_view(), name='empresas'),
    url(r'^personas$', views.PersonaList.as_view(), name='personas'),
    #DetailView
    url(r'^locacion/(?P<pk>[0-9]+)/$', views.LocacionDetail.as_view(), name='locacion'),
    url(r'^empresa/(?P<pk>[0-9]+)/$', views.EmpresaDetail.as_view(), name='empresa'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.PersonaDetail.as_view(), name='persona'),
]

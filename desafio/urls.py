from django.conf.urls import patterns, include, url
from django.views.generic import list, detail, edit
	
from django.contrib import admin
from django.conf import settings
from ordemVenda.models import OrdemDeVenda
from ordemVenda import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ordemVenda.views.cadastrarVenda'  ),

    # url(r'^blog/', include('blog.urls')),

    url(r'^consulta/$', list.ListView.as_view(model=OrdemDeVenda, context_object_name="ordens")),
    url(r'^consulta/(?P<pk>\d+)$', detail.DetailView.as_view(model=OrdemDeVenda)),
    url(r'^admin/', include(admin.site.urls))
)
#urlpatterns += patterns ('',(r'^static/(.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_URL)}),)

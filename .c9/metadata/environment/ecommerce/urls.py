{"filter":false,"title":"urls.py","tooltip":"/ecommerce/urls.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":15,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^accounts/', include(urls_accounts)),","]"],"id":2},{"start":{"row":15,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}],[{"start":{"row":15,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]",""],"id":3},{"start":{"row":15,"column":0},"end":{"row":31,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}],[{"start":{"row":15,"column":0},"end":{"row":31,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"],"id":4},{"start":{"row":15,"column":0},"end":{"row":33,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}]]},"ace":{"folds":[],"scrolltop":164.5,"scrollleft":0,"selection":{"start":{"row":18,"column":29},"end":{"row":18,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1590758502025,"hash":"98af1e2f49a26ce4b64cec2d0a79a54f1808cbbb"}
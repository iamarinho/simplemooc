#url raíz
from django.urls import include, re_path
from django.conf import settings
from django.contrib import admin
from simplemooc.core import url as core_url
from simplemooc.accounts import urls as acc_url
from simplemooc.courses import urls as course_url
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include(core_url, namespace = 'core')),
    re_path(r'^conta/', include(acc_url, namespace = 'accounts')),
    re_path(r'^cursos/', include(course_url, namespace = 'courses')),

]

pattern = r'^%s/(?P.*)$' % settings.STATIC_URL
urlpatterns += patterns('django.views.static',
    url(pattern, 'serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

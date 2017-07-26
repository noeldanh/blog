from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name="post_details"),
    # url(r'^create/$', views.post_create, name='post_create'),
    # url(r'^posts/(?P<post_id>[0-9]+)/edit/$', views.post_update, name='post_update'),
    # url(r'^posts/(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

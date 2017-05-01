from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #home page
    # url(r'^$','app.views.home'),
    # url(r'^home/$','app.views.home'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^home/$', TemplateView.as_view(template_name='index.html'), name='home'),

    #registration (redux)
	url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^list/$','app.views.charity_list'),
    url(r'^detail/(?P<pk>.+)/$', 'app.views.charity_detail'),

    url(r'^test/$', TemplateView.as_view(template_name='test.html'), name='test'),

    url(r'^contact/$', 'app.views.email_submission'),


]

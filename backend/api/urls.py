from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCompanyView, CreateContactView, DetailsCompanyView, DetailsContactView

urlpatterns = {
    url(r'^company/$', CreateCompanyView.as_view(), name="create"),
    url(r'^company/(?P<pk>[0-9]+)/$', DetailsCompanyView.as_view(), name="details"),
    url(r'^contacts/$', CreateContactView.as_view(), name="create"),
    url(r'^contacts/(?P<pk>[0-9]+)/$', DetailsContactView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
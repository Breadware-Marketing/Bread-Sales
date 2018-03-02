from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCompanyView, CreateContactView

urlpatterns = {
    url(r'^company/$', CreateCompanyView.as_view(), name="create"),
    url(r'^contacts/$', CreateContactView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
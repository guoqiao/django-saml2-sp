from django.conf.urls import url
from views import (
    descriptor,
    sso_idp_select,
    sso_response,
    sso_single_logout,
    sso_test,
)

urlpatterns = ['',
    url(r'^test/$', sso_test),
    url(r'^idpselect/$', sso_idp_select),
    url(r'^acs/$', sso_response),
    url(r'^singlelogout/$', sso_single_logout, name='sso_single_logout'),
    url(r'^metadata/', descriptor, name='spssodescriptor'),
]

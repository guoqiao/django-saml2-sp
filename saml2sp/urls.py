from django.conf.urls import url
from views import (
    descriptor,
    sso_idp_select,
    sso_response,
    sso_single_logout,
    sso_test,
)

urlpatterns = ['',
    (r'^test/$', sso_test),
    (r'^idpselect/$', sso_idp_select),
    (r'^acs/$', sso_response),
    url(r'^singlelogout/$', sso_single_logout, name='sso_single_logout'),
    url(r'^metadata/', descriptor, name='spssodescriptor'),
]

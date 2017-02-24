from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^Reg$', Reg, name = 'Reg'),
    url(r'^SignIn$', SignIn, name = 'SignIn'),
    url(r'^clear$', clear, name = 'clear'),
    url(r'^profile$', success, name = 'profile'),
    url(r'^quotes$', quotes, name = 'quotes')

]

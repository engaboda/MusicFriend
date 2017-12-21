from django.conf.urls import url , include
from . import views
urlpatterns = [
    #url(r'^$' , views.IndexView.as_view() , name='index' ),
    url(r'^$' , views.index , name='index' ),
    url(r'^createalbum/$' , views.creatView , name='createalbum' ),
    url(r'^detail/(?P<pk>[0-9]+)/$' , views.detail , name='detail' ),
    url(r'^favorite/$' , views.favorite , name="favorite"),
    url(r'^delete/(?P<pk>[0-9]+)/$' , views.deletealbum , name="delete"),
    url(r'^search/$' , views.searchview , name='search' ),
    url(r'^signup/$' , views.signup , name="signup"  ),
    #url(r'^reqister/$' , views.reqister , name="reqister"  ),
    url(r'^signin/$' , views.signin , name="signin" ),
    url(r'^signout/(?P<pk>[0-9]+)$' , views.signout , name="signout" ),
    url(r'^profile/$' , views.profile , name="profile" ),
    url(r'^add_song/(?P<pk>[0-9]+)/$'  , views.add_song , name='add_song'),

]

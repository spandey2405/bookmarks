from django.conf.urls import url
from src.api.v1.views.welcome import WelcomeView
from src.api.v1.views.loginview import LoginView
from src.api.v1.views.bookmarkspost import BookmarksView
from src.api.v1.views.bookmarksget import BookmarksGETView

urlpatterns  = [
     url(r'^v1/$', WelcomeView.as_view()),
     url(r'^v1/login/$', LoginView.as_view()),
     url(r'^v1/bookmarks/$', BookmarksView.as_view()),
     url(r'^v1/bookmarks/get/$', BookmarksGETView.as_view()),
     ]








from django.urls import path

from tweets.views import all_tweets

urlpatterns = [
    path("", all_tweets),
]
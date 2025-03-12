from django.shortcuts import render

from tweets.models import Tweet


def all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "tweets.html",
        {
            "tweets": tweets,
            "title": "All Tweets!"
        }
    )


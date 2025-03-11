from django.contrib import admin
from .models import Tweet, Like


class MuskFilter(admin.SimpleListFilter):
    title = "Filter by Musk"

    parameter_name = "musk"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Contain Elon Musk"),
            ("exclude", "Exclude Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        if word == 'contain':
            return tweets.filter(payload__contains="Elon Musk")
        if word == 'exclude':
            return tweets.exclude(payload__contains="Elon Musk")


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('payload', 'like_count')

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = 'Like Count'
    search_fields = ["payload", "user__username"]
    list_filter = [
        "created_at", MuskFilter
    ]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["created_at"]

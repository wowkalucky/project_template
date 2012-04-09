# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    public_profile_field = models.BooleanField(default=False)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


from tinymce import models as tinymce_models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    text = tinymce_models.HTMLField()
    short_description = models.CharField(max_length=255)
    sorting = models.PositiveSmallIntegerField("Sorting", blank=True, null=True)
    date = models.DateField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('sorting', )


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date', 'active', 'sorting', )
    list_editable = ('sorting', )

    class Media:
        js = (
            '/static/js/jquery-1.7.1.min.js',
            '/static/js/jquery-ui-1.8.18.custom.min.js',
        )

admin.site.register(BlogPost, BlogPostAdmin)

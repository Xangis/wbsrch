from django.db import models
from tagging.fields import TagField, Tag
import tagging

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class BlogPost(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    url = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField(null=False, blank=False, help_text='Use HTML. Include opening and closing <p> tags because they will not be in the template')
    post_time = models.DateTimeField(blank=True, auto_now_add=True)
    # Don't bother to tag with user.
    #user = models.ForeignKey(User)
    author = models.CharField(max_length=80, null=False, blank=False)
    tags = TagField()
    meta_description = models.CharField(max_length=250, null=True, blank=True)
    slug = models.TextField(null=True, blank=True)
    published = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def __unicode__(self):
        return self.title


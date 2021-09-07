from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django_extensions.db.models import TimeStampedModel
from taggit.managers import TaggableManager


# Create your models here.
class Question(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextUploadingField()
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("question:question-detail", kwargs={"slug": self.slug})

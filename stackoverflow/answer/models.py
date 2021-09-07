from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Answer(TimeStampedModel):
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE, related_name="answers")
    description = RichTextUploadingField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers")
    is_accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Answers'
        ordering = ['-created']

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse_lazy("question:question-detail", kwargs={"slug": self.question.slug})

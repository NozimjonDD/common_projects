from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from common import utils
from marks_projects.base_model import BaseModel


class LessonVideo(BaseModel):
    title = models.CharField(max_length=100, help_text="Dars nomi", unique=True)
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="videos")
    # content = CKEditor5Field(null=True, blank=True, help_text="Dars matni")
    video = models.FileField(upload_to='course/welcome/video/', null=True, blank=True, help_text="Dars video")
    time = models.CharField(max_length=4, help_text="minutes", default=10)
    image = models.ImageField(upload_to='course/welcome/images/', null=True, blank=True, help_text="Dars rasmi")
    is_read = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, default=utils.auto_generate_slug())

    def save(self, *args, **kwargs):
        # generate slug if it's not already set or if thee title changesdd
        if not self.slug or (self.pk and self.slug != slugify(self.title)):
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while LessonVideo.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{get_random_string(6)}"  # Add a random string for uniqueness
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

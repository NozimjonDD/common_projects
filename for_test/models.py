from django.db import models


# Create your models here.
from marks_projects.base_model import BaseModel


class RequestCheckingCreation(BaseModel):
    cross_id = models.PositiveIntegerField(blank=True, null=True)
    cross_setting_id = models.PositiveIntegerField(blank=True, null=True)
    cross_title = models.CharField(max_length=1000, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)

from django.db import models

# Create your models here.
from marks_projects.base_model import BaseModel


class RequestCheckingCreation(BaseModel):
    cross_id = models.PositiveIntegerField(blank=True, null=True)
    cross_setting_id = models.PositiveIntegerField(blank=True, null=True)
    cross_title = models.CharField(max_length=1000, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)


class Teacher(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)


class Student(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100)
    res = models.ManyToManyField(to=RequestCheckingCreation, related_name="res",
                                 blank=True, null=True)

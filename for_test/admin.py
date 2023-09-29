from django.contrib import admin

# Register your models here.
from for_test.models import *

"""examples"""

# class AttachModelInline(admin.TabularInline):
#     model = AttachMode
#     extra = 1
#     readonly_fields = ['creator', 'created_at', 'updated_at']
#
#
# @admin.register(ModelName)
# class ModelNameAdmin(admin.ModelAdmin):
#     def public_id(self, obj: ApplicationChronology):
#         return obj.application.public_id
#
#     def district_winner(self, obj: ApplicationChronology):
#         return obj.application.districtwinner_set.exists()
#
#     district_winner.boolean = True
#
#     list_select_related = [
#         'application',
#     ]
#     list_display = [
#         '__str__',
#         'application',
#         'public_id',
#         'district_winner',
#         'type',
#         'created_at',
#         'updated_at',
#     ]
#     list_display_links = ['__str__']
#     search_fields = ['id', 'application__public_id']
#     autocomplete_fields = ['application', 'creator']
#     list_filter = ['type']
#     inlines = [
#         AttachModelInline,
#     ]
"""--------------------------------------------"""


@admin.register(RequestCheckingCreation)
class RequestCheckingCreationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cross_id',
        'cross_setting_id',
        'cross_title',
        'data',
        'updated_at',
        'created_at',
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'course',
        'updated_at',
        'created_at',
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'teacher',
        'name',
        'course',
        'updated_at',
        'created_at',
    ]

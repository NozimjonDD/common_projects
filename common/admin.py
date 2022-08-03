from django.contrib import admin

# Register your models here.
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

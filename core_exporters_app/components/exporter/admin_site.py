""" Custom admin site for the Exporter model
"""
from django.contrib import admin


class CustomExporterAdmin(admin.ModelAdmin):
    """CustomExporterAdmin"""

    exclude = ["_cls", "url"]
    list_display = ["name", "enable_by_default"]
    search_fields = ["name"]

    def has_add_permission(self, request, obj=None):
        """Prevent from manually adding Exporters"""
        return False

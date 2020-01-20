from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ResrvationAdmin(admin.ModelAdmin):

    """ Reservtion Admin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)


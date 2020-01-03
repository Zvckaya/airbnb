from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ResrvationAdmin(admin.ModelAdmin):

    """ Reservtion Admin Definition"""

    pass

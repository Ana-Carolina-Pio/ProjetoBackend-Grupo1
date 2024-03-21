from django.contrib import admin


from chess.models import Time
# Register your models here.


class TimeAdmin(admin.ModelAdmin):
    list_display = ("nome", "color1", "color2", "branding")
    search_fields = ("nome",)


admin.site.register(Time, TimeAdmin)

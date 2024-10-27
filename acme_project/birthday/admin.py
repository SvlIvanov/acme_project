from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'last_name',
        'birthday',
    )
    search_fields = ('first_name', 'last_name',)
    list_display_links = ('first_name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)

from django.contrib import admin
from .models import Project
from django.utils.safestring import mark_safe

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')  # 一覧画面で表示するフィールド
    ordering = ('order',)  # 管理画面でもorder順で表示

    def formatted_description(self, obj):
        # 改行を <br> に変換して mark_safe で HTML として表示
        return mark_safe(obj.description.replace('\n', '<br><br>'))

    formatted_description.short_description = 'Description'

admin.site.register(Project, ProjectAdmin)


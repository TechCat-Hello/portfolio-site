from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')  # 一覧画面で表示するフィールド
    ordering = ('order',)  # 管理画面でもorder順で表示

admin.site.register(Project, ProjectAdmin)


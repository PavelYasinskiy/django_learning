from django.contrib import admin
from app_news.models import Comments, News


class CommentsInLine(admin.TabularInline):
    model = Comments

    def get_extra(self, request, obj=Comments, **kwargs):
        extra = 0
        return extra

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['username', 'short_comment', 'article']
    list_filter = ['username']
    list_display_links = ['short_comment']

    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(text_comment='Удалено администратором')

    delete_by_admin.short_description = "Удалить запрещенный комментарий"

    def short_comment(self, obj):
        result = lambda x: x[:15]+"..." if len(x) > 15 else x
        return result(obj.text_comment)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'public_date', 'edit_date', 'active_flag']
    list_filter = ['active_flag']
    list_editable = ['active_flag']
    inlines = [CommentsInLine]
    get_max_num = 0

    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(active_flag=True)

    def deactivate(self, request, queryset):
        queryset.update(active_flag=False)

    activate.short_description = "Перевести в статус Активно"
    deactivate.short_description = "Перевести в статус Неактивно"


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)



# добавьте возможность просматривать и редактировать комментарии к новости с помощью TabularInline
# добавьте 2 действия для массового перевода новостей: в статус “активно” и статус “неактивно”
# добавьте действие для комментариев, которое будет проставлять текст выбранным комментариям “Удалено администратором”.
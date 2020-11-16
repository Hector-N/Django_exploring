from django.contrib import admin

from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    fieldsets = [('fieldset1', {'fields': ['headline', 'date']}),
                 ('fieldset2', {'fields': ['tags', 'text']})]
    list_display = ['pk', 'headline']
    list_filter = ['date']
    search_fields = ['text']

    # fields = ['headline', 'text', 'date', 'tags']


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ['date', 'text', 'post']
    list_filter = ['date', 'author', 'post']

admin.site.register(Comment, CommentAdmin)



admin.site.register(Tag)

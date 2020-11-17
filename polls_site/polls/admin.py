from django.contrib import admin

from .models import Question, Option


# class OptionInline(admin.StackedInline):
class OptionInline(admin.TabularInline):
    model = Option
    extra = 3


class OptionAdmin(admin.ModelAdmin):
    # fields
    # fieldsets
    list_display = ['text', 'question_id', 'votes']
    list_filter = ['question_id', 'votes']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'date']
    list_filter = ['date']
    search_fields = ['text']
    inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)

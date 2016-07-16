from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
  field = ['pub_date', 'question_text'] 
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
  field = ['choice', 'votes'] 
  list_display = ('question','choice','votes')
  list_filter = ['votes']
  search_fields = ['choice']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
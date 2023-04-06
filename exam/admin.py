from django.contrib import admin

from exam.models import Result, Course, Question
# Register your models here.

admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Result)

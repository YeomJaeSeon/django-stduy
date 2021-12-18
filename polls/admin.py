from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# 내가 만든 모델을 어드민에 추가하는 코드
admin.site.register(Question)
admin.site.register(Choice)

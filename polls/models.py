import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

    # shell에서 Question.objects.all()하면 어떤 데이터인지 한눈에 보기 어려워서 해당 메서드를 추가함 (java의 toString 오버라이딩하는 것과 같은듯)
    # shell이 아니더라도 해당 row데이터가 뭔지 식별하기 쉬워진다!
    def __str__(self):
        return self.question_text

    # 필요한 메서드도 이렇게 추가할 수 있다.
    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
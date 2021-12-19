from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from manage_team.models import Team


class Member(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(7), MaxValueValidator(19)])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "MEMBER"

    def __str__(self):
        return self.name
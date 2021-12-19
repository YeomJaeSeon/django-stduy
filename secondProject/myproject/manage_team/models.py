from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "TEAM"

    def __str__(self):
        return self.name
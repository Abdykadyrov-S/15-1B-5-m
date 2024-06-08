from django.db import models

from apps.team.models import Team

# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(
        Team, on_delete=models.CASCADE,
        verbose_name="Сотрудник", related_name="team_service"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок услуги"
    )
    description = models.TextField(
        verbose_name="Описание услуги"
    )
    image = models.ImageField(
        upload_to="news/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"услуга {self.title} от {self.user}"
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

        
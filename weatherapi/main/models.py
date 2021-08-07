from django.db import models

# Create your models here.
DESCRIPTIONS = (
    (0,'Quyosh'),
    (1,"Yomg'ir"),
    (2,"Bulut"),
    (3,"Qor"),
)
class Description(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)
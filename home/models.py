from django.db import models

class MetaDatos(models.Model):
	title = models.CharField(max_length=50)
	logo = models.ImageField(upload_to = "Logo")
	title_banner = models.CharField(max_length=50)
	number = models.IntegerField(default = 0)




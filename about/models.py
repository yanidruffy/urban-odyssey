from django.db import models

# Create your models here.

class About(models.Model):
	title=models.CharField(max_length=100)
	mission=models.TextField(default="Our mission is to empower digital nomads and adventurers with stylish, durable, and minimalist products.")
	history=models.TextField(default="Founded with the goal of redefining urban mobility, we partner with leading brands to deliver innovative solutions.")
	vision=models.TextField(default="To become the go-to platform for digital nomads seeking premium everyday carry solutions.")
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "About Section"
		verbose_name_plural = "About Section"

	def __str__(self):
		return self.title

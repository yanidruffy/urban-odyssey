from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	read = models.BooleanField(default=False)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name} - {self.subject}"

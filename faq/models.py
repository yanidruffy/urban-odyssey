from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["question"]

    def __str__(self):
        return self.question

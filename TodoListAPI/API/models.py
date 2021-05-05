from django.db import models

class Todo(models.Model):
    """A Todo Instance"""
    title = models.CharField(max_length=255, default='')
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
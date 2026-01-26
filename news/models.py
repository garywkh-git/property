from django.db import models

from salespersons.models import Salesperson

class News(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news/')
    description = models.TextField()
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
        # ADD THIS to fix admin display name
    class Meta:
        verbose_name = 'News Article'  # Singular name
        verbose_name_plural = 'News Articles'  # Plural name (same as singular)s
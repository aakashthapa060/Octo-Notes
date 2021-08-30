from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=100)
    pub_date = models.DateField(default= timezone.now, blank=True)
    
    def __str__(self):
        return f"{self.title} // {self.user}"
    
    class Meta:
        ordering = ["pub_date"]
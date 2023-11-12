from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import uuid

class Hotel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=100)    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.hotel)
    
    class Meta:
        unique_together = (('hotel', 'user'),)
        index_together = (('hotel', 'user'),)
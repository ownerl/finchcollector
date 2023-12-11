from django.db import models
from django.urls import reverse
from django.utils import timezone

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=231)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    favourite_anime = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    date = models.DateField('feeding time')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    def is_fed(self):
        now = timezone.now().date()
        twenty_four_hours_ago = now - timezone.timedelta(days=1)
        
        return twenty_four_hours_ago <= self.date

    class Meta:
        ordering = ['-date']
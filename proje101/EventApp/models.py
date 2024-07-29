from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    registered_count = models.IntegerField(default=0)


    def register(self):
        if self.registered_count < self.capacity:
            self.registered_count += 1
            self.save()
            return True
        return False
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default="0000000000")
    birth_date = models.DateField()
    gender_choices = [('B', 'Bay'), ('K', 'Bayan')]
    gender = models.CharField(max_length=1, choices=gender_choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event', 'email'], name='unique_event_email')
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event.name}"
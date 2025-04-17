from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

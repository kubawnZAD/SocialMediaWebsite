from django.db import models
from django.contrib.auth.models import User #defaultowa pole userów
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #pobiera czas za każdym razem kiedy zapiszemy 
    created = models.DateTimeField(auto_now_add=True) #pobiera czas tylko za pierwszym razem

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE) #relacja jeden do wielu. Kiedy usuniemy pokój wszystkie wiadomości zostają usunięte
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #pobiera czas za każdym razem kiedy zapiszemy 
    created = models.DateTimeField(auto_now_add=True) #pobiera czas tylko za pierwszym razem


    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.body[0:50] #pokazuje znaki wiadomosci w body od 0 do 50 
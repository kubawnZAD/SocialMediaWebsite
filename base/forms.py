from django.forms import ModelForm
from .models import Room


#tworzy formularz zawierający inputy z atrybutów okreslonych w tabeli przchowywanej w zminnej model 
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host','participants']
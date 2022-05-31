from django import forms
from .models import GENRE_CHOICES, CD


class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(required=False, widget=forms.Textarea)


    def clean_artist(self):
        artist_list = []
        data_BD = CD.objects.all()
        for artist in data_BD:
            artist_list.append(artist.artist)
        data = self.cleaned_data['artist']
        data = 'Мы не продаем диски данного исполнителя ' + data
        if data not in artist_list:
            raise forms.ValidationError(data)
        return data

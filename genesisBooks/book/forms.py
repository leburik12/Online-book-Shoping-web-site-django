from django import forms
from .models import Books


class SearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('arts & hilosophy', 'Arts'),
        ('biographies & memories', 'Biographies & Memories'),
        ('business & Money', 'Business & Money'),
        ('calendar', 'Calendar'),
        ('children books', 'Children\'s Books'),
        ('christian books & Bibles', 'Christian Books & Bibles'),
        ('comics & graphic novels', 'Comics & Graphic Novels'),
        ('computer & technology', 'Computer & Technology'),
        ('Cookbooks, Food & Wine', 'Cookbooks, Food & Wine'),
        ('History', 'History'),
        ('Law', 'Law'),
        ('Literature & Fiction', 'Literature & Fiction'),
        ('Medical Books', 'Medical Books'),
        ('Romance', 'Romance'),
        ('Science & Math', 'Science & Math'),
        ('Sport & Outdoors', 'Sport & Outdoors'),
        ('Test preparation', 'Test preparation'),
    ]
    category = forms.ChoiceField(widget=forms.Select,
                                 choices=CATEGORY_CHOICES)
    search_query = forms.CharField(widget=forms.TextInput,
                                   max_length=200)



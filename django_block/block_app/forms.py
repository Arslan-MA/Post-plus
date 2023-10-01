from block_app.models import Post
from django import forms


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'date_posted']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'content': forms.Textarea(attrs={'class': 'content'})
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Текст'
        }

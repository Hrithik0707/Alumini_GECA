from django.forms import ModelForm
from .models import Posts
class Postform(ModelForm):
    class Meta:
        model = Posts
        fields = ('title','content',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Title of your Blog'})
        self.fields['content'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Content of your Blog'})
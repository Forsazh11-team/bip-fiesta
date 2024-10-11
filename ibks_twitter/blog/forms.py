from django import forms
from .models import Tweet, Comment


class TweetForm(forms.ModelForm):
    hashtags = forms.CharField(widget=forms.Textarea, max_length=100, required=False, help_text="Введите хэштеги через запятую")

    class Meta:
        model = Tweet
        fields = ['content', 'hashtags']

    def clean_hashtags(self):
        hashtags_data = self.cleaned_data['hashtags']
        hashtags_list = [tag.strip() for tag in hashtags_data.split(',') if tag.strip()]
        return hashtags_list


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

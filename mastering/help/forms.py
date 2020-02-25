from django import forms
from .models import Topic, Comment


class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'topic_text']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text',]
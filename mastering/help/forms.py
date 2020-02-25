from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'topic_text']
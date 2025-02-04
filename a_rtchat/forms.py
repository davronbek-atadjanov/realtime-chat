from django.forms import ModelForm
from django.forms import TextInput
from .models import GroupMessage

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': TextInput(attrs={'placeholder':'Add message...', 'class': 'p-4 text-black', 'maxlength':'300', 'autofocus': True}),
        }
from django.db import models
from user_app.models import Profile


class ChatGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Profile, blank=True)
    is_personal_chat = models.BooleanField(default=False) # Чи є цей чат особистим

    def __str__(self):
        return f'Група "{self.name}" '
    

class ChatMessage(models.Model):
    content = models.TextField(max_length=4096)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Повідомлення від {self.author}. Відправлено {self.sent_at} '

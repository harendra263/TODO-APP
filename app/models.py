from django.db import models
from django.contrib.auth.models import User



class TODO(models.Model):
    STATUS_CHOICES = [
        ("C", "Completed"),
        ("P", "Pending")
    ]

    PRIORITY_CHOICES = [
        ("1", "1️⃣"),
        ("2", "2️⃣"),
        ("3", "3️⃣"),
        ("4", "4️⃣"),
        ("5", "5️⃣"),
        ("6", "6️⃣"),
        ("7", "7️⃣"),
        ("8", "8️⃣"),
        ("9", "9️⃣"),
        ("10", "🔟")
    ]
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices = PRIORITY_CHOICES)

    def __str__(self):
        return self.title

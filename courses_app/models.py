from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()   #تکست فیلد تفاوتش با بالایی اینه که کاراکتر بیشتری داخلش میشه نوشت
    situation = models.BooleanField(default=True)
    views = models.IntegerField(null=True)

    def __str__(self):
        return self.title

#def __str__(self):
#    return f"{self.title} - {self.description[:40]}"

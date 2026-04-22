from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()   #تکست فیلد تفاوتش با بالایی اینه که کاراکتر بیشتری داخلش میشه نوشت
    situation = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(null=True, upload_to='Test_1_media')

    def __str__(self):
        return self.title

#def __str__(self):
#    return f"{self.title} - {self.description[:40]}"

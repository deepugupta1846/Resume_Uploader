from django.db import models

STATE_CHOICE = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh')
)


class Resume(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(max_length=100, choices=STATE_CHOICE)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.dob}-{self.gender}-{self.locality}-{self.city},{self.pin}-{self.state}-{self.mobile}" \
               f"{self.email}-{self.job_city}-{self.profile_image}-{self.my_file}"




# Create your models here.

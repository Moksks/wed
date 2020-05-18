from django.db import models

class Fitting_order(models.Model):
    fit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    fit_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    email = models.EmailField()
    comment = models.TextField  (max_length=500)

    def  __str__(self):
        return "%s %s" % (self.name, self.phone)
from django.db import models

class Farmer(models.Model):
  farmer_idx = models.IntegerField(max_length=6)
  farmer_id = models.CharField(max_length=10)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  alias = models.CharField(max_length=30)
  res_address = models.CharField(max_length=100)
  tel_number = models.CharField(max_length=20)
  cell_number = models.CharField(max_length=20)
  verified_status = models.BooleanField(default=False)
  dob = models.CharField(auto_now=False, auto_now_add=False)
  reg_date = models.CharField(auto_now=False, auto_now_add=False)
  agri_activity = models.CharField(max_length=30)

  class Meta:
    ordering = ('reg_date',)


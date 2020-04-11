# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


'''
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'ifsc', 'TEXT', 0, None, 0)
(2, 'bank_id', 'INTEGER', 0, None, 0)
(3, 'branch', 'TEXT', 0, None, 0)
(4, 'address', 'TEXT', 0, None, 0)
(5, 'city', 'TEXT', 0, None, 0)
(6, 'district', 'TEXT', 0, None, 0)
(7, 'state', 'TEXT', 0, None, 0)
(8, 'bank_name', 'TEXT', 0, None, 0)
'''


class Bank_Details(models.Model):
    # index = models.IntegerField(primary_key=True)
    ifsc = models.TextField(primary_key=True)
    bank_id = models.IntegerField(blank=True, null=True)
    branch = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    bank_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_details'






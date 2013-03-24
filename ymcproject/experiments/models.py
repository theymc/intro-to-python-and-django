from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class LcboProduct(models.Model):
    name = models.CharField(max_length=200)
    price_in_cents = models.IntegerField(default=0, null=True)
    primary_category = models.CharField(max_length=100, null=True)
    secondary_category = models.CharField(max_length=100, null=True)
    package_unit_type = models.CharField(max_length=20, null=True)
    package_unit_volume_in_milliliters = models.IntegerField(default=0, null=True)
    total_package_units = models.IntegerField(default=0, null=True)
    volume_in_milliliters = models.IntegerField(default=0, null=True)
    alcohol_content = models.IntegerField(default=0, null=True)
    price_per_liter_of_alcohol_in_cents = models.IntegerField(null=False)
    price_per_liter_in_cents = models.IntegerField(default=0, null=True)
    producer_name = models.CharField(max_length=255, null=True)
    image_thumb_url = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255, null=True)
    is_discontinued = models.BooleanField()
    is_dead = models.BooleanField()
    limited_time_offer_ends_on = models.CharField(max_length=255, null=True)
    tasting_note = models.CharField(max_length=400, null=True)
    description = models.CharField(max_length=400, null=True)
    origin = models.CharField(max_length=255, null=True)
    product_no = models.IntegerField()

from django.contrib import admin
from cashflex.benefits.models import Benefit, BenefitPrice

# Register your models here.
admin.site.register(Benefit)
admin.site.register(BenefitPrice)

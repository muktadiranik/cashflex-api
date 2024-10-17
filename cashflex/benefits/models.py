from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _



class Benefit(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Benefit')
        verbose_name_plural = _('Benefits')

    def __str__(self):
        return self.name


class BenefitPrice(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_('Group'), blank=True, null=True)
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, verbose_name=_('Benefit'), blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'), blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Sub total'), blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name=_('Total amount'), blank=True, null=True)

    class Meta:
        verbose_name = _('Benefit price')
        verbose_name_plural = _('Benefit prices')

    def __str__(self):
        return self.benefit.name

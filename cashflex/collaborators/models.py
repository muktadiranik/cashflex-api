from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class CollaboratorAccount(models.Model):
    collaborator = models.ForeignKey(User, on_delete=models.CASCADE,
                                     verbose_name=_('Collaborator'), blank=True, null=True)
    budget_balance = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name=_('Budget balance'), blank=True, null=True)
    cost_balance = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name=_('Cost balance'), blank=True, null=True)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name=_('Cash balance'), blank=True, null=True)
    withdraw = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Withdraw'), blank=True, null=True)
    donation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Donation'), blank=True, null=True)

    class Meta:
        verbose_name = _('Collaborator account')
        verbose_name_plural = _('Collaborator accounts')

    def __str__(self):
        return self.collaborator.email


class CollaboratorPayment(models.Model):
    collaborator = models.ForeignKey(User, on_delete=models.CASCADE,
                                     verbose_name=_('Collaborator'), blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', verbose_name=_('QR code'), blank=True, null=True)

    class Meta:
        verbose_name = _('Collaborator payment')
        verbose_name_plural = _('Collaborator payments')

    def __str__(self):
        return self.collaborator.email


class CollaboratorPaymentDetails(models.Model):
    collaborator_payment = models.ForeignKey(CollaboratorPayment, on_delete=models.CASCADE,
                                             verbose_name=_('Collaborator payment'), blank=True, null=True)
    #
    # ongoing
    #
    #
    #
    #
    #
    # completed

    class Meta:
        verbose_name = _('Collaborator payment details')
        verbose_name_plural = _('Collaborator payment details')

    def __str__(self):
        return self.collaborator_payment.collaborator.email

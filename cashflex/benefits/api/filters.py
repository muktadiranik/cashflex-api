from django_filters import *
from cashflex.benefits.models import Benefit, BenefitPrice


class BenefitFilter(FilterSet):
    class Meta:
        model = Benefit
        fields = {
            'id': ['exact'],
            'name': ['exact'],
            'description': ['exact'],
        }


class BenefitPriceFilter(FilterSet):
    class Meta:
        model = BenefitPrice
        fields = {
            'id': ['exact'],
            'group_id': ['exact'],
            'benefit_id': ['exact'],
            'amount': ['exact'],
            'sub_total': ['exact'],
            'total_amount': ['exact'],
        }

from django_filters import *
from django_filters.rest_framework import FilterSet
from cashflex.core.models import *




class PartnerFilter(FilterSet):
    class Meta:
        model = Partner
        fields = {
            'id': ['exact'],
            'name': ['exact'],
            'is_active': ['exact'],
            'website': ['exact'],

        }


class FAQCategoryFilter(FilterSet):
    class Meta:
        model = FAQCategory
        fields = {
            'id': ['exact'],
            'name': ['exact'],

        }


class FAQFilter(FilterSet):
    class Meta:
        model = FAQ
        fields = {
            'id': ['exact'],
            'category': ['exact'],

        }


class TrainingTypeFilter(FilterSet):
    class Meta:
        model = TrainingType
        fields = {
            'id': ['exact'],
            'name': ['exact'],

        }


class TrainingFilter(FilterSet):
    class Meta:
        model = Training
        fields = {
            'id': ['exact'],
            'title': ['exact'],
            'is_active': ['exact'],

        }

class SocialMediaFilter(FilterSet):
    class Meta:
        model = SocialMedia
        fields = {
            'id': ['exact'],
            'platform': ['exact'],
        
        }
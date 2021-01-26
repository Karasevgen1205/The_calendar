from django.shortcuts import render
from django_filters.rest_framework import FilterSet, RangeFilter, BaseInFilter, CharFilter

from app_calendar.models import Country


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass

class CountryFilter(FilterSet):
    name = CharFilterInFilter(field_name='country__name', lookup_expr='in')
    id = RangeFilter()

    class Meta:
        model = Country
        fields = ['id', 'name']

import graphene
from graphene_django.types import DjangoObjectType
from .models import Country, City

class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class CityType(DjangoObjectType):
    class Meta:
        model = City

class Query(graphene.ObjectType):
    all_countries = graphene.List(CountryType)
    country_by_name = graphene.Field(CountryType, name=graphene.String())

    def resolve_all_countries(self, info):
        return Country.objects.all()

    def resolve_country_by_name(self, info, name):
        return Country.objects.get(name=name)

schema = graphene.Schema(query=Query)
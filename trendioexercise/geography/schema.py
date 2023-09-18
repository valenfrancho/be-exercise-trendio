import graphene
from graphene_django.types import DjangoObjectType
from .models import Country, City

# Defining GraphQL types:

class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class CityType(DjangoObjectType):
    class Meta:
        model = City

# Defining query type:

class Query(graphene.ObjectType):
    all_countries = graphene.List(CountryType)
    country_by_name = graphene.Field(CountryType, name=graphene.String())

    def resolve_all_countries(self, info):
        return Country.objects.all()

    def resolve_country_by_name(self, info, name):
        return Country.objects.filter(name=name).first()
    
# Defining input types:
    
class CreateCountryInput(graphene.InputObjectType):
    name = graphene.String(required=True)

class CreateCityInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    country_id = graphene.ID(required=True)

# Implementing resolver functions:

class CreateCountry(graphene.Mutation):
    class Arguments:
        input = CreateCountryInput(required=True)

    country = graphene.Field(CountryType)

    def mutate(self, info, input):
        name = input.get('name')
        country = Country(name=name)
        country.save()
        return CreateCountry(country=country)

class CreateCity(graphene.Mutation):
    class Arguments:
        input = CreateCityInput(required=True)

    city = graphene.Field(CityType)

    def mutate(self, info, input):
        name = input.get('name')
        country_id = input.get('country_id')
        country = Country.objects.get(pk=country_id)
        city = City(name=name, country=country)
        city.save()
        return CreateCity(city=city)
    
# Defining mutations:

class Mutation(graphene.ObjectType):
    create_country = CreateCountry.Field()
    create_city = CreateCity.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
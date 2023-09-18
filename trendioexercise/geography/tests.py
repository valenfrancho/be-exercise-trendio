from django.test import TestCase
from .models import Country, City

class ModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")
        self.city = City.objects.create(name="Test City", country=self.country)


    # Check if model instances can be created successfully:

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Test Country")

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")


    # Retrieve instances from the db and verify their attributes:

    def test_country_retrieval(self):
        retrieved_country = Country.objects.get(id=self.country.id)
        self.assertEqual(retrieved_country.name, "Test Country")

    def test_city_retrieval(self):
        retrieved_city = City.objects.get(id=self.city.id)
        self.assertEqual(retrieved_city.name, "Test City")


    # Check if instances can be updated and that changes are reflected in the db:

    def test_country_update(self):
        updated_country = Country.objects.get(id=self.country.id)
        updated_country.name = "Updated Country"
        updated_country.save()
        self.assertEqual(updated_country.name, "Updated Country")

    def test_city_update(self):
        updated_city = City.objects.get(id=self.city.id)
        updated_city.name = "Updated City"
        updated_city.save()
        self.assertEqual(updated_city.name, "Updated City")


    # Test model deletion:

    def test_country_deletion(self):
        deleted_country = Country.objects.get(id=self.country.id)
        deleted_country.delete()
        with self.assertRaises(Country.DoesNotExist):
            Country.objects.get(id=self.country.id)

    def test_city_deletion(self):
        deleted_city = City.objects.get(id=self.city.id)
        deleted_city.delete()
        with self.assertRaises(City.DoesNotExist):
            City.objects.get(id=self.city.id)
            

    # Test model relationships:

    def test_city_country_relationship(self):
        country_of_city = self.city.country
        self.assertEqual(country_of_city, self.country)
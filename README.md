# Backend Exercise for Trendio

## Project Description

This project is a simple Django-based GraphQL API that manages information about countries and cities, developed to evaluate backend development skills.

## Requirements
- Python 3.x
- Django 3.x
- GraphQL
- SQLite

## Installation
1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server `python manage.py runserver`.

## Project Structure
- `trendioexercise/` - Django project settings and configuration.
- `geography/` - Main app, containing: models, GraphQL schemas, and views.

## API Usage
To interact with the GraphQL API, use the endpoint `/graphql`.
- Here's an example query to get a list of all countries and their cities:

```graphql
query {
  allCountries {
    id
    name
    citySet {
      id
      name
    }
  }
}
```

- The query can be filtered by country name:

```graphql
query {
  countryByName(name: "YourCountryName") {
    id
    name
  }
}
```

- And new countries
```graphql
mutation {
  createCountry(input: { name: "YourCountryName" }) {
    country {
      id
      name
    }
  }
}
```
or cities can be added:
```graphql
mutation {
  createCity(input: { name: "YourCityName", countryId: 1 }) {
    city {
      id
      name
      country {
        id
        name
      }
    }
  }
}
```
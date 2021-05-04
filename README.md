# PyOli

Booking and order manager for the restaurant **Pa i oli**.

- Clients can book a table or order food.
- Restaurant administrators can add food to deliver, tables in the restaraunt and manage pending orders and table
  bookings.
  
## Run locally
```bash
python3 manage.py runserver
```

Admin test user:
- user: alex
- pass: alex

## Docker run
If you want to run with docker compose, switch to branch [deliver1-docker](https://github.com/SergiGirabet/PyOli/tree/deliver1-docker)
and execute:
```bash
docker-compose up -d
```
## Other

Google Maps API:
- We plan to use GOOGLE MAPS API for the class 'Address'.
    - Note that: A key is personal and private, each member needs to have their own secret key. Such keys can be hidden from the
      code in several ways, we have decided that in order to everyone has the same environment we will all have the API
      key stored as an environment variable in our system. So, you must define an environment variable in your system with the name GOOGLE_API_KEY to get it to work.

## Agile Behaviour Driven Development (BDD)
Now, we have the initial Django project and application that we will start filling with functionality.

The aim of this application is to let users book a table or order products of the restaurant.

Consequently, and following a BDD approach, first we define the intended features:

- Register new Product
  
*new_product.feature*

**In order to** [achieve some business value],

**As a** [stakeholder type],

**I want** [some new system feature].

- Register new Order
- Register new Booking

**More features coming soon**

Afterwards we have set in the directory *features* the environment to work with the browser.

In the *features* directory we have also created the *steps* directory where we will write the code to execute the features.

For example, in the *authentication.py* we can use the steps to login users with any username and password, as long as we have previously created them, and the password matches.

To support this behaviour, we first link the login, and also logout, views from django.contrib.auth.views in the project urls file, pyoli/urls.py:




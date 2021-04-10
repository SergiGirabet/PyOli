# PyOli

Booking and order manager for the restaurant **Pa i oli**.

- Clients can book a table or order food.
- Restaurant administrators can add food to deliver, tables in the restaraunt and manage pending orders and table
  bookings.

## Docker run
If you want to run with docker compose, switch to branch [deliver1-docker](https://github.com/SergiGirabet/PyOli/tree/deliver1-docker)
and execute:
```bash
docker-compose up -d
```

If you want to create a superuser:
```bash
docker-compose run app python3 manage.py createsuperuser
```

To apply booking_manager migrations
```bash
docker-compose run app python3 manage.py makemigrations booking_manager
docker-compose run app python3 manage.py migrate booking_manager
```

## Other

Google Maps API:
- We plan to use GOOGLE MAPS API for the class 'Address'.
    - Note that: A key is personal and private, each member needs to have their own secret key. Such keys can be hidden from the
      code in several ways, we have decided that in order to everyone has the same environment we will all have the API
      key stored as an environment variable in our system. So, you must define an environment variable in your system with the name GOOGLE_API_KEY to get it to work.

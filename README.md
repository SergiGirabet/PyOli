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

- user: admin
- pass: admin

There are some restaurant tables, food categories and food added to the database.

## Google Maps API
When a user places an order in the 'Delivery' page, we make a request to the Google Maps distance matrix API, so you
will need the API KEY (otherwise a default time is set: 10 minutes). **The API KEY can be found in the Deliverable 2 report.**
Once an order is placed, it's possible to check the estimated hour the delivery will get into your home.

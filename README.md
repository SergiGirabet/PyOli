# PyOli

Booking and order manager for the restaurant **Pa i oli**.

- Clients can book a table or order food.
- Restaurant administrators can add food to deliver, tables in the restaraunt and manage pending orders and table
  bookings.

## Run locally

```bash
export API_KEY=AIzaSyA0aRqXdWjSyZ5rllDPxKsX0oNG4Cnud8Y
python3 manage.py runserver
```

Admin test user:

- user: admin
- pass: admin

There are some restaurant tables, food categories and food added to the database.

When a user places an order in the 'Delivery' page, we make a request to the Google Maps distance matrix API, so you
will need the API KEY (otherwise a default time is set: 10 minutes).

Once an order is placed, it's possible to check the estimated hour the delivery will get into your home. The restaurant
is located in 'C/ de Jaume II, 69, 25001 Lleida'.

The estimated time is calculated as 20 minutes for preparation and D minutes for shipping, where D is the GMAPS response.
To modify: 
- UML add to Product model "Description" field.
- Modify "Reserve" field to "Reserved"

Classes fetes:
- Booking
- Table
- Order (using GOOGLE MAPS API)


API:

- We have used a GOOGLE MAPS API in the field 'address' of the Order class. 

    - Note that:
A key is personal and private, each member needs to have their own secret key.
Such keys can be hidden from the code in several ways, we have decided that in order to everyone has the same environment we will all have the API key stored as an environment variable in our system.

You must define an environment variable in your system with the name GOOGLE_API_KEY to get it to work.

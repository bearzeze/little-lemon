SUPERUSER:
username - admin_django
password - employee@123!

USER:
username - berks
password - zulejman123


URLs:
http://127.0.0.1:8000/auth/token/login/ - POST for obtaining token, user credentials required in body form

http://127.0.0.1:8000/auth/users/ - GET all users, admin token required in auth tab
http://127.0.0.1:8000/auth/users/ - POST creating new user, admin token required in auth tab

http://127.0.0.1:8000/restaurant/api/menu/ - GET all menu items, no token required
http://127.0.0.1:8000/restaurant/api/menu/ - POST creating menu item, admin token required in auth tab
http://127.0.0.1:8000/restaurant/api/menu/3 - GET single menu item, no token required
http://127.0.0.1:8000/restaurant/api/menu/3 - PUT, PATCH, DELETE single menu item, admin token required in auth tab

http://127.0.0.1:8000/restaurant/api/bookings/ - GET all bookings, user/admin token required in auth tab
http://127.0.0.1:8000/restaurant/api/bookings/2 - GET single booking, user/admin token required in auth tab
http://127.0.0.1:8000/restaurant/api/bookings/2 - PUT, PATCH, DELETE single booking, admin token required in auth tab


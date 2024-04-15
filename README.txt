LittleLemon API endpoints

home page
GET /restaurant/

user registration: username, password
POST /auth/users/

user login: username,password
POST /api-token-auth/
POST /auth/token/login/

user logout: username,password
POST /auth/token/logout/

menu items:
GET /restaurant/menu/
POST /restaurant/menu/
GET /restaurant/menu/{id}
DELETE /restaurant/menu/{id}
PUT /restaurant/menu/{id}

booking tables:
GET /restaurant/booking/tables/
POST /restaurant/booking/tables/

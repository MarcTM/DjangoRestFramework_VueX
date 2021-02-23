<h1>2DAW PROJECT WITH DJANGO REST FRAMEWORK AND VUEX</h1>

This web page works with 1 backend (Django Rest Framework, a Python framework) and the frontend (VueX).  
Poject developed by *Marc Torres Martínez*.
<br>
With this project I was trying to do a page where the people can buy meals/tuppers.
---

## Getting started

To run this repository locally:

- Clone this repository to a folder
- Install PostgreSQL and run it. Then create the database that you are going to use for the application.
- Migrate DRF tables with python3 manage.py makemigrations and python3 manage.py migrate.
- Now you can execute the frontend with **npm start**, and the backend with with **python3 manage.py runserver**.
- To access django pannel admin, go to localhost:8000/admin, and to register a superadmin do python3 manage.py createsuperuser. 


---

## Features

| Page | Features |
| - | - |
| Home | The home has the categories , that if you click you can see the category recipes |
| Shop | Lists the shop with a pagination and a search bar |
| Account | Non ended in Vue, but in Django you have your profile and you can update it |
| Cart | Lists your cart |


<br>

| Services | Features |
| - | - |
| Register | You can register manually |
| Login | You can login manually |
| Add and remove to cart | You can add and remove meals from your cart |

<br>

| Technical Features |  |
| - | - |
| Authentication | You need to be signed in (authenticated) to be allowed to do some actions |
| Admin features | You can create categories, meals, etc from the Django superadmin pannel |

---

### Technologies used in this project

* Python: Django Rest Framework
* VueX
* Docker
* PostgreSQL

### Other technologies used

* JWT 
* Docker Compose

---
Docker is actually not working, I couldn't end it.
---

# Module – 5 (DB and Python Framework

# Why Django should be used for web-development? Explain how you can create a project in Django? 
# ANS. Django is a powerful web framework that is widely used for web development due to its versatility, scalability, and productivity.
# -Rapid development
# -Object-relational mapping (ORM)
# -Scalability and reusability
# -Security
# -Community and ecosystem

# creating a project in Django
# --->create a virtual environment to isolate your project dependencies. You can create a virtual environment using tools like venv or virtualenv.

# --->Install Django: Once your environment is set up, you need to install Django. You can do this by running the command pip install django in your terminal.

# --->Create a Django project: Open your terminal, navigate to the desired directory where you want to create your project, and run the following command:
               #   django-admin startproject projectname

# --->Navigate to the project directory: After running the previous command, a new directory with your project's name will be created. Move into that directory using the cd command:
              #   cd projectname

# --->Run the development server: To test your project, run the following command:
            #    python manage.py runserver

# --->Access the project: Open your web browser and enter http://localhost:8000 in the address bar. You should see the default Django welcome page, confirming that your project is set up correctly.
# At this point, you have successfully created a Django project. From here, you can start defining your application's models, views, and templates by creating Django apps within your project. You can also configure the project's settings, connect to databases, handle URL routing, and add additional functionality using Django's extensive features and libraries.


# How to check installed version of django?
# ANS. To check the installed version of Django use the following command in terminal or command prompt:
            # python -m django --version


# Explain what does django-admin.py make messages command is used for?
# ANS. The django-admin.py makemessages command in Django is used for the management of internationalization (i18n) and localization (l10n) in Django projects. It is used to extract translatable strings from project's source code and create or update language-specific message files. When you're building a multilingual website or application, it's essential to provide translations for different languages. The makemessages command helps simplify this process by automatically scanning your project's source code, identifying translatable strings, and creating or updating language-specific message files.


# What is Django URLs?make program to create django url.
# ANS.In Django, URLs (Uniform Resource Locators) are used to map specific URLs or web addresses to corresponding views or functions in your Django project. URLs define the structure and routing of your web application, allowing to navigate to different pages or trigger specific actions based on the provided URL.
# In urls.py file:
# --->Open your project's main urls.py file. This file is typically located in the project's root directory.
# --->Import the necessary modules and functions:
            # from django.urls import path
            # from . import views
# --->Define your URL patterns using the path() function:
            # urlpatterns = [
        # path('', views.home, name='home'),
        # path('about/', views.about, name='about'),
        # ]
# --->Save the urls.py file.
# In view.py file:
# --->Open your Django application's views.py file.
# --->Define the view functions:
#    from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
    # return HttpResponse("Welcome!")
# def about(request):
    # return HttpResponse("This is the about page.")


# What is a QuerySet?Write program to create a new Post object in database:
# ANS.In Django, a QuerySet is a collection of database objects obtained from a model using a database query. It represents the results of a query and allows you to retrieve, filter, and manipulate data from the database.
# eg. -Suppose a Django project is set up with an app and a defined model for a "Post" object, open the file that contains the model (models.py) within your app.
# -Import the necessary modules and define  model class:
# from django.db import models
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
# -To create a new Post object and save it to the database, open a Python shell or a script interact with a Django project.
# -Import the necessary modules and create a new Post object:
# from myapp.models import Post
# from datetime import datetime
# post = Post(title='First Post', content='This is the content of my post.', pub_date=datetime.now())
# -Save the Post object to the database:
#           post.save()


# Mention what command line can be used to load data into Django? 
# python manage.py loaddata path/to/your/fixture/file


# Explain what does django-admin.py make messages command is used for? 
# The django-admin.py makemessages command in Django is used to create or update language translation files based on the translatable strings inDjango project.


# Make Django application to demonstrate following things o There will be 2 modules(Admin,Product manager) o Admin can add product name (ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc. Data should store in 
# ANS.
# Step 1: Set up a new Django project and application
#  django-admin startproject product_management
# cd product_management
# python manage.py startapp products

# Step 2: Configure the database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Step 3: Define the models
# from django.db import models
# class Admin(models.Model):
#     username = models.CharField(max_length=100)
# class Product(models.Model):
#     product_id = models.IntegerField()
#     product_name = models.CharField(max_length=100)
#     admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

# Step 4: Create the database tables
# python manage.py makemigrations
# python manage.py migrate


# Certainly! I'll provide you with an example Django application that demonstrates the functionality you mentioned, including two modules (Admin and Product Manager) and the ability for the admin to add product names (product ID and product name). The data will be stored in a database.

# Follow the steps below to create the application:

# Step 1: Set up a new Django project and application
# In your terminal or command prompt, navigate to the desired directory and run the following commands:

# bash
# Copy code
# django-admin startproject product_management
# cd product_management
# python manage.py startapp products
# This will create a new Django project named "product_management" with an application named "products".

# Step 2: Configure the database
# In the project's settings.py file, find the DATABASES section and modify it according to your database settings. For example, to use SQLite as the database, you can set it as follows:

# python
# Copy code
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# Step 3: Define the models
# In the products/models.py file, define the models for the Admin and Product Manager modules:

# python
# Copy code
# from django.db import models

# class Admin(models.Model):
#     username = models.CharField(max_length=100)

# class Product(models.Model):
#     product_id = models.IntegerField()
#     product_name = models.CharField(max_length=100)
#     admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
# Step 4: Create the database tables
# Run the following command in the terminal to create the necessary database tables:

# Copy code
# python manage.py makemigrations
# python manage.py migrate

# Step 5: Create views and templates
# from django.shortcuts import render, redirect
# from .models import Admin, Product
# def add_product(request):
#     if request.method == 'POST':
#         product_id = request.POST['product_id']
#         product_name = request.POST['product_name']
#         admin_id = request.POST['admin_id']
#         admin = Admin.objects.get(id=admin_id)
#         product = Product(product_id=product_id, product_name=product_name, admin=admin)
#         product.save()
#         return redirect('product_list')
#     else:
#         admins = Admin.objects.all()
#         return render(request, 'add_product.html', {'admins': admins})
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# add_product.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Add Product</title>
# </head>
# <body>
#     <h1>Add Product</h1>
#     <form method="post">
#         {% csrf_token %}
#         <label for="product_id">Product ID:</label>
#         <input type="number" name="product_id" required><br>

#         <label for="product_name">Product Name:</label>
#         <input type="text" name="product_name" required><br>

#         <label for="admin_id">Admin:</label>
#         <select name="admin_id" required>
#             {% for admin in admins %}
#                 <option value="{{ admin.id }}">{{ admin.username }}</option>
#             {% endfor %}
#         </select><br>

#         <input type="submit" value="Add Product">
#     </form>
# </body>
# </html>

# product_list.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Product List</title>
# </head>
# <body>
#     <h1>Product List</h1>
#     <ul>
#         {% for product in products %}
#             <li>{{ product.product_name }} - Admin: {{ product.admin.username }}</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>

# Step 6: Define URLs and run the application
# from django.contrib import admin
# from django.urls import path
# from products import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('add-product/', views.add_product, name='add_product'),
#     path('product-list/', views.product_list, name='product_list'),
# ]

# Save the files:
# python manage.py runserver



# Product_mst table with product id as primary key o Admin can add product subcategory details Like (Product price, product image, Product model, product Ram) data should store in Product_sub_cat table o Admin can get product name as foreign key from product_mst table in product_sub_category_details page Admin can view, update and delete all registered details of product manager can search product on search bar and get all details about product

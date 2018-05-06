# Coretabs Django Workshop
[Workshop Index](https://forums.coretabs.net/t/django/58)

## Lesson 01
### Install Last Version of Django
    pip install django

### Check Your Django Version, or Check if Django is Installed
    python -m django --version

### Start a New Project
    django-admin startproject coretabs

### Run Development Server
    python manage.py runserver

## Lesson 02
### Start a New Application
    python manage.py startapp shop

### Create migrations files for all apps, you can specify one or more applications
    python manage.py makemigrations [app] [app]

### Apply Migrations to Database
    python manage.py migrate

## Lesson 03
### Run Django Shell
    python manage.py shell

### Mission
<details>
  <summary>Show Solution</summary>

    python manage.py shell

    >>> from shop.models import Category, Product

    # Insert Data into Database
    >>> c1 = Category(name="Mobile Devices", description="This category will contain mobile devices")
    >>> c1.save()

    >>> c2 = Category(name="Computers", description="This category will contain computers")
    >>> c2.save()

    >>> p1 = Product.objects.create(name="Apple iPhone X", price=1100.00, stock=12, description="iPhone X features a new all-screen design. Face ID, which makes your face your password. And the most powerful and smartest chip ever in a smartphone.",category=c1)

    >>> p2 = Product.objects.create(name="Google Pixel 2", price=860.20, stock=14, description="The unlocked Pixel 2 provides a clean, bloat-free experience with no unwanted apps, one of the highest rated smartphone cameras, with free unlimited storage.",category=c1)

    >>> p3 = Product.objects.create(name="Sony Xperia ZX2", price=920.49, stock=9, description="The Xperia XZ2 is packed with the latest Sony technologies to deliver an entertainment experience that touches your senses in a whole new way – whether you’re lost in a HDR movie or capturing hidden details with the new advanced Motion Eye™ camera.",category=c1)

    >>> p4 = Product.objects.create(name="Dell Inspiron 17 5000", price=799.99, stock=11, description="17-inch laptop with an anti-glare, backlit display. Add options like an FHD screen with discrete graphics to create a PC that reflects what matters to you.",category=c2)

    >>> p5 = Product.objects.create(name="MacBook Pro", price=2999.00, stock=6, description="It’s razor thin, feather light, and even faster and more powerful than before. It has the brightest, most colorful Mac notebook display ever. And it features the Touch Bar — a Multi-Touch enabled strip of glass built into the keyboard for instant access to the tools you want, right when you want them. MacBook Pro is built on groundbreaking ideas. And it’s ready for yours.",category=c2)

    # Return all Products
    >>> Product.objects.all()

    # Return Product with id = 0
    >>> Product.objects.get(id=0)

    # Return Products with stock > 10
    >>> Product.objects.filter(stock__gt=10)

    # Change Description of Products with stock < 10
    >>> Product.objects.filter(stock__lt=10).update(description="Will be deleted")

    # Delete Products with Description = "Will be deleted"
    >>> Product.objects.filter(description__exact="Will be deleted").delete()

    # Return Products that not meet price__gte=900
    >>> Product.objects.exclude(price__gte=900)
</details>

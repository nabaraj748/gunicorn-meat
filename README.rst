Canned gUnicorn Meat
====================

This project allows you to easily script Gunicorn from Python.


Usage
-----

::

    from myflaskapp import app
    from gunicorn_meat import Meat

    server = Meat(app=app, workers=4, type='sync')


Gratitous Image
---------------

..image: http://a.tgcdn.net/images/products/frontsquare/e5a7_canned_unicorn_meat.jpg
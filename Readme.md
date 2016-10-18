# django-tasix

[![Build
Status](https://travis-ci.org/muminoff/django-tasix.svg?branch=master)](https://travis-ci.org/muminoff/django-tasix)

## What is Tas-IX?
Data exchange network in Uzbekistan, where many domestic ISP providers give access to resources within the network to their subscribers for free.

## What is `django-tasix`?
Simple django app to detect ip adresses/ranges of coming HTTP requests in middleware layer.

# Requirements

* Python (3.2, 3.3, 3.4, 3.5)
* Django (1.10)

# Installation

Install using `pip`:

    pip install django-tasix

There are 2 ways for using this app:

1. Middleware style (blocks every request outside Tas-IX)
2. Decorator style (blocks certain requests outside Tas-IX)

### Middleware style

Add `'tasix'` to your `MIDDLEWARE_CLASSES` setting:

    MIDDLEWARE_CLASSES = (
        # other middleware classes
        'tasix.middleware.TasixMiddleware',
    )

### Decorator style

Import `allow_tasix` decorator in your view

    from django.http import HttpResponse
    from tasix.decorators import allow_tasix


    @allow_tasix
    def index_view(request):
        return HttpResponse('Only Tas-IX users can view this')


## Disclaimer
Network range is being fetched manually from `http://tasix.sarkor.uz/full`, meaning correctness is based on 3rd party ISP provider which releases network information periodically.

## License
BSD

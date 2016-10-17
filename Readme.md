# django-tasix

## What is Tas-IX?
Data exchange network in Uzbekistan, where many domestic ISP providers give access to resources within the network to their subscribers for free.

## What is `django-tasix`?
Simple django app to detect ip adresses/ranges of coming HTTP requests in middleware layer.

# Requirements

* Python (2.7, 3.2, 3.3, 3.4, 3.5)
* Django (1.9, 1.10)

# Installation

Install using `pip`...

    pip install django-tasix

Add `'tasix'` to your `MIDDLEWARE_CLASSES` setting.

    MIDDLEWARE_CLASSES = (
        # other middleware classes
        'tasix.middleware.TasixMiddleware',
    )

## License
BSD

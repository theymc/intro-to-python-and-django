import requests
from django.core.management import setup_environ
from ymcproject import settings
setup_environ(settings)
import simplejson as json
from experiments import models


def _get_dict_for_one_page_of_products(page):
    response = requests.get("http://lcboapi.com/products?per_page=100&page=%d" % page)
    return response.json()


def _store_products_from_a_page(lcbo_data):
    for product in lcbo_data:
            lcbo_product = models.LcboProduct()  # Initialize our lcbo product object
            for field in models.LcboProduct._meta.fields:  # For every field on our model definition
                setattr(lcbo_product, field.name, product.get(field.name, None))  # Set the field with api data, or None if it does not exist
            if product.get('name', None):
                lcbo_product.save()


def store_all_lcbo_products():
    page = 0
    has_next_page = True
    while has_next_page:
        page += 1
        try:  # Thanks alot lcbo api for giving us malformed json.
            lcbo_data = _get_dict_for_one_page_of_products(page)
            _store_products_from_a_page(lcbo_data['result'])
        except json.scanner.JSONDecodeError:
            print "Page %s blew up with malformed json. Call the cops." % page
        if lcbo_data['pager']['is_final_page']:
            has_next_page = False

print "Begin stealing booze..."
store_all_lcbo_products()
print "%d liquor products have been stolen" % models.LcboProduct.objects.count()

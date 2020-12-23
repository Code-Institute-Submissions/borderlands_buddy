from django.test import TestCase


class TestViews(TestCase):
    # A test to see if the user is redirected to the checkout page
    def test_get_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 302)

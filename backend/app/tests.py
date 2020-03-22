from django.conf import settings
from django.test import Client, TestCase


class CocoCabanaTests(TestCase):

    def test_redirect(self):
        client = Client()
        response = client.get('/the-coco-cabana') 
        self.assertRedirects(
            response,
            settings.COCO_CABANA_HANGOUT_URL,
            fetch_redirect_response=False,
            status_code=302,
        )

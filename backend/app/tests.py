from django.conf import settings

from rest_framework.test import APITestCase


class FrontendTests(APITestCase):
    
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # It should return the frontend's index.html.
        with open(settings.FRONTEND_INDEX) as f:
            html = f.read()
            self.assertEqual(response.content, html.encode())


class CocoCabanaTests(APITestCase):

    def test_redirect(self):
        response = self.client.get('/the-coco-cabana') 
        self.assertRedirects(
            response,
            settings.COCO_CABANA_HANGOUT_URL,
            fetch_redirect_response=False,
            status_code=302,
        )

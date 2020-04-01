from datetime import datetime
from unittest import mock

from django.conf import settings

from rest_framework.test import APITestCase
import pytz


class FrontendTests(APITestCase):
    
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # It should return the frontend's index.html.
        with open(settings.FRONTEND_INDEX) as f:
            index = f.read().encode()
            self.assertEqual(response.content, index)


class CocoCabanaTests(APITestCase):

    @mock.patch('backend.app.views.timezone')
    def test_open(self, mock_timezone):
        # Mock 6:30pm PT.
        pt = pytz.timezone('US/Pacific')
        six_thirty = datetime.now(tz=pt).replace(hour=18, minute=30)
        mock_timezone.localtime.return_value = six_thirty
        
        response = self.client.get('/the-coco-cabana') 

        # It should redirect to the Google Hangout URL.
        self.assertRedirects(
            response,
            settings.COCO_CABANA_HANGOUT_URL,
            fetch_redirect_response=False,
            status_code=302,
        )

    @mock.patch('backend.app.views.timezone')
    def test_before_open(self, mock_timezone):
        # Mock 6:24pm PT (clubhouses open 5 minutes early
        # just in case someone arrives a little early).
        pt = pytz.timezone('US/Pacific')
        six_twenty_nine = datetime.now(tz=pt).replace(hour=18, minute=24)
        mock_timezone.localtime.return_value = six_twenty_nine
        
        response = self.client.get('/the-coco-cabana') 
        self.assertEqual(response.status_code, 200)

        # It should return the frontend's index.html.
        with open(settings.FRONTEND_INDEX) as f:
            index = f.read().encode()
            self.assertEqual(response.content, index)

    @mock.patch('backend.app.views.timezone')
    def test_after_close(self, mock_timezone):
        # Mock 7:30pm PT.
        pt = pytz.timezone('US/Pacific')
        seven_thirty = datetime.now(tz=pt).replace(hour=19, minute=30)
        mock_timezone.localtime.return_value = seven_thirty
        
        response = self.client.get('/the-coco-cabana') 
        self.assertEqual(response.status_code, 200)

        # It should return the frontend's index.html.
        with open(settings.FRONTEND_INDEX) as f:
            index = f.read().encode()
            self.assertEqual(response.content, index)

from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class BlogTest(SimpleTestCase):
  def helper_status_code_200(self, url_name):
    url = reverse(url_name)
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)


  def test_home_page_status(self):
    self.helper_status_code_200('home')
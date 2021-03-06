"""Test class for the user views."""
import json
from .import BaseClass

SIGNUP_URL = '/api/v1/user/register'
LOGIN_URL = '/api/v1/user/login'


class TestUserView(BaseClass):
    """docstring for TestUserView."""

    def test_user_routes_response_code(self):
        """Test API can register a user."""
        response = self.client.post(SIGNUP_URL, data=json.dumps(
            self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_routes_message(self):
        """Test API can register a user."""
        response = self.client.post(SIGNUP_URL, data=json.dumps(
            self.user_data), content_type='application/json')
        results = json.loads(response.data.decode())
        self.assertEqual(results['message'], 'Successfully registered')

    def test_signup_with_missing_details_status_code(self):
        """Test if API can signup with missing details."""
        response = self.client.post(SIGNUP_URL,
                                    data=json.dumps(
                                        {'username':
                                         'Barclay', 'email': 'koin@gmail.com'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        """Test the login method."""
        self.test_user.save()
        response = self.client.post(LOGIN_URL,
                                    data=json.dumps(
                                        {'username':
                                         'Barclay', 'password': 'mypassword'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

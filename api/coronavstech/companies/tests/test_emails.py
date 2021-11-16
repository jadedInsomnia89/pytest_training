import json
from django.core import mail
from django.test import Client, client
from django.test import TestCase
from unittest.mock import patch


class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
        ):
            # Test to make sure there are no emails in the outbox prior to sending message
            self.assertEqual(len(mail.outbox), 0)
            
            # Send email
            mail.send_mail(
                subject='Test Subject',
                message='Test message',
                from_email='testemail@gmail.com',
                recipient_list=['testemail2@gmail.com'],
                fail_silently=False,
            )
            
            # Test that one message has been sent
            self.assertEqual(len(mail.outbox), 1)
            
            # Verify that the subject is correct
            self.assertEqual(mail.outbox[0].subject, 'Test Subject')
            
    def test_send_email_without_arguments_should_send_empty_email(self) -> None:
        client = Client()
        
        with patch('api.coronavstech.companies.views.send_mail') as mocked_send_mail_function:
            response = client.post(path='/send-email')
            response_content = json.loads(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['status'], 'success')
            self.assertEqual(response_content['info'], 'email sent successfully')
            mocked_send_mail_function.assert_called_with(
                subject=None,
                message=None,
                from_email='whosyerdady2007@gmail.com',
                recipient_list=['whosyerdady2007@gmail.com'],
            )
            
    def test_send_email_with_get_verb_should_fail(self) -> None:
        client = Client()
        response = client.get(path='/send-email')
        assert response.status_code == 405
        assert json.loads(response.content) == {'detail': 'Method "GET" not allowed.'}

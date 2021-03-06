import json
from django.core import mail
from unittest.mock import patch


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

    # Test to make sure there are no emails in the outbox prior to sending message
    assert len(mailoutbox) == 0

    # Send email
    mail.send_mail(
        subject='Test Subject',
        message='Test message',
        from_email='testemail@gmail.com',
        recipient_list=['testemail2@gmail.com'],
        fail_silently=False,
    )

    # Test that one message has been sent
    assert len(mailoutbox) == 1

    # Verify that the subject is correct
    assert mailoutbox[0].subject == 'Test Subject'


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch('api.coronavstech.companies.views.send_mail'
              ) as mocked_send_mail_function:
        response = client.post(path='/send-email')
        assert response.status_code == 200

        response_content = response.json()
        assert response_content['status'] == 'success'
        assert response_content['info'] == 'email sent successfully'
        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email='whosyerdady2007@gmail.com',
            recipient_list=['whosyerdady2007@gmail.com'],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path='/send-email')
    assert response.status_code == 405
    assert response.json() == {'detail': 'Method "GET" not allowed.'}

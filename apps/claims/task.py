from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Claim


@shared_task
def send_claim_notification(claim_id):
    """
    Task to send a notification email for a claim.

    This task retrieves the claim instance using the provided claim_id and
    sends an email notification to the claimer.
    """
    try:
        claim = Claim.objects.get(id=claim-id)
        claim_email = claim.claimer.email

        send_mail(
            subjects="Claim Notification",
            message= f"your claim for {claim.title} has been received and is being processed.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[claim_email],
            fail_silently=False,
        )
    except Claim.DoesNotExist:
        print(f"Claim with id {claim_id} does not exist.")
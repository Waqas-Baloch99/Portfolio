from django.utils.timezone import now
from .models import Payment

class CheckMembershipMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            payment = Payment.objects.filter(user=request.user, status='completed').order_by('-renewal_date').first()
            if payment and payment.renewal_date < now():
                request.user.is_premium = False
                request.user.save()
        return self.get_response(request)

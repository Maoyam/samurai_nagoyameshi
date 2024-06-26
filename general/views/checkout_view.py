from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse, HttpResponse
from commondb.models.user import User
import stripe
import os

#-----サブスクメソッド------


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':

        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'payment_successful/',
                cancel_url=domain_url + 'payment_cancelled/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body.decode('utf-8')
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)


@method_decorator(login_required,name="dispatch")
class UpgradeView(TemplateView):
    template_name = "general/user_upgrade.html"

@method_decorator(login_required,name="dispatch")
class UpgradeCheckoutView(TemplateView):
    template_name = "general/upgrade_checkout.html"

@method_decorator(login_required,name="dispatch")
class UpgradeSuccessView(TemplateView):
    template_name = "general/upgrade_success.html"
    
    def dispatch(self, request, *args, **kwargs):
        # ユーザーを取得
        user = request.user
        # is_paid_memberをTrueに変更
        user.is_paid_member = True
        # 保存
        user.save()
        # 親クラスのdispatchメソッドを呼び出してビューを処理
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name="dispatch")
class UpgradeCancelView(TemplateView):
    template_name = "general/upgrade_cancel.html"

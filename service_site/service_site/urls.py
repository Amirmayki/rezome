"""
URL configuration for service_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render, redirect
from core.models import Service, Portfolio
from django.contrib import messages
from core.forms import OrderForm
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
def calculate_price(service, description):
    """هوش مصنوعی قیمت‌گذاری واقعی"""
    base = service.base_price
    desc = description.lower()
    complexity = 1.0
    time_estimate = "۷-۱۰ روز کاری"

    if any(word in desc for word in ['فروشگاه', 'فروشگاهی', 'shop', 'ecommerce']):
        complexity += 1.8
        time_estimate = "۱۴-۲۵ روز"
    elif any(word in desc for word in ['رزومه', 'شخصی', 'لندینگ', 'پورتفولیو']):
        complexity += 0.5
        time_estimate = "۵-۸ روز"
    elif any(word in desc for word in ['اپ', 'موبایل']):
        complexity += 2.3
        time_estimate = "۲۵-۴۰ روز"

    if any(word in desc for word in ['انیمیشن', 'سینمایی', 'خفن', 'immersive']):
        complexity += 1.1
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    length_factor = len(description) / 180
    final_price = int(base * complexity * (1 + length_factor))
    final_price = max(final_price, base)

    return final_price, time_estimate

def home(request):
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()[:6]  # فقط ۶ تا نشون بده
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.estimated_price, _ = calculate_price(order.service, order.description)
            order.save()
            messages.success(
                request,
                "✅ سفارش شما با موفقیت ثبت شد. کارشناسان ما به زودی با شما تماس خواهند گرفت."
            )
            return redirect('success')

    context = {
        'services': services,
        'portfolios': portfolios,
        'form': form,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, "about.html")

def success(request):
    return render(request, 'success.html')
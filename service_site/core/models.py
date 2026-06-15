from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="نام خدمت")
    description = models.TextField(verbose_name="توضیحات")
    base_price = models.IntegerField(verbose_name="قیمت پایه (تومان)")
    icon = models.CharField(max_length=100, blank=True, verbose_name="آیکون Font Awesome")

    def str(self):
        return self.title

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"


class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات کامل")
    image = models.ImageField(upload_to='portfolio/', verbose_name="عکس پروژه")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='projects')
    link = models.URLField(blank=True, null=True, verbose_name="لینک پروژه")
    technologies = models.CharField(max_length=300, blank=True)
    client = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کارها"
        ordering = ['-created_at']


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('processing', 'در حال انجام'),
        ('completed', 'تحویل داده شد'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    estimated_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"سفارش {self.name} - {self.service.title}"
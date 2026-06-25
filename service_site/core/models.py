from django.db import models
from django.core.validators import MinLengthValidator

class Service(models.Model):

    title = models.CharField(
        max_length=150,
        verbose_name="نام خدمت"
    )

    description = models.TextField(
        verbose_name="توضیحات"
    )

    base_price = models.PositiveIntegerField(
        verbose_name="قیمت پایه"
    )

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=300, blank=True)
    client = models.CharField(max_length=150, blank=True)
    link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Order(models.Model):

    STATUS = (

        ("pending", "در انتظار"),

        ("review", "در حال بررسی"),

        ("working", "در حال انجام"),

        ("completed", "تحویل شده"),

    )

    name = models.CharField(

        max_length=100

    )

    phone = models.CharField(

        max_length=20

    )

    email = models.EmailField(

        blank=True

    )

    service = models.ForeignKey(

        Service,

        on_delete=models.CASCADE

    )

    budget = models.PositiveIntegerField(

        default=0

    )

    description = models.TextField(

        validators=[MinLengthValidator(20)]

    )

    estimated_price = models.PositiveIntegerField(

        default=0

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS,

        default="pending"

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="نام"
    )

    email = models.EmailField(
        verbose_name="ایمیل"
    )

    subject = models.CharField(
        max_length=200,
        verbose_name="موضوع"
    )

    message = models.TextField(
        verbose_name="پیام"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject

class Testimonial(models.Model):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    stars = models.IntegerField(default=5)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Career(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان شغلی"
    )

    description = models.TextField(
        verbose_name="توضیحات"
    )

    requirements = models.TextField(
        verbose_name="شرایط"
    )

    salary = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="حقوق"
    )

    active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class JobApplication(models.Model):

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    position = models.ForeignKey(
        Career,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to="resumes/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name
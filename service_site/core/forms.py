from django import forms
from .models import Order
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            "name",
            "phone",
            "email",
            "service",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "نام و نام خانوادگی",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "شماره تماس (09xxxxxxxxx)",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "ایمیل (اختیاری)",
                }
            ),

            "service": forms.Select(
                attrs={
                    "class": "form-select form-select-lg",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "مثال: طراحی سایت فروشگاهی با پنل مدیریت، درگاه پرداخت و طراحی اختصاصی...",
                }
            ),
        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if len(name) < 3:
            raise forms.ValidationError("نام باید حداقل ۳ کاراکتر باشد.")

        if len(name) > 100:
            raise forms.ValidationError("نام بیش از حد طولانی است.")

        return name

    def clean_description(self):

        description = self.cleaned_data["description"]

        if len(description.strip()) < 20:
            raise forms.ValidationError(
                "توضیحات پروژه باید حداقل ۲۰ کاراکتر باشد."
            )

        return description

    def clean_phone(self):

        phone = self.cleaned_data["phone"].replace(" ", "")

        pattern = r"^09\d{9}$"

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                "شماره موبایل معتبر نیست."
            )

        return phone

    def clean_email(self):

        email = self.cleaned_data["email"]

        if email:

            email = email.lower()

            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError("ایمیل معتبر نیست.")

        return email

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={

                "class": "form-control",

                "placeholder": "نام شما"

            }),

            "email": forms.EmailInput(attrs={

                "class": "form-control",

                "placeholder": "ایمیل"

            }),

            "subject": forms.TextInput(attrs={

                "class": "form-control",

                "placeholder": "موضوع"

            }),

            "message": forms.Textarea(attrs={

                "class": "form-control",

                "rows": 6,

                "placeholder": "پیام خود را بنویسید"

            }),

        }
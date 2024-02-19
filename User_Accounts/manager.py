from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    # here the 'email' parameter is refrenced from the BaseUserManager Class
    def create_user(self, email, password = None, **extra_fields):
        
        # same 'email' parameter in if condition
        if not email:
            raise ValueError('Email is required')

        # same 'email' parameter inside brackets
        normalized_email = self.normalize_email(email)
        phone = extra_fields.pop('phone_number', None)

        # here 'email' is refrencing the email field in CustomUser model in models.py
        user = self.model(email = normalized_email , phone_number = phone, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)
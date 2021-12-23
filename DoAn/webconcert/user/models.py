from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
    lưu dữ liệu thông tin người dùng
    """
    phone = models.CharField(max_length=40, help_text="Số điện thoại")
    addr = models.CharField(max_length=200, help_text="Địa chỉ", default='')


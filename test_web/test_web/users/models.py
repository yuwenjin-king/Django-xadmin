from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Test-Web."""

    #: First and last name do not cover name patterns around the globe
    nick_name = models.CharField(_("昵称"), blank=True, max_length=255)
    job_title = models.CharField(_("职称"), blank=True, max_length=255)
    introduction = models.TextField(_("职称"), blank=True, max_length=255)
    picture = models.ImageField(_("图片"), upload_to='profile_pics/', blank=True, max_length=255)
    location = models.CharField(_("地理位置"), blank=True, max_length=255)
    personal_url = models.URLField(_("个人地址"), blank=True, max_length=255)
    webo_url = models.URLField(_("微博地址"), blank=True, max_length=255)
    zhihu_url = models.URLField(_("知乎地址"), blank=True, max_length=255)
    github_url = models.URLField(_("github地址"), blank=True, max_length=255)
    create_time = models.DateTimeField(_("创建时间"), auto_now_add=True)
    update_time = models.DateTimeField(_("更新时间"), auto_now_add=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
    def get_profile_name(self):
        if self.nick_name:
            return self.nick_name


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

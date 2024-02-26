from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client

import os

from random import choice

from .models import AtlasUser


# Create your tests here.
class AtlasUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "test", email="test@example.com", password="password"
        )
        self.user.save()
        self.deleteFiles = []
        self.client = Client()

    def tearDown(self):
        parent_folders = set()
        for file in self.deleteFiles:
            parent_folders.add(os.path.abspath(os.path.dirname(file)))
            os.remove(file)
        for folder in parent_folders:
            os.rmdir(folder)

    def test_can_create_atlas_user(self):
        atlas_user = AtlasUser(
            user=self.user,
            department=AtlasUser.DepartmentNames.SOFTWARE_DEVELOPMENT,
            role=AtlasUser.Roles.MEMBER,
        )
        atlas_user.save()
        self.assertEqual(str(atlas_user), "test in Software Development department")

    def test_atlas_user_can_save_profile_picture(self):
        atlas_user = AtlasUser(
            user=self.user,
            department=AtlasUser.DepartmentNames.SOFTWARE_DEVELOPMENT,
            role=AtlasUser.Roles.MEMBER,
        )
        atlas_user.save()
        uploaded_file = SimpleUploadedFile(
            "profile_picture.jpeg",
            open("./tests/assets/profile/profile_picture.jpeg", "rb").read(),
            "image/jpeg",
        )
        atlas_user.profile_picture = uploaded_file
        atlas_user.save()
        self.deleteFiles.append(atlas_user.profile_picture.path)
        self.assertTrue(os.path.exists(atlas_user.profile_picture.path))


class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "test", email="test@example.com", password="password"
        )
        self.user.save()
        self.atlas_user = AtlasUser.objects.create(
            user=self.user,
            department=choice(list(AtlasUser.DepartmentNames)),
            role=choice(list(AtlasUser.Roles)),
            telegram_handle="testuser",
        )
        self.atlas_user.save()

    def test_can_get_csrf_token(self):
        self.assertFalse("csrftoken" in self.client.cookies)
        response = self.client.get("/auth/csrf")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("csrftoken" in self.client.cookies)

    def test_can_login(self):
        self.assertFalse("csrftoken" in self.client.cookies)
        response = self.client.post(
            "/auth/login", {"username": "test", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("csrftoken" in self.client.cookies)

    def test_can_get_user(self):
        response = self.client.post(
            "/auth/login", {"username": "test", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/auth/user")
        self.assertJSONEqual(
            response.content,
            {
                "username": self.user.username,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "email": self.user.email,
                "profile_picture": self.user.atlasuser.profile_picture.url,
                "department": self.user.atlasuser.department,
                "role": self.user.atlasuser.role,
                "telegram_handle": self.user.atlasuser.telegram_handle,
            },
        )

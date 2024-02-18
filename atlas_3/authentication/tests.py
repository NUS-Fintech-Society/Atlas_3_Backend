from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

import os

from authentication.models import AtlasUser


# Create your tests here.
class AtlasUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', email='test@example.com', password='password')
        self.user.save()
        self.deleteFiles = []

    def tearDown(self):
        parent_folders = set()
        for file in self.deleteFiles:
            parent_folders.add(os.path.abspath(os.path.dirname(file)))
            os.remove(file)
        for folder in parent_folders:
            os.rmdir(folder)

    def test_can_create_atlas_user(self):
        atlas_user = AtlasUser(user=self.user, department=AtlasUser.DepartmentNames.SOFTWARE_DEVELOPMENT, role=AtlasUser.Roles.MEMBER)
        atlas_user.save()
        self.assertEqual(str(atlas_user), 'test in Software Development department')

    def test_atlas_user_can_save_profile_picture(self):
        atlas_user = AtlasUser(user=self.user, department=AtlasUser.DepartmentNames.SOFTWARE_DEVELOPMENT, role=AtlasUser.Roles.MEMBER)
        atlas_user.save()
        uploaded_file = SimpleUploadedFile('profile_picture.jpeg', open('./tests/assets/profile/profile_picture.jpeg', 'rb').read(), 'image/jpeg')
        atlas_user.profile_picture = uploaded_file
        atlas_user.save()
        self.deleteFiles.append(atlas_user.profile_picture.path)
        self.assertTrue(os.path.exists(atlas_user.profile_picture.path))

from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_profile(self):
        """ test view for profile """

        self.user = User.objects.create_user(
            username='phife',
            password='aTribeCalledQuest'
        )

        self.client.login(username='phife', password='aTribeCalledQuest')

        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)

        template = 'profiles/profile.html'
        self.assertTemplateUsed(response, template)

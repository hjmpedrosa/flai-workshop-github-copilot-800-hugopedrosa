from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import OctoFitUser, Team, Activity, Leaderboard, Workout
from datetime import date


class OctoFitUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = OctoFitUser.objects.create(
            name='Tony Stark', email='tony@avengers.com', age=45
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tony Stark')

    def test_create_user(self):
        data = {'name': 'Bruce Banner', 'email': 'bruce@avengers.com', 'age': 40}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = OctoFitUser.objects.create(
            name='Peter Parker', email='peter@avengers.com', age=22
        )
        self.team = Team.objects.create(name='Team Marvel')
        self.team.members.set([self.user])

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_team(self):
        response = self.client.get(f'/api/teams/{self.team.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')


class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = OctoFitUser.objects.create(
            name='Natasha Romanoff', email='natasha@avengers.com', age=35
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Combat Training',
            duration=90,
            date=date(2026, 2, 22),
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_activity(self):
        response = self.client.get(f'/api/activities/{self.activity.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity_type'], 'Combat Training')


class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = OctoFitUser.objects.create(
            name='Thor Odinson', email='thor@avengers.com', age=1500
        )
        self.entry = Leaderboard.objects.create(user=self.user, score=1200)

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_entry(self):
        response = self.client.get(f'/api/leaderboard/{self.entry.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 1200)


class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Arc Reactor Endurance',
            description='High-intensity Iron Man endurance workout',
            exercises='Repulsor Pushups,Flight Planks,Sprint Intervals',
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_workout(self):
        response = self.client.get(f'/api/workouts/{self.workout.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Arc Reactor Endurance')


class APIRootTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_at_slash(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_root_at_api(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.core.management.base import BaseCommand
from octofit_tracker.models import OctoFitUser, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')

        # Delete in reverse dependency order
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        OctoFitUser.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating superhero users...')

        # Marvel heroes
        tony = OctoFitUser.objects.create(name='Tony Stark', email='tony@avengers.com', age=45)
        peter = OctoFitUser.objects.create(name='Peter Parker', email='peter@avengers.com', age=22)
        natasha = OctoFitUser.objects.create(name='Natasha Romanoff', email='natasha@avengers.com', age=35)
        thor = OctoFitUser.objects.create(name='Thor Odinson', email='thor@avengers.com', age=1500)

        # DC heroes
        bruce = OctoFitUser.objects.create(name='Bruce Wayne', email='bruce@jla.com', age=42)
        diana = OctoFitUser.objects.create(name='Diana Prince', email='diana@jla.com', age=900)
        clark = OctoFitUser.objects.create(name='Clark Kent', email='clark@jla.com', age=38)
        barry = OctoFitUser.objects.create(name='Barry Allen', email='barry@jla.com', age=28)

        self.stdout.write('Creating teams...')

        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.set([tony, peter, natasha, thor])

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.set([bruce, diana, clark, barry])

        self.stdout.write('Creating activities...')

        Activity.objects.create(user=tony, activity_type='Iron Man Flight Training', duration=60, date=date(2026, 2, 20))
        Activity.objects.create(user=peter, activity_type='Web-Slinging Cardio', duration=45, date=date(2026, 2, 21))
        Activity.objects.create(user=natasha, activity_type='Black Widow Combat Drills', duration=90, date=date(2026, 2, 22))
        Activity.objects.create(user=thor, activity_type='Hammer Throw', duration=30, date=date(2026, 2, 22))
        Activity.objects.create(user=bruce, activity_type='Bat-Cave Strength Training', duration=120, date=date(2026, 2, 20))
        Activity.objects.create(user=diana, activity_type='Amazonian Warrior Training', duration=75, date=date(2026, 2, 21))
        Activity.objects.create(user=clark, activity_type='Flying Speed Run', duration=20, date=date(2026, 2, 23))
        Activity.objects.create(user=barry, activity_type='Speed Force Sprint', duration=10, date=date(2026, 2, 23))

        self.stdout.write('Creating leaderboard...')

        Leaderboard.objects.create(user=tony, score=980)
        Leaderboard.objects.create(user=peter, score=870)
        Leaderboard.objects.create(user=natasha, score=950)
        Leaderboard.objects.create(user=thor, score=1200)
        Leaderboard.objects.create(user=bruce, score=1100)
        Leaderboard.objects.create(user=diana, score=1050)
        Leaderboard.objects.create(user=clark, score=1300)
        Leaderboard.objects.create(user=barry, score=1400)

        self.stdout.write('Creating workouts...')

        Workout.objects.create(
            name='Arc Reactor Endurance',
            description='High-intensity endurance workout inspired by Iron Man',
            exercises='Repulsor Pushups,Flight Simulation Planks,Armor Sprint Intervals,Core Reactor Crunches',
        )
        Workout.objects.create(
            name='Spider Agility Circuit',
            description='Agility and flexibility workout inspired by Spider-Man',
            exercises='Wall Crawl Squats,Web-Shoot Shoulder Press,Spider Crawl,Quick Reflex Burpees',
        )
        Workout.objects.create(
            name='Dark Knight Strength',
            description='Strength and conditioning inspired by Batman',
            exercises='Bat-Pull Ups,Batarang Rotations,Gotham Deadlift,Stealth Lunges',
        )
        Workout.objects.create(
            name='Speed Force Cardio',
            description='Ultra-fast cardio session inspired by The Flash',
            exercises='Lightning Sprints,Treadmill Max Speed,Speed Force Jumps,Flashpoint Shuttle Runs',
        )

        self.stdout.write(self.style.SUCCESS('Database populated successfully with superhero test data!'))
        self.stdout.write(f'  Users: {OctoFitUser.objects.count()}')
        self.stdout.write(f'  Teams: {Team.objects.count()}')
        self.stdout.write(f'  Activities: {Activity.objects.count()}')
        self.stdout.write(f'  Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'  Workouts: {Workout.objects.count()}')

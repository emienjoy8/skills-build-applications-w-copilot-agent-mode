from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # 清空所有集合
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 创建团队
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # 创建用户
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
        ]
        for user in users:
            user.save()

        # 创建活动
        activities = [
            Activity(user='Spider-Man', type='Running', duration=30),
            Activity(user='Iron Man', type='Cycling', duration=45),
            Activity(user='Wonder Woman', type='Swimming', duration=60),
            Activity(user='Batman', type='Yoga', duration=20),
        ]
        for activity in activities:
            activity.save()

        # 创建排行榜
        Leaderboard.objects.create(team=marvel.name, points=150)
        Leaderboard.objects.create(team=dc.name, points=120)

        # 创建锻炼
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes.'),
            Workout(name='Power Yoga', description='Yoga for strength and flexibility.'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功填充测试数据！'))

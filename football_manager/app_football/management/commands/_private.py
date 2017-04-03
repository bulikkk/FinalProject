from faker import Factory
from random import choice, randint

from football_manager.settings import *
from app_football.models import Player, Team, User



def create_teams_names():
    fake = Factory.create("en_GB")
    name = fake.last_name()
    return name + " FC"

def create_teams():
    for i in range(15):
        user = User.objects.create(username=(str(i) + "a"))
        Team.objects.create(name=create_teams_names(), user=user)

def create_name():
    fake = Factory.create("en_GB")
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


def create_players():
    player_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for team in Team.objects.all():
        for player in player_range:
            name = create_name()
            if player <= 3:
                att = randint(20, 30)
                deff = randint(50, 60)
                Player.objects.create(name=name[0], surname=name[1], position=1, attack=att, defence=deff, team=team)
            elif player <= 9:
                att = randint(30, 40)
                deff = randint(40, 50)
                Player.objects.create(name=name[0], surname=name[1], position=2, attack=att, defence=deff, team=team)
            elif player <= 15:
                att = randint(40, 50)
                deff = randint(30, 40)
                Player.objects.create(name=name[0], surname=name[1], position=3, attack=att, defence=deff, team=team)
            elif player <= 18:
                att = randint(50, 60)
                deff = randint(20, 30)
                Player.objects.create(name=name[0], surname=name[1], position=4, attack=att, defence=deff, team=team)

# def create_subjects():
#     Subject.objects.create(name="Język polski", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Matematyka", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Język angielski", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Fizyka", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Wychowanie fizyczne", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Technika", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Biologia", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Chemia", teacher_name=" ".join(create_name()))
#     Subject.objects.create(name="Geografia", teacher_name=" ".join(create_name()))


# def create_grades():
#     students = Student.objects.all()
#     subjects = Subject.objects.all()
#     for student in students:
#         for subject in subjects:
#             for i in range(1, 6):
#                 StudentGrades.objects.create(student=student, school_subject=subject, grade=choice([1, 1.5, 1.75, 2, 2.5, 2.75, 3, 3.5, 3.75, 4, 4.5, 4.75, 5, 5.5, 5.75, 6]))

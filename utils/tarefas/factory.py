# from inspect import signature
from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')


def make_task():
    return {
        'id_task' : fake.random_number(digits=2, fix_len=True),
        'task_name': fake.sentence(nb_words=4),
        'description': fake.sentence(nb_words=12),
        'priority': fake.word(),
        'type': fake.word(),
        'deadline': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        }
    }
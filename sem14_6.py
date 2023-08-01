import sem13_6
import pytest
import json


@pytest.fixture
def new_data():
    data = {"1": ["John", 4],
            "2": ["Ben", 1],
            "5": ["Иван", 1],
            "4": ["Ольга", 5]}
    with open('test.json', 'w', encoding='UTF-8') as f1:
        json.dump(data, f1)
    return data


@pytest.fixture
def new_project(new_data):
    p = sem13_6.Project('test.json')
    p.enter(id='2', name='Ben')
    return p


@pytest.fixture
def new_user():
    return dict(id='7', name='Steve', level=2)


def test_add_user(new_user, new_project, new_data):
    # tmp = new_project.users.copy()
    # tmp.add(sem13_6.User(id=7, name='Steve', level=2))
    num_users = len(new_project.users)
    new_project.add_user(**new_user)

    # new_data['7'] = ['Steve', 2]
    assert (len(new_project.users) == num_users + 1)


def test_enter(new_project):
    num_users = len(new_project.users)
    new_project.enter(id="5", name="Иван")
    assert (len(new_project.users) == num_users)

def test_enter2(new_project):
    num_users = len(new_project.users)
    with pytest.raises(sem13_6.AccessException):
        new_project.enter(id="4", name="Иван")



if __name__ == '__main__':
    pytest.main()

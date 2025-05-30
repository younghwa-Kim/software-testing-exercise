import pytest
from lift import Lift

def test_initial_values():
    lift = Lift(5)
    assert lift.get_top_floor() == 5
    assert lift.get_current_floor() == 0
    assert lift.get_num_riders() == 0
    assert not lift.is_full()

def test_add_riders_not_full():
    lift = Lift(5)
    lift.add_riders(5)
    assert lift.get_num_riders() == 5
    assert not lift.is_full()


def test_go_up():
    lift = Lift(3)
    lift.go_up()
    lift.go_up()
    lift.go_up()  # should be at top
    lift.go_up()  # should stay at top
    assert lift.get_current_floor() == 3

def test_go_down():
    #Create lift object
    lift = Lift(3)
    #INcrease current_floor > 0
    lift.go_up()
    lift.go_up()
    lift.go_down()
    assert lift.get_current_floor() == 1
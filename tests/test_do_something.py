import pytest
import test_hatch_uv_actions.do_something as do


def test_return_1():
    assert do.return_1() == 1

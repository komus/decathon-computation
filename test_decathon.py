import pytest
from decathon import ComputeDecathon


def test_score_100m():
    assert ComputeDecathon().score_100m(10.395) == 1000
    assert ComputeDecathon().score_100m(10.827) >= 900

def test_score_long_jump():
    assert ComputeDecathon().score_long_jum(7.76) == 1000
    assert ComputeDecathon().score_long_jum(7.36) >= 900

def test_score_shot_put():
    assert ComputeDecathon().score_shot_put(18.40) == 1000
    assert ComputeDecathon().score_shot_put(16.79) >= 900

def test_score_high_jump():
    assert ComputeDecathon().score_high_jump(2.20) == 1000
    assert ComputeDecathon().score_high_jump(2.10) >= 900

def test_score_400m():
    assert ComputeDecathon().score_400m(46.17) == 1000
    assert ComputeDecathon().score_400m(48.19) == 900

def test_score_110m_hurdles():
    assert ComputeDecathon().score_110_hurdles(13.80) == 1000
    assert ComputeDecathon().score_110_hurdles(14.59) >= 900

def test_score_discus():
    assert ComputeDecathon().score_discus_throw(56.17) == 1000
    assert ComputeDecathon().score_discus_throw(51.4) >= 900

def test_score_pole_vault():
    assert ComputeDecathon().score_pole_vault(5.28) == 1000
    assert ComputeDecathon().score_pole_vault(4.96) >= 900

def test_score_javalin():
    assert ComputeDecathon().score_javelin(77.19) == 1000
    assert ComputeDecathon().score_javelin(70.67) >= 900

def test_score_1500():
    assert ComputeDecathon().score_1500m('3:53.79') == 1000
    assert ComputeDecathon().score_1500m('4.07.42') >= 900

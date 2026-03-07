import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points_works(game):
    result = add_points(game, 10)
    assert result["score"] == 10

def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)

def test_no_points_added_when_inactive(game):
    game["active"] = False
    result = add_points(game, 10)
    assert result["score"] == 0

def test_multiplier_updates(game):
    result = apply_multiplier(game, 2)
    assert result["multiplier"] == 2

def test_multiplier_rejects_less_than_1(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0.5)

def test_no_multiplier_added_when_inactive(game):
    game["active"] = False
    game["score"] = 2
    result = apply_multiplier(game, 2)
    assert result["score"] == 2

def test_reset_score_works(game):
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"] == 1

def test_reset_score_works_when_inactive(game):
    game["active"] = False
    game["score"] = 2
    game["multiplier"] = 2
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"] == 1

def test_is_high_score_works(game):
    threshold = 1
    result = is_high_score(game, threshold)
    assert result == False

def test_threshold_greater_than_or_equal_to_0(game):
    with pytest.raises(ValueError):
        is_high_score(game, -1)

from health import take_damage, heal


def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] == 50


def test_heal_adds_health(player):
    result = heal(player, 20)
    assert result["health"] == 100


def test_player_dies(player):
    result = take_damage(player, 100)
    assert not result["alive"]

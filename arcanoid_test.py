from main import paddle, game_ball, is_game_over

import pytest


# Fixture for creating a player paddle object
@pytest.fixture
def create_player_paddle():
    return paddle()


# Fixture for creating a game ball object
@pytest.fixture
def create_game_ball(create_player_paddle):
    return game_ball(create_player_paddle.x +
                     (create_player_paddle.width // 2), create_player_paddle.y - create_player_paddle.height)
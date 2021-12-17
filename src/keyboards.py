from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from game import Game


def game_keyboard(game: Game):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=game.button_1,
                    callback_data="button_1",
                ),
                InlineKeyboardButton(
                    text=game.button_2,
                    callback_data="button_2",
                ),
                InlineKeyboardButton(
                    text=game.button_3,
                    callback_data="button_3",
                )
            ],
            [
                InlineKeyboardButton(
                    text=game.button_4,
                    callback_data="button_4",
                ),
                InlineKeyboardButton(
                    text=game.button_5,
                    callback_data="button_5",
                ),
                InlineKeyboardButton(
                    text=game.button_6,
                    callback_data="button_6",
                )
            ],
            [
                InlineKeyboardButton(
                    text=game.button_7,
                    callback_data="button_7",
                ),
                InlineKeyboardButton(
                    text=game.button_8,
                    callback_data="button_8",
                ),
                InlineKeyboardButton(
                    text=game.button_9,
                    callback_data="button_9",
                )
            ],
        ]
    )

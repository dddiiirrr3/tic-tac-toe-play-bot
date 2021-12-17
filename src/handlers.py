from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from game import Game
from keyboards import game_keyboard


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_handler(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def game_handler(update: Update, context: CallbackContext):
    game = Game()
    context.chat_data['game'] = game

    game_message = context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='game:',
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=game_keyboard(game),
    )
    context.chat_data['game_message'] = game_message


def game_button_handler(update: Update, context: CallbackContext):
    update.callback_query.answer()
    button = update.callback_query.data.replace('button_', '')

    game = context.chat_data['game']
    exec(f"game.change_button_{button}()")
    game_message = context.chat_data['game_message']
    context.chat_data['game'] = game

    context.bot.edit_message_reply_markup(
        chat_id=game_message.chat_id,
        message_id=game_message.message_id,
        reply_markup=game_keyboard(game)
    )

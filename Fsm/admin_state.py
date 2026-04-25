from aiogram.fsm.state import State, StatesGroup

class AdminNewsletter(StatesGroup):
    '''Состояние ожидания сообщения от админа для рассылки всем пользователям бота'''
    waiting_for_message = State()

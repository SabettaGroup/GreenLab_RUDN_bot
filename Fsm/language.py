from aiogram.fsm.state import State, StatesGroup

class LanguageState(StatesGroup):
    '''Машина состояний для процесса выбора языка'''
    waiting_for_language = State() # Состояние, когда бот ждет выбора языка от пользователя
    
from aiogram.fsm.state import State, StatesGroup

class MemberState(StatesGroup):
    '''Состояние выбора отдела'''
    choosing_department = State()

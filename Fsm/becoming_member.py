from aiogram.fsm.state import State, StatesGroup

class MemberState(StatesGroup):
    choosing_department = State() # Состояние выбора отдела

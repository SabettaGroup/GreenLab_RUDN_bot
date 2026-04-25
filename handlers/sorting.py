from text import TEXTS
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards.inlinek import get_waste_main_kb, get_waste_rules_kb 


router_sort = Router()

# 1. Главное меню сортировки (после нажатия на реплай-кнопку "Сортировка мусора")
@router_sort.message(F.text.in_([
    TEXTS['ru']['keyboard_reply_buttons']['waste_sorting'],
    TEXTS['en']['keyboard_reply_buttons']['waste_sorting'],
    TEXTS['fr']['keyboard_reply_buttons']['waste_sorting']
]))
async def waste_sorting_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    text = TEXTS[lang]['wasting']['location_of_rubbish_bins']
    await message.answer(text, reply_markup=get_waste_main_kb(lang))

@router_sort.callback_query(F.data == "show_rules")
async def waste_rules(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    text = TEXTS[lang]['wasting']['how_to_handle']
    # Вызываем клавиатуру из inlinek.py
    await callback.message.edit_text(text, reply_markup=get_waste_rules_kb(lang))

@router_sort.callback_query(F.data == "back_to_plan")
async def back_to_plan(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    text = TEXTS[lang]['wasting']['location_of_rubbish_bins']
    # Возвращаем первую клавиатуру
    await callback.message.edit_text(text, reply_markup=get_waste_main_kb(lang))

@router_sort.callback_query(F.data == "back_to_main_menu")
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.delete()

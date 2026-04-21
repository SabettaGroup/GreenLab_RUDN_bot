LANGUAGES = {
    'ru': 'Русский🇷🇺',
    'en': 'English🇺🇸',
    'fr': 'Français🇫🇷',
    'de': 'Deutsch🇩🇪',
    'es': 'Español🇪🇸',
}

# Структура: TEXTS[язык][ключ]
TEXTS = {
    'ru': {
        # --- Общие тексты ---
        'welcome_message_lang':'Выберите язык\nSelect a language',
        'welcome_message': 'Здравствуйте, это бот НСО Гринлаба РУДН! Давайте начнем?',
        'error_message': 'Произошла ошибка. Пожалуйста, попробуйте позже.',
        'admin_notification_new_application': '📝 Новая заявка от пользователя:\n'
                                              'ID: {user_id}\n'
                                              'Имя: {username}\n\n'
                                              'Анкета:\n{application_data}',
        'application_created': 'Рады знакомству! Вы можете ознакомиться с нашими возможностями по кнопкам ниже',
        
        # --- Тексты для анкеты (FSM) ---
        'registration_prompt_fio': '👋 Давайте познакомимся! Пожалуйста, введите ваше ФИО:',
        'registration_prompt_faculty': ' Укажите ваш факультет и направление:',
        'registration_prompt_course_level': 'Выберите ваш уровень образования:',
        'registration_prompt_course_number': 'Выберите ваш курс:',
        'registration_prompt_experience': 'Чем Вы занимались раньше? Расскажите о своём опыте и интересах.',
        'registration_prompt_interests': 'Чем бы вы хотели заниматься сейчас?',
        'registration_confirm_data': 'Вот данные, которые вы ввели. Всё верно?',
        'registration_data_sent_to_admin': 'Ваша анкета отправлена на рассмотрение!',
        # --- Тексты для клавиатур ---
        'keyboard_levels': {
            'bachelor': 'Бакалавриат',
            'master': 'Магистратура',
            'phd': 'Аспирантура',
        },
        'keyboard_courses': {
            '1': '1 курс',
            '2': '2 курс',
            '3': '3 курс',
            '4': '4 курс',
            '5': '5 курс',
            '6': '6 курс',
        },
        'keyboard_departments': {
            'media': 'Медиа',
            'relations': 'Связи',
            'event': 'Ивент',
            'volunteer': 'Волонтёрство',
            'outdoor': 'Аутдор',
            'games': 'Игры',
            'content': 'Контент',
            'photo': 'Фото',
            'project': 'Проектный отдел',
        },
        "keyboard_reply_buttons": {
            'join_nso_button': 'Вступить в НСО',
            'become_a_member': 'стать участником',
            'become_an_org': 'стать организатором',
            'events': 'мероприятия',
            'waste_sorting': 'сортировка мусора'
        },
        'department_description_media': 'Отдел Медиа: Создаем контент, ведем соцсети...',
        'department_description_relations': 'Отдел Связи: Налаживаем партнерства...',
        # TODO: остальные описания отделов
        'become_participant_message': 'Вы можете ознакомиться с нашими возможностями!',
        'become_organizer_message': 'Чтобы стать организатором, свяжитесь с председателем НСО.\n'
                                   'Контактные данные: [Указать контакт председателя]',
        'events_prompt': 'У нас есть различные мероприятия. Выберите, какое по душе:',
        'event_example': 'Название мероприятия 1\nОписание мероприятия 1\nОбратитесь к админу',
        'sorting_prompt': 'Выберите корпус:',
        'sorting_main_corpus': 'Главный корпус',
        'sorting_ecology_corpus': 'Корпус Института Экологии',
        'sorting_waste_info': {
            'paper': 'Бумага: !',       # TODO
            'bottles': 'Бутылки: !',    # TODO
            # TODO:
        },
        'sorting_bin_location_main': 'Карта Главного корпуса', # Тут будем отправлять картинку
        'sorting_bin_location_ecology': 'Карта Корпуса Института Экологии',

    },
    'en': {
        # --- General Texts ---
        'join_nso_button': 'Join NSO',
        'error_message': 'An error occurred. Please try again later.',
        'welcome_message': 'Hello, this is the RUDN GreenLab NSO bot! Shall we get started?',
        'application_created': '✅ Your application has been created. Thank you for your interest!',
        
        # --- Registration Texts (FSM) ---
        'registration_prompt_fio': "Let's get acquainted! Please enter your Full Name:",
        'registration_prompt_faculty': 'Please specify your faculty and major:',
        'registration_prompt_course_level': 'Please select your education level:',
        'registration_prompt_course_number': 'Please select your current year:',
        'registration_prompt_experience': 'Tell us about your previous experience and interests',
        'registration_prompt_interests': 'What would you like to do now?',
        'registration_confirm_data': 'Here is the data you entered. Is everything correct?',
        'registration_data_sent_to_admin': 'Your application has been sent for review!',
        
        # --- Keyboard Texts ---
        'keyboard_levels': {
            'bachelor': 'Bachelor\'s Degree',
            'master': 'Master\'s Degree',
            'phd': 'PhD',
        },
        'keyboard_courses': {
            '1': '1st Year',
            '2': '2nd Year',
            '3': '3rd Year',
            '4': '4th Year',
            '5': '5th Year',
            '6': '6th Year',
        },
        'keyboard_departments': {
            'media': 'Media',
            'relations': 'Relations',
            'event': 'Event',
            'volunteer': 'Volunteering',
            'outdoor': 'Outdoor',
            'games': 'Games',
            'content': 'Content',
            'photo': 'Photo',
            'project': 'Project Department',
        },
        'keyboard_reply_buttons': {
            'join_nso_button': 'Join the NSO',
            'become_a_member': 'Become a member',
            'become_an_org': 'Become an organiser',
            'events': 'Events',
            'waste_sorting': 'Waste sorting'
        },

        'department_description_media': 'Media Department: We create content, manage social media...',
        'department_description_relations': 'Relations Department: We establish partnerships...',
        # TODO: other department descriptions
        'become_participant_message': 'become a member',
        'become_organizer_message': 'To become an organizer, please contact the NSO chairman.\n'
                                   'Contact details: [Insert chairman\'s contact]',
        'events_prompt': 'We have various events. Choose one you like:',
        'event_example': 'Event Name 1\nEvent Description 1\nContact the admin',
        'sorting_prompt': 'Select the building:',
        'sorting_main_corpus': 'Main Building',
        'sorting_ecology_corpus': 'Ecology Institute Building',
        'sorting_waste_info': {
            'paper': 'Paper: recycle...',       # TODO:
            'bottles': 'Bottles: recycle...',   # TODO:
           # TODO:
        },
        'sorting_bin_location_main': 'Main Building Map', 
        'sorting_bin_location_ecology': 'Ecology Institute Building Map',
    },
    
    'fr': {
    # ---основной ---
    'join_nso_button': 'Adhérer à la NSO',
    'error_message': "Une erreur s'est produite. Veuillez réessayer plus tard.",
    'welcome_message': 'Bonjour, ici le bot NSO de Greenlab RUDN ! On commence?',
    'application_created': "Votre candidature a été enregistrée. Merci de l'intérêt que vous nous portez !",
    
    # --- заполнение анкеты (FSM) ---
    'registration_prompt_fio': "Faisons connaissance ! Veuillez saisir votre nom complet:",
    'registration_prompt_faculty': "Veuillez indiquer votre faculté et votre filière:",
    'registration_prompt_course_level': "Veuillez sélectionner votre niveau d'études:",
    'registration_prompt_course_number': "Veuillez sélectionner l'année en cours:",
    'registration_prompt_experience': "Parlez-nous de votre expérience et de vos centres d'intérêt",
    'registration_prompt_interests': "Qu'est-ce que tu aimerais faire maintenant?",
    'registration_confirm_data': "Voici les données que vous avez saisies. Tout est correct?",
    'registration_data_sent_to_admin': "Ta candidature a été transmise pour examen!",
    
    # --- клавы ---
    'keyboard_levels': {
        'bachelor': 'licence',
        'master': 'Master',
        'phd': 'doctorat',
    },
    'keyboard_courses': {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
    },
    'keyboard_departments': {
        'media': 'Médias',
        'relations': 'Relations',
        'event': 'Événement',
        'volunteer': 'Bénévolat',
        'outdoor': 'Activités de plein air',
        'games': 'Jeux',
        'content': 'Contenu',
        'photo': 'Photo',
        'project': 'Département des projets',
    },

    "keyboard_reply_buttons" : {
    'join_nso_button': "Rejoindre l'NSO",
    "become_a_member": "Devenir membre",
    "become_an_org": "Devenir organisateur",
    "events": "Événements",
    "waste_sorting": "Tri des déchets"
    },

    'department_description_media': '!',
    'department_description_relations': '!',
    #TODO: other department descriptions
    'become_participant_message': 'Devenir membre',
    'become_organizer_message': "Pour devenir organisateur, veuillez contacter le président du NSO\nCoordonnées:",
    'events_prompt': 'Nous proposons divers événements. Choisissez celui qui vous plaît :',
    'event_example': 'Event Name 1\nEvent Description 1\nContact the admin',
    'sorting_prompt': 'Sélectionnez le bâtiment:',
    'sorting_main_corpus': 'Bâtiment principal',
    'sorting_ecology_corpus': "Bâtiment de l'Institut d'écologie",
    'sorting_waste_info': {
        'paper': '!',       # TODO:
        'bottles': '!',     # TODO:
        # TODO:...
    },
    'sorting_bin_location_main': 'Plan du bâtiment principal',
    'sorting_bin_location_ecology': "Plan du bâtiment de l'Institut d'écologie",
}
}

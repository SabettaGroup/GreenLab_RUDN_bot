LANGUAGES = {
    'ru': 'Русский🇷🇺',
    'en': 'English🇺🇸',
    'fr': 'Français🇫🇷',
    # 'de': 'Deutsch🇩🇪',
    # 'es': 'Español🇪🇸',
}

ADMIN_FORM_LABELS = { # Метки для анкеты, которая придет админу
            'new_submission': 'Новая заявка на вступление в НСО!',
            'fio': 'ФИО',
            'faculty': 'Факультет',
            'course_level': 'Уровень образования',
            'course_number': 'Курс',
            'experience': 'Предыдущий опыт/интересы',
            'interests': 'Чем хочет заниматься сейчас',
            'user_lang': 'Язык пользователя',
            'user_id': 'ID пользователя'
        }

# Структура: TEXTS[язык][ключ]
TEXTS = {
    'ru': {
        # --- Общие тексты ---
        'welcome_message_lang':'Выберите язык\nSelect a language',
        'welcome_message': 'Здравствуйте, это бот НСО Гринлаба РУДН!🌱\n Давайте начнем?',
        'error_message': 'Произошла ошибка. Пожалуйста, попробуйте позже.',
        'admin_notification_new_application': '📝 Новая заявка от пользователя:\n'
                                              'ID: {user_id}\n'
                                              'Имя: {username}\n\n'
                                              'Анкета:\n{application_data}',
        'application_created': 
        'Спасибо! Рады знакомству! теперь вы - часть нашего комьюнити!🫂\n скоро с вами свяжется наш ответственный, чтобы согласовать действия, а пока можете ознакомиться с нашими возможностями!',
        'already_applied': "Вы уже подали заявку. Если хотите поменять выбор, свяжитесь с ответственным\n\n@sasha_erbaeva",
        "too_many_registrations": "Вы уже заполнили анкету максимально возможное количество раз",
        # --- Тексты для анкеты (FSM) ---
        'registration_prompt_fio': '👋 Давайте познакомимся! Пожалуйста, введите ваше ФИО:',
        'registration_prompt_faculty': ' Укажите ваш факультет и направление:',
        'registration_prompt_course_level': 'Выберите ваш уровень образования:',
        'registration_prompt_course_number': 'Выберите ваш курс:',
        'registration_prompt_experience': 'Чем Вы занимались раньше? Расскажите о своём опыте и интересах.',
        'registration_prompt_interests': 'Чем бы вы хотели заниматься сейчас?',
        'registration_prompt_contacts': "📞Оставьте, пожалуйста, ваши контактные данные (подойдет корпоративная почта, юзернейм в телеграме или любой другой):",
        # 'registration_confirm_data': 'Вот данные, которые вы ввели. Всё верно?',
        # 'registration_data_sent_to_admin': 'Ваша анкета отправлена на рассмотрение!',

        'choose_dept_message': "Выберите отдел, который вам интересен:",
        'dept_actions': {'select': "✅ Выбрать отдел", 'back': "⬅️ Назад"},
        'org_actions': {'become': "🙌 Стать организатором", 'back': "⬅️ Назад"},
        'thanks_dept': "Спасибо за выбор, заявка создана! С вами свяжутся наши ответственные.",
        'organizer_promo': "Организаторы занимаются проведением мероприятий, курированием участников, управлением НСО. При подаче заявки с вами свяжутся для обсуждения. Хотите стать организатором?",
        'thanks_org': "Спасибо за стремление принимать активное участие в НСО! С вами свяжутся наши ответственные.",
       
        
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
            'become_an_org': 'стать организатором👩‍⚕️',
            'events': 'мероприятия',
            'waste_sorting': 'сортировка мусора♻️'
        },
        'department_description_media': 'Медиа отдел занимается всем тем, что вы видите в социальных сетях, - посты с красивыми картинками и завлекающими текстами. Дизайн, фигма, охваты и всё, что связано с соц сетями, - это медийщики.',
        'department_description_relations': 'Отдел связи - это связывающее звено между студентами и НСО. Здесь важно быть общительным и уметь договариваться с самыми разными людьми 🤝',
        'department_description_event': 'Хочешь быть организатором самых ярких мероприятий - тогда тебе точно сюда!🥳',
        'department_description_volunteer': 'Если ты любишь творить добро и готов брать на себя ответственность,  вступай в отдел Волонтёрства. Здесь тебя жду выезды в приюты и на субботники, участие в крутых университетских и внешних мероприятиях и много-много новых знакомств🤩.',
        'department_description_outdoor': 'Идеальная возможность увидеть не только Россию, но и мир! Твои организаторские навыки в сфере туризма точно найдут применение🌏',
        'department_description_games': 'Специальный отдел, занимающийся проведением игр, чтобы студенты могли не только проверить свои знания, но и словить полный чилл аут в уютной компании самых крутых ребят🤪',
        'department_description_photo': 'Фото - отдел, благодаря которому твоё хобби может стать чем-то большим! На мероприятиях всегда хочется всё запечатлеть на камеру, а людей хватает не всегда, поэтому мы ждём именно тебя)',
        'department_description_content': 'Контент отдел занимается съемкой роликов, монтажом и разработкой сценариев для программ короткого и длинного формата. Все видео на наших аккаунтах сделаны этим отделом.',
        'department_description_project': 'Проектный отдел занимается проектной документацией, в том числе отчетами и подачей заявок на гранты и конкурсы, а также в этот отдел входят составители интеллектуальных игр.\nИнтеллектуальные игры у нас это - ЭкоМозгобойня, ЭкоСвояк, ЭкоЧто?Где?Когда? И все они с вопросами про экологию, природу, путешествия, географию, устойчивое развитие и т.д. Раз в месяц мы проводим один из наших форматов. Участие можно принять самостоятельно (если нет команды), тогда мы подыскиваем команду для участника, и командой (до 5-6 человек).',

        'become_participant_message': 'Вы можете ознакомиться с нашими возможностями!',
        'events_prompt': 'У нас есть различные мероприятия. Выберите, какое по душе:',
        'event_example': 'Название мероприятия 1\nОписание мероприятия 1\nОбратитесь к админу',
        
        "wasting": {
            "location_of_rubbish_bins": "В корпусе института экологии баки для мусора отсортированы по этажам и классам отходов, вот их расположение:\n\n 1 этаж: пластиковые бутылки, стекло, металл.\n\n2 этаж: бумага, стекло, металл, пластиковые бутылки и крышки, батарейки.\n\n3 этаж: стекло, бумага, пластиковые бутылки и крышки, батарейки\n\nЗона Буккроссинга: чеки, ручки.",
            "how_to_handle": "Бумага:\n1) должна быть сухой\n2) очищаем от скотча, плёнки и скрепок\n3) отправляем в бак\nЧто не подходит:\n- Плотный многослойный картон \n- Тетра-пак\n- Фантики с алюминиевым покрытием\n- Чеки\n\nСтекло:\n1) Моем, сушим\n2) Убираем наклейки\n\nПластиковые бутылки PET:\n1) моем, сушим\n2) снимаем бумажные наклейки\n3) отправляем в бак\nУважаемые студенты, для данного бака не подходят вещи из трудноперерабатываемого пластика иных категорий.\n*PET - 1 категория пластика, в составе полиэтилентерефталат, самый распространенный термопластик.",
            "how_to_handle_btn": "как обращаться с отходами?",
            "back": "назад"
        },

        'placeholders': {
    'fio': "Иванов Иван Иванович",
    'faculty': "Экономический факультет",
    'experience': "Расскажите о своих проектах",
    'interests': "Что вам интересно?",
    'contacts': "@username или почта",
}

    },
    'en': {
        # --- General Texts ---
        'join_nso_button': 'Join NSO',
        'error_message': 'An error occurred. Please try again later.',
        'welcome_message': 'Hello, this is the RUDN GreenLab NSO bot!🌱\n Shall we get started?',
        'application_created': 'Thank you! It’s a pleasure to meet you! You’re now part of our community!🫂\n One of our representatives will be in touch shortly to discuss the next steps, but in the meantime, why not take a look at what we have to offer?',
        'already_applied': "ou have already submitted your application. If you wish to change your selection, please contact the person in charge\n\n@sasha_erbaeva",
        'too_many_registrations': 'You have already submitted the form the maximum number of times allowed',
        # --- Registration Texts (FSM) ---
        'registration_prompt_fio': "Let's get acquainted! Please enter your Full Name:",
        'registration_prompt_faculty': 'Please specify your faculty and major:',
        'registration_prompt_course_level': 'Please select your education level:',
        'registration_prompt_course_number': 'Please select your current year:',
        'registration_prompt_experience': 'Tell us about your previous experience and interests',
        'registration_prompt_interests': 'What would you like to do now?',
        # 'registration_confirm_data': 'Here is the data you entered. Is everything correct?',
        # 'registration_data_sent_to_admin': 'Your application has been sent for review!',
        'registration_prompt_contacts': "📞Please provide your contact details (a work email address, Telegram username or any other details will do)",

        'choose_dept_message': "Select the department you're interested in:",
        'dept_actions': {'select': "Select department", 'back': "Back"},
        'org_actions': {'become': "Become an organiser", 'back': "Back"},
        'thanks_dept': "Thank you for your selection, your application has been created! Our team will be in touch with you",
        'organizer_promo': "Organisers are responsible for running events, supervising participants and managing the NSO. Once you submit your application, we will contact you to discuss it. Would you like to become an organiser?",
        'thanks_org': "Thank you for your interest in actively participating in the NSO! Our team will be in touch with you.",    
        
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
            'become_an_org': 'Become an organiser👩‍⚕️',
            'events': 'Events',
            'waste_sorting': 'Waste sorting♻️'
        },

        'department_description_media': 'The Media Department handles everything you see on social media – posts with attractive images and engaging text. Design, Figma, reach, and everything related to social media – that’s what the media team does.',
        'department_description_relations': 'The Communications Department acts as the link between students and the Student Union. Here, it’s important to be sociable and able to negotiate with all sorts of people 🤝',
        'department_description_event': '“Want to organise the most exciting events? Then this is definitely the place for you!🥳',
        'department_description_volunteer': 'If you love doing good and are ready to take on responsibility, join the Volunteering Department. Here you can look forward to trips to animal shelters and community clean-up days, taking part in awesome university and external events, and meeting loads of new people🤩.',
        'department_description_outdoor': 'The perfect opportunity to see not just Russia, but the world! Your organisational skills in the field of tourism will definitely come in handy🌏',
        'department_description_games': 'A special department dedicated to organising games, so that students can not only test their knowledge but also have a proper chill-out in the cosy company of the coolest bunch of people🤪',
        'department_description_photo': 'The photography department, where your hobby can become something much bigger! At events, you always want to capture everything on camera, but there aren’t always enough people to do it, so we’re waiting for you)',
        'department_description_content': 'The Content Department is responsible for filming, editing and scriptwriting for both short and long-form programmes. All the videos on our accounts are produced by this department.',
        'department_description_project': 'The Projects Department handles project documentation, including reports and applications for grants and competitions, and also includes the creators of our brainteasers.\nOur brainteasers include EcoBrain Teaser, EcoTrivia, and EcoWhat?Where?When? All of them feature questions on ecology, nature, travel, geography, sustainable development, and so on. Once a month, we host one of our game formats. You can take part individually (if you don’t have a team), in which case we’ll find a team for you, or as part of a team (up to 5–6 people).',

        'become_participant_message': 'become a member',
        'events_prompt': 'We have various events. Choose one you like:',
        'event_example': 'Event Name 1\nEvent Description 1\nContact the admin',
        
        "wasting": {
            "location_of_rubbish_bins": "In the Institute of Ecology building, the waste bins are sorted by floor and waste category; here is their layout:\n\n Ground floor: plastic bottles, glass, metal.\n\nFirst floor: paper, glass, metal, plastic bottles and caps, batteries.\ n\n3rd floor: glass, paper, plastic bottles and caps, batteries\n\nBookcrossing area: receipts, pens.",
            "how_to_handle": "Paper:\n1) Must be dry\n2) Remove any tape, plastic film and paper clips\n3) Place in the bin\nWhat is not accepted:\n- Thick, multi-layered cardboard\n- Tetra Pak cartons\n- Aluminium-coated sweet wrappers\n - Receipts\n\nGlass:\n1) Wash and dry\n2) Remove labels\n\nPET plastic bottles:\n1) Wash and dry\n2) Remove paper labels\n3) Place in the bin\ nDear students, items made of hard-to-recycle plastics from other categories are not suitable for this bin.\n*PET – Category 1 plastic, composed of polyethylene terephthalate, the most common thermoplastic.",
            "how_to_handle_btn": "How should waste be managed?",
            "back": "back"
        },

        'placeholders': {
    'fio': "Margaret Thatcher",
    'faculty': "Faculty of Economics",
    'experience': "ell us about your projects",
    'interests': "What interests you?",
    'contacts': "username or email",
        }
    },
    
    'fr': {
    # ---основной ---
    'join_nso_button': 'Adhérer à la NSO',
    'error_message': "Une erreur s'est produite. Veuillez réessayer plus tard.",
    'welcome_message': 'Bonjour, ici le bot NSO de Greenlab RUDN!🌱\n On commence?',
    'application_created': "Merci! Ravis de faire votre connaissance! Vous faites désormais partie de notre communauté!🫂\n Notre responsable vous contactera prochainement pour coordonner nos actions. En attendant, n'hésitez pas à découvrir nos services!",
    'already_applied' : "Vous avez déjà déposé votre candidature. Si vous souhaitez modifier votre choix, veuillez contacter le responsable\n\n@sasha_erbaeva",
    "too_many_registrations" : "Vous avez déjà rempli le formulaire autant de fois que possible",
    # --- заполнение анкеты (FSM) ---
    'registration_prompt_fio': "Faisons connaissance ! Veuillez saisir votre nom complet:",
    'registration_prompt_faculty': "Veuillez indiquer votre faculté et votre filière:",
    'registration_prompt_course_level': "Veuillez sélectionner votre niveau d'études:",
    'registration_prompt_course_number': "Veuillez sélectionner l'année en cours:",
    'registration_prompt_experience': "Parlez-nous de votre expérience et de vos centres d'intérêt",
    'registration_prompt_interests': "Qu'est-ce que tu aimerais faire maintenant?",
    'registration_confirm_data': "Voici les données que vous avez saisies. Tout est correct?",
    'registration_data_sent_to_admin': "Ta candidature a été transmise pour examen!",
    'registration_prompt_contacts': "📞Veuillez nous communiquer vos coordonnées (adresse e-mail professionnelle, identifiant Telegram ou tout autre moyen de contact)",
    
    'choose_dept_message': "Sélectionnez le service qui vous intéresse:",
    'dept_actions': {'select': "Sélectionner un service", 'back': "back"},
    'org_actions': {'become': " Devenir organisateur", 'back': "back"},
    'thanks_dept': "Merci pour votre choix, votre candidature a été enregistrée ! Nos responsables vous contacteront.",
    'organizer_promo': "Les organisateurs s'occupent de l'organisation des événements, de l'encadrement des participants et de la gestion de l'OSN. Une fois votre candidature envoyée, nous vous contacterons pour en discuter. Souhaitez-vous devenir organisateur?",
    'thanks_org': "Merci de votre volonté de participer activement au NSO ! Nos responsables vous contacteront.",

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
    "become_an_org": "Devenir organisateur👩‍⚕️",
    "events": "Événements",
    "waste_sorting": "Tri des déchets♻️"
    },

    'department_description_media': "Le service médias s'occupe de tout ce que vous voyez sur les réseaux sociaux : les publications avec de belles images et des textes accrocheurs. Design, Figma, portée et tout ce qui touche aux réseaux sociaux : c'est le domaine des spécialistes des médias.",
    'department_description_relations': "Le département des relations est le lien entre les étudiants et l'association étudiante. Ici, il est important d'être sociable et de savoir s'entendre avec des personnes très différentes 🤝",
    'department_description_event': "Tu veux organiser les événements les plus marquants ? Alors tu es au bon endroit!🥳",
    'department_description_volunteer': "Si tu aimes faire le bien et que tu es prêt à prendre des responsabilités, rejoins le département du bénévolat. Ici, tu participeras à des sorties dans des foyers d'accueil et à des journées de nettoyage, à des événements universitaires et extérieurs géniaux, et tu feras plein de nouvelles rencontres🤩.",
    'department_description_outdoor': "L'occasion idéale de découvrir non seulement la Russie, mais aussi le monde ! Tes compétences en organisation dans le domaine du tourisme trouveront certainement leur utilité🌏",
    'department_description_games': "Un département spécial dédié à l'organisation de jeux, pour que les étudiants puissent non seulement tester leurs connaissances, mais aussi se détendre complètement en bonne compagnie avec les gens les plus sympas🤪",
    'department_description_photo': "Le département Photo : grâce à lui, ton passe-temps peut devenir bien plus qu'un simple hobby ! Lors des événements, on a toujours envie de tout immortaliser avec un appareil photo, mais on manque parfois de personnel, c'est pourquoi nous attendons justement ta candidature)",
    'department_description_content': "Le département Contenu s'occupe du tournage de vidéos, du montage et de l'élaboration de scénarios pour des programmes de format court et long. Toutes les vidéos sur nos comptes sont réalisées par ce département.",
    'department_description_project': "Le département Projets s'occupe de la documentation relative aux projets, notamment des rapports et des demandes de subventions et de participation à des concours, et comprend également les concepteurs de jeux intellectuels. \nNos jeux intellectuels sont : Éco-Casse-tête, Éco-Svojak, Éco-Quoi ? Où ? Quand ? Et toutes ces questions portent sur l'écologie, la nature, les voyages, la géographie, le développement durable, etc. Une fois par mois, nous organisons l'un de nos formats. Il est possible de participer individuellement (si vous n'avez pas d'équipe), auquel cas nous vous trouverons une équipe, ou en équipe (jusqu'à 5-6 personnes).",

    'become_participant_message': 'Devenir membre',
    'events_prompt': 'Nous proposons divers événements. Choisissez celui qui vous plaît :',
    'event_example': 'Event Name 1\nEvent Description 1\nContact the admin',
    
    "wasting": {
            "location_of_rubbish_bins": "Dans le bâtiment de l'Institut d'écologie, les poubelles sont réparties par étage et par type de déchets. Voici leur emplacement :\n\n 1er étage : bouteilles en plastique, verre, métal.\n\n2e étage : papier, verre, métal, bouteilles et bouchons en plastique, piles.\ n\n3e étage : verre, papier, bouteilles en plastique et bouchons, piles\n\nZone de bookcrossing : tickets de caisse, stylos.",
            "how_to_handle": "Papier :\n1) doit être sec\n2) retirer le ruban adhésif, les films plastiques et les trombones\n3) mettre dans le conteneur\nCe qui n'est pas accepté :\n- Carton épais multicouche\n- Tetra Pak\n- Emballages en aluminium\n - Tickets de caisse\n\nVerre :\n1) Laver, sécher\n2) Retirer les autocollants\n\nBouteilles en plastique PET :\n1) Laver, sécher\n2) Retirer les autocollants en papier\n3) Déposer dans le conteneur\ Chers étudiants, les objets en plastique difficile à recycler appartenant à d'autres catégories ne sont pas adaptés à ce conteneur.\n*PET - plastique de catégorie 1, composé de polyéthylène téréphtalate, le thermoplastique le plus répandu.",
            "how_to_handle_btn": "Comment gérer les déchets ?",
            "back": "revenir"
        },

    'placeholders': {
    'fio': "Jean-Jacques",
    'faculty': "Faculté d'économie",
    'experience': "Parlez-nous de vos projets",
    'interests': "u'est-ce qui vous intéresse?",
    'contacts': "@username ou e-mai"
    }
}
}

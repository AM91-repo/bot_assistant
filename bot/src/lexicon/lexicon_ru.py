LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\nДавай начнем работу!',
    '/help': '/help - список команд \n'
            '/start - начать работу с ботом \n'
            '/budget - раздел по работе с бюджетом \n'
            '/task - раздел по работе с задачами \n'
            '\n\nПродолжим?',
    'other_answer': 'Извини, это сообщение мне непонятно...',
    'budget_menu': {
        'start_description': '💰 Вы в разделе управления бюджетом. Выберите действие:',
        'current_budget': '💼 Текущий бюджет: {amount:.2f} ₽',
        'adjust_budget': '✏️ Введите новую сумму бюджета:',
        'history_header': '📝 Последние 10 операций:\n{operations}',
        'planning_stub': '⏳ Раздел в разработке',
        'buttons': [
            [{'text': '💼 Мой бюджет', 'callback': 'my_budget'}],
            [
                {'text': '➖ Расход', 'callback': 'add_expense'},
                {'text': '➕ Доход', 'callback': 'add_income'}
            ],
            [
                {'text': '📜 История', 'callback': 'history'},
                {'text': '📅 Планирование', 'callback': 'planning'}
            ],
            [{'text': '🔙 Назад', 'callback': 'back'}]
        ]
    }
}

# LEXICON_RU: dict[str, str] = {
#     '/start': 'Привет!\nДавай начнем работу!',
#     '/help': (
#         '/help - список команд\n'
#         '/start - начать работу с ботом\n'
#         '/budget - управление бюджетом\n'
#         '/task - задачи\n'
#         '/planner - планировщик\n'
#         '/note - блокнот\n'
#         '/friends - друзья\n'
#         '/setting - настройки\n'
#         '\nПродолжим?'
#     ),
#     'other_answer': 'Извини, это сообщение мне непонятно...',
#     'budget_actions': 'Выберите действие:',
#     'input_amount': 'Введите сумму:',
#     'operation_success': 'Операция успешно выполнена!',
#     'invalid_amount': 'Некорректная сумма!'
# }

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/help': 'Список команд',
    '/start': 'Запуск бота',
    '/budget': 'Управление бюджетом',
    '/task': 'Задачи',
    '/planner': 'Планировщик',
    '/note': 'Блокнот',
    '/friends': 'Друзья',
    '/setting': 'Настройки'
}

LEXICON_BUDGET_RU: dict = {
    'start_description': '💰 Вы в разделе управления бюджетом\nВыберите действие:',
    'current_budget': '💼 Текущий бюджет: {amount:.2f} ₽',
    'adjust_budget': '✏️ Введите новую сумму бюджета:',
    'history_header': '📝 Последние 10 операций:\n{operations}',
    'planning_stub': '⏳ Раздел в разработке'
}

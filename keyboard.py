from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

from json_content import test

BUTTON_INFO = 'Детальніше про Flugtag'
BUTTON_CHALLENGE = 'Challenge'
BUTTON_CHECK = 'Перевір себе'

CALLBACK_INFO = 'callback_info'
CALLBACK_CHALLENGE = 'callback_challenge'
CALLBACK_TEST = 'callback_test'

def get_base_reply_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(BUTTON_INFO),KeyboardButton(BUTTON_CHALLENGE), KeyboardButton('Перевір себе'))
    return markup

# INLINE CALLBACKS FOR BUTTON

CALLBACK_BUTTON_INFO = 'callback_button1_info'
CALLBACK_BUTTON_VIDEO = 'callback_button1_video'
CALLBACK_BUTTON_SEND = 'callback_button1_send'
CALLBACK_BUTTON_VIEWER = 'callback_button_viewer'

# INLINE KEYBOARD FOR CHALLENGE

CALLBACK_BUTTON_ONE = 'callback_button_one'
CALLBACK_BUTTON_TWO = 'callback_button_two'

# INLINE KEYBOARD FOR REGULATIONS

CALLBACK_BUTTON_SECURITY =  'callback_button_security'
CALLBACK_BUTTON_BUILD = 'callback_button_build'
CALLBACK_BUTTON_TEAMS = 'callback_button_teams'

CALLBACK_BUTTON_REGULATIONS = 'callback_button_regulations'

CALLBACK_BUTTON_TEST = 'callback_button_test'

CALLBACK_BUTTON_BACK_INFO = 'callback_button_back_info'
CALLBACK_BUTTON_BACK_TEST = 'callback_button_back_test'

# titles for inline button

TITLES = {
    CALLBACK_BUTTON_INFO: 'Що таке Red Bull Flugtag?',
    CALLBACK_BUTTON_VIDEO: 'Як це було в 2013?',
    CALLBACK_BUTTON_SEND: 'Хочу взяти участь',
    CALLBACK_BUTTON_VIEWER: 'Хочу бути глядачем!',
    CALLBACK_BUTTON_ONE: '#некласичнийкостюм',
    CALLBACK_BUTTON_TWO: '#самсобідавінчі',
    CALLBACK_BUTTON_SECURITY: 'Безпека',
    CALLBACK_BUTTON_BUILD: 'Будівництво',
    CALLBACK_BUTTON_TEAMS: 'Команди',
    CALLBACK_BUTTON_TEST: 'Я все знаю! Потеліли!',
    CALLBACK_BUTTON_REGULATIONS: 'Ознайомитись з правилами',
    CALLBACK_INFO: BUTTON_CHECK,
    CALLBACK_CHALLENGE: BUTTON_CHALLENGE,
    CALLBACK_TEST: BUTTON_INFO
}

def get_inline_keyboard_info():
    markup = InlineKeyboardMarkup(row_width=1)
    info_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_INFO], callback_data=CALLBACK_BUTTON_INFO)
    video_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_VIDEO], callback_data=CALLBACK_BUTTON_VIDEO)
    send_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_SEND], url='https://bit.ly/flugtagregistrations') #callback_data=CALLBACK_BUTTON_SEND)
    viewer_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_VIEWER], url='https://bit.ly/facebookFlugtag')
    markup.add(info_btn, video_btn, send_btn, viewer_btn)
    return markup

def get_inline_keyboard_challenge():
    markup = InlineKeyboardMarkup(row_width=1)
    one_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_ONE], callback_data=CALLBACK_BUTTON_ONE)
    two_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TWO], callback_data=CALLBACK_BUTTON_TWO)
    markup.add(one_btn,two_btn)
    return markup


def get_inline_keyboard_regulations(callback):
    markup = InlineKeyboardMarkup(row_width=1)
    security_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_SECURITY], callback_data=CALLBACK_BUTTON_SECURITY)
    build_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BUILD], callback_data=CALLBACK_BUTTON_BUILD)
    teams_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TEAMS], callback_data=CALLBACK_BUTTON_TEAMS)
    back_btn = InlineKeyboardButton('Повернутись назад', callback_data=callback)
    markup.add(security_btn, build_btn, teams_btn, back_btn)
    return markup


def get_inline_keyboard_test_start():
    markup = InlineKeyboardMarkup(row_width=1)
    regulation_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_REGULATIONS], callback_data=CALLBACK_BUTTON_REGULATIONS)
    test_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TEST], callback_data=CALLBACK_BUTTON_TEST)
    markup.add(test_btn, regulation_btn)
    return markup

def get_inline_keyboard_test_finish():
    markup = InlineKeyboardMarkup(row_width=1)
    send_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_SEND], url='https://bit.ly/flugtagregistrations') #callback_data=CALLBACK_BUTTON_SEND)
    viewer_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_VIEWER], url='https://bit.ly/facebookFlugtag')
    markup.add(send_btn, viewer_btn)
    return markup

# INLINE KEYBOARD FOR ADMIN
ADMIN_CALLBACK = [
    'callback_button1_info_res',
    'callback_button1_video_res',
    'callback_button_one_res',
    'callback_button_two_res',
    'callback_button_security_res',
    'callback_button_build_res',
    'callback_button_teams_res',
    'callback_button_test_res',
    'callback_info_res',
    'callback_challenge_res',
    'callback_test_res'
]


def get_inline_keyboard_admin():
    markup = InlineKeyboardMarkup(row_width=2)
    info_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_INFO], callback_data=ADMIN_CALLBACK[0])
    video_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_VIDEO], callback_data=ADMIN_CALLBACK[1])
    one_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_ONE], callback_data=ADMIN_CALLBACK[2])
    two_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TWO], callback_data=ADMIN_CALLBACK[3])
    security_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_SECURITY], callback_data=ADMIN_CALLBACK[4])
    build_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BUILD], callback_data=ADMIN_CALLBACK[5])
    teams_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TEAMS], callback_data=ADMIN_CALLBACK[6])
    test_btn = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_TEST], callback_data=ADMIN_CALLBACK[7])
    info_wel_btn = InlineKeyboardButton(TITLES[CALLBACK_INFO], callback_data=ADMIN_CALLBACK[8])
    chall_btn = InlineKeyboardButton(TITLES[CALLBACK_CHALLENGE], callback_data=ADMIN_CALLBACK[9])
    test_btn = InlineKeyboardButton(TITLES[CALLBACK_TEST], callback_data=ADMIN_CALLBACK[10])
    markup.add(info_btn, video_btn, one_btn, two_btn, security_btn, build_btn, teams_btn, test_btn, info_wel_btn, chall_btn)
    return markup

TEST_BUTTONS = ["A","B","C","D"]

def get_inline_keyboard_test(number):
    content = test[number]
    buttons = content["buttons"]

    markup = InlineKeyboardMarkup(row_width=2)
    one_btn = InlineKeyboardButton(buttons[TEST_BUTTONS[0]], callback_data=TEST_BUTTONS[0])
    two_btn = InlineKeyboardButton(buttons[TEST_BUTTONS[1]], callback_data=TEST_BUTTONS[1])
    three_btn = InlineKeyboardButton(buttons[TEST_BUTTONS[2]], callback_data=TEST_BUTTONS[2])
    four_btn = InlineKeyboardButton(buttons[TEST_BUTTONS[3]], callback_data=TEST_BUTTONS[3])
    markup.add(one_btn, two_btn, three_btn, four_btn)
    return markup
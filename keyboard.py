from strings import AKI_LANG_CODE, DEV_URL, GITHUB_URL
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('- قناه السورس .', GITHUB_URL),
            InlineKeyboardButton('- المطور .', DEV_URL)   
        ]
    ]
)

#Shows a bunch of buttons to change the language of the Akinator when playing.
AKI_LANG_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(AKI_LANG_CODE['en'], callback_data='aki_set_lang_en'),
            InlineKeyboardButton(AKI_LANG_CODE['ar'], callback_data='aki_set_lang_ar'),
            InlineKeyboardButton(AKI_LANG_CODE['cn'], callback_data='aki_set_lang_cn'),
            InlineKeyboardButton(AKI_LANG_CODE['de'], callback_data='aki_set_lang_de')
         ],
         [
            InlineKeyboardButton(AKI_LANG_CODE['es'], callback_data='aki_set_lang_es'),
            InlineKeyboardButton(AKI_LANG_CODE['fr'], callback_data='aki_set_lang_fr'),
            InlineKeyboardButton(AKI_LANG_CODE['il'], callback_data='aki_set_lang_il'),
            InlineKeyboardButton(AKI_LANG_CODE['it'], callback_data='aki_set_lang_it')
         ],
         [
            InlineKeyboardButton(AKI_LANG_CODE['jp'], callback_data='aki_set_lang_jp'),
            InlineKeyboardButton(AKI_LANG_CODE['kr'], callback_data='aki_set_lang_kr'),
            InlineKeyboardButton(AKI_LANG_CODE['nl'], callback_data='aki_set_lang_nl'),
            InlineKeyboardButton(AKI_LANG_CODE['pl'], callback_data='aki_set_lang_pl')
         ],
         [
            InlineKeyboardButton(AKI_LANG_CODE['pt'], callback_data='aki_set_lang_p'),
            InlineKeyboardButton(AKI_LANG_CODE['ru'], callback_data='aki_set_lang_ru'),
            InlineKeyboardButton(AKI_LANG_CODE['tr'], callback_data='aki_set_lang_tr'),
            InlineKeyboardButton(AKI_LANG_CODE['id'], callback_data='aki_set_lang_id')
         ],

    ]
)

#Child Mode enable/disable Buttons
CHILDMODE_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Enable", callback_data='c_mode_1'),
            InlineKeyboardButton("Disable", callback_data='c_mode_0')
        ]
    ]
)


AKI_PLAY_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- نعم .", callback_data='aki_play_0'),
            InlineKeyboardButton("- لا .", callback_data='aki_play_1'),
            InlineKeyboardButton("- من المحتمل .", callback_data='aki_play_3')
        ],
        [
            InlineKeyboardButton("- لا اعلم .", callback_data='aki_play_2'),
            InlineKeyboardButton("- علي الاغلب لا .", callback_data='aki_play_4')
        ],
        [   InlineKeyboardButton("- العوده .", callback_data= 'aki_play_5')
        ]
    ]
)

AKI_WIN_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- نعم .", callback_data='aki_win_y'),
            InlineKeyboardButton("- لا .", callback_data='aki_win_n'),
        ]
    ]
)


AKI_LEADERBOARD_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Total Guesses", callback_data='aki_lead_tguess'),
            InlineKeyboardButton("Correct Guesses", callback_data='aki_lead_cguess'),
        ],
        [
            InlineKeyboardButton("Wrong Guesses", callback_data='aki_lead_wguess'),
            InlineKeyboardButton("Total Questions", callback_data='aki_lead_tquestions'),
        ]
    ]
)
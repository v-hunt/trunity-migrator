#####################################################
#                  EXAMPLE OF CONF FILE
# Attention!! The following settings must be filled
# before running this script!
#####################################################

# set here your user name and password:
TRUNITY_2_LOGIN = "my-trunity-2-login"
TRUNITY_2_PASSWORD = "secret"

TRUNITY_3_LOGIN = "my-trunity-3-login"
TRUNITY_3_PASSWORD = "verysecret"

# the name of Trunity book you need to import:
TRUNITY_2_BOOK_NAME = "Integrating Concepts in Biology"
TRUNITY_3_BOOK_NAME = "Integrating Concepts in Biology v13"

# All of these content types will be imported.
# You may comment out what you don't need:
CONTENT_TYPES = [
    "article",
    # "questionpool",
    # "exam"
    # "news",
    # "video",
    # "podcast",
    # "gallery",
    "game",
    # "assignment",
    # "whitepaper",
    # "casestudy",
    # "presentation",
    # "lecture",
    # "exercise",
    # "teachingunit",
]




TRUNITY_2_API_ENDPOINT = "http://api.trunity.net/v1/"
# TRUNITY_2_API_ENDPOINT = "http://api2.trunity.net/v1/"


TRUNITY_2_APP_CODE = 'your-app-code'


###############################################################################
#                           FIXERS SETTINGS
###############################################################################


# this will be added to all 'src' urls
STATIC_URL = 'http://www.trunity.net'
IMG_BASE_URL = 'http://www.trunity.net'


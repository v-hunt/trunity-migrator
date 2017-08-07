#####################################################
#                  EXAMPLE OF CONF FILE
# Attention!! The following settings must be filled
# before running this script!
#####################################################

# set here your user name and password:
TRUNITY_2_LOGIN = ""
TRUNITY_2_PASSWORD = ""

TRUNITY_3_LOGIN = ""
TRUNITY_3_PASSWORD = ""

# the name of Trunity book you need to import:
TRUNITY_2_BOOK_NAME = "Integrating Concepts in Biology"
TRUNITY_3_BOOK_NAME = "Integrating Concepts in Biology v11"

# this will be added to all 'src' urls
STATIC_URL = 'http://www.trunity.net'

# All of these content types will be saved.
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




#-------- STRING CONSTANTS ----------------
TRUNITY_2_API_ENDPOINT = "http://api.trunity.net/v1/"
# TRUNITY_2_API_ENDPOINT = "http://api2.trunity.net/v1/"


TRUNITY_2_APP


# -------------- Fixers -----------------

IMG_BASE_URL = 'http://www.trunity.net'


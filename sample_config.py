HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["6928080871:AAEmsJAKf6hGUpW6PasVwYXHJ3bX_ESfj98"]
    ARQ_API_KEY = environ["ILYCNX-RECXOD-FJPPJI-ZELJVI-ARQ"]
    LANGUAGE = environ["LANGUAGE = "en" "]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
    ARQ_API_KEY = "Get this from @ARQRobot"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"

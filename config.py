#config options
BOT_USER_ID = 0 #e: 123456789012345678
ALLOWED_CHANNELS = [""] #e: [000000000000000000, 000000000000000001, 000000000000000002]
CLIENT_TOKEN = "" #e: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._12345"

#ignore
missing_info = False

if BOT_USER_ID == 0:
    print("You have not provided your bot's user id! Please provide one in config.py file.")
    missing_info = True

if ALLOWED_CHANNELS == [""]:
    print("You have not selected what channels your bot will be operating on! Please provide at least one in config.py file.")
    missing_info = True

if CLIENT_TOKEN == "":
    print("You have not provided your bot's client token! Please provide one in config.py file.")
    missing_info = True

if missing_info == True:
    a = input('Press enter to exit ...\n')
    exit(0)

# Movie Reviewer Discord Bot!

This bot was created with the purpose of helping friends **review movies** on discord. When an image is posted in a selected channel, the bot will add 5 reactions to it. After a new reaction from a user, the bot will remove double votes and calculate the average score.

## Get started:
To get started, you first need to modify the **<span>config</span>.py** file with the required parameters as in the exemple below:

    BOT_USER_ID = 795736328632270899
    ALLOWED_CHANNELS = [805931582149099600, 4159525192383725001]
    CLIENT_TOKEN = "zgz4TUGlhIt7AU8uUhbZmXpAkik40A6MTtc8ft3WaIAjbHoZCZ0xvmoQIVh"

**Do not share your CLIENT_TOKEN with anyone, this will give them full access to control your bot.**
<br>

Make sure you also have installed all dependencies listed in **requirements.txt** file:

    aiohttp==3.7.4.post0
    async-timeout==3.0.1
    attrs==21.4.0
    chardet==4.0.0
    discord.py==1.7.3
    idna==3.3
    multidict==6.0.2
    yarl==1.7.2

To install all the dependencies automatically, run the following command in terminal:

    $ pip install -r requirements.txt

Make sure you are in the right directory before running this command, change directories with:

    $ cd path/to/movie-reviewer-discord-bot
Be aware, this will install the dependencies in the system directory, if you do not wish that to happen, check out [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

## Launching bot
To start the bot, run the **<span>reaction.py</span>** file, you can accomplish by either double-clicking on the file or by running one of the following commands:

    $ python reaction.py
</br>

    $ python3 reaction.py
</br>

If everything went right, you should get the following output:

![enter image description here](https://s7.gifyu.com/images/launching_bot_cropped.gif)

## Adding image
 Once the bot is running, you just need to **send an image** you want the bot to react in a selected channel (view **<span>config</span>.py**), make sure the image you are sending is either a **png** or **jpg/jpeg** file.
 </br>

 ![enter image description here](https://s7.gifyu.com/images/sending_pic_bot_gif.gif)
## Average score
The bot will automatically **calculate the average score** and say it on the chat. When a new reaction is added, the score is recalculated and **the message is edited** no matter its position in the channel history.
</br>

![enter image description here](https://s7.gifyu.com/images/calculating_average_bot.gif)
## Double vote
To avoid double votes, when a new reaction is added, the bot scan the message and remove any reactions from the same user.
</br>

![enter image description here](https://s7.gifyu.com/images/double_vote_bot.gif)

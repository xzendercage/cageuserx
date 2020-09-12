# CAGE USER X

<p align="center">
<img src="https://telegra.ph/file/2c62695e201c3efe17289.jpg" alt="USERX USER">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![forthebadge made-with-swag](https://forthebadge.com/images/badges/built-with-swag.svg)
![forthebadge work-in-my-machine](https://forthebadge.com/images/badges/works-on-my-machine.svg)



Best User Bot To Manage Your Telegram Account 
## Most PowerFul And Better And Secure

## © By 彡Xzͥenͣdͫer Cage彡™


### Host USERX In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/xzendercage/cageuserx)

## Telegram-String

[![Run on Repl.it](https://repl.it/badge/github/CAGEGANG/USERX)](https://cagestring.xzendercage.repl.run/)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/xzendercage/cageuserx
cd cageuserx
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.


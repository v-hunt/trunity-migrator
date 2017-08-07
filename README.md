# Trunity Migrator

The app that allows to migrate learning content from Trunity 2 to Trunity 3 LMS


## Installation

We recommend to use virtual environment. Install and activate it:

```
virtualenv --python=python3.5 .env
source .env/bin/activate
```

Than install the package:

```
pip install trunity-migrator
```


## Usage

First you need to create a settings.py file with all settings
that you need. As an example you can copy [this file](https://raw.githubusercontent.com/v-hunt/trunity-migrator/master/trunity_migrator/settings.py)

So you can copy it into your system and use as a template:

```
wget https://raw.githubusercontent.com/v-hunt/trunity-migrator/master/trunity_migrator/settings.py
```


Fill all the required settings. Then you may start the migration process:

```
trunity-migrator /path/to/settings.py
```

Pay a special attention that `/path/to/settings.py` should be a absolute path.
Otherwise the script won't work.


### HTML Fixers

You can apply html fixers to fix html issues. Each of fixers
mentioned in settings will be applied to each article (or another content
type).

See `FIXERS SETTINGS` section in example settings file.

**Implemented fixers:**

* `fix_img_src` --
Search for all \<img\> tags and add the scheme part for src if src is
    not the absolute url. Required parameters: `base_url`

* `fix_table_width` -- search for tables and change  'width' attribute

```shell
       __  _                                                       __  _       __
  ____/ / (_)___ _____  ____ _____      ___  _____________  ____  / /_(_)___ _/ /
 / __  / / / __ `/ __ \/ __ `/ __ \    / _ \/ ___/ ___/ _ \/ __ \/ __/ / __ `/ /
/ /_/ / / / /_/ / / / / /_/ / /_/ /   /  __(__  |__  )  __/ / / / /_/ / /_/ / /
\__,_/_/ /\__,_/_/ /_/\__, /\____/____\___/____/____/\___/_/ /_/\__/_/\__,_/_/
    /___/            /____/     /_____/

```
### proved by a step by step the potential and flexibility of the framework for developing web applications and APIs

* Python version: 3.5.0
* Django: 1.9
* Environment: GNU/Linux

## The project is divided into none steps

### Step Zero or prepare to walk

#### Install project dependencies
```shell
sudo apt-get install -y make build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev
```

#### Install pyenv
```shell
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

#### Put these lines on your $HOME/.bashrc (similar file depending on your distribution)
```shell
export PATH="/home/vagrant/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

#### Persist your changes
```shell
source ~/.bashrc
```
#### Install version 3.5.0
```shell
pyenv install 3.5.0
```
#### Version 3.5.0 to set as global
```shell
pyenv global 3.5.0
```

#### To begin we will clone the project
```shell
git clone git@github.com:neldevfull/django_api.git
```

### Step one
In step one, you have to create a minimum viable project done in Django, the files are in the directory 'stepone' and they can be used as templates for your new project django API

* Create environment variables

```shell
export DEBUG=off
```

```shell
export ALLOWED_HOSTS=localhost
```

* To run the project installs the dependencies and run the server

```shell
cd stepone
```
```shell
pip install -r requirements
```
```shell
gunicorn manage
```

* You can use stepone as a template to start another project

```shell
django-admin.py startproject foo --template=stepone
```

### Step two
In step two, it was included logic to create the rendering of an image according to the parameters passed in the URL, as was also developed the static part of the application, homepage

* Installs new dependencies

```shell
cd ../steptwo
```
```shell
pip install -r requirements
```
Obs: See the Pillow library was installed

You can access the project using your favorite browser and play with imaging
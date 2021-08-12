# Geo Calculate

The App for calculating the distance between Moscow Ring Road to specific adresses

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

<!-- * Python 3.9.1

visit [here](https://realpython.com/installing-python/) to read more about python installation

```shell-script
$ python --version
Python 3.9.1
``` -->

#### Python and virtual environment

- Using pyenv to manage python version and python virtualenv as virtual environment

  1.  Install pyenv
      visit [here](https://github.com/pyenv/pyenv) to read more about pyenv installation

          ```shell
          $ pyenv --version
          pyenv 1.2.16-5-g7097f820
          ```

  2.  Install Python 3.9.1 on pyenv

      ```shell
      $ pyenv install 3.9.1
      Downloading Python-3.9.1.tar.xz...
      -> https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tar.xz
      Installing Python-3.9.1...
      Installed Python-3.9.1 to /home/muhazrisofyan/.pyenv/versions/3.9.1
      ```

  3.  Use pyenv python 3.9.1 as global python

      ```shell
      $ pyenv global 3.9.1
      -
      ```

  4.  Install python virtualenv and activate the virtualenv

      ```shell
      $ pip install virtualenv
      Collecting virtualenv...
      $ virtualenv venv
      created virtual environment...
      $ source venv/bin/activate
      (venv) $
      ```

### Installing dependencies and run the app

1. Make sure your virtualenv is activated

   ```shell
   (venv) $ which python
   /path/to/your/venv/bin/python
   ```

2. Copy env example file and adjust it with your needs
   In this repo we provide the example file of the env file, you can copy from that example and adjust it.

   ```shell
   (venv) $ cp .env.example .env
   -
   ```

3. Create logs folder

   ```shell
   (venv) $ mkdir logs
   ```

4. Installing pip dependencies

   Installing pip dependencies using requirements.txt

   ```shell
   (venv) $ pip install -r requirements.txt
   Collecting autopep8...
   ```

5. Running development server

   ```shell
   (venv) $ flask run
   * Serving Flask app "app" (lazy loading)
   * Environment: development
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 503-733-148
   ```

## Running the tests

Test Driven Development using python unittest. All the test code is below tests folder, there is unittest folder.

1. Coverage command

   To run all test using make coverage command

   ```shell
   (venv) $ make coverage
   python -m coverage run -m unittest discover -v
   test_should_return_float_value (tests.unittest.controllers.test_home.TestHome) ... ok
   test_should_return_none (tests.unittest.controllers.test_home.TestHome) ... ok
   test_validate_an_empty_value (tests.unittest.controllers.test_home.TestHome) ... ok

   ----------------------------------------------------------------------
   Ran 3 tests in 2.405s

   OK
   ```

#### Docker and docker-compose

Use docker and docker-compose for running the application

1. Install Docker and docker-compose
   visit [here](https://docs.docker.com/) to read more about docker installation

   ```shell
   $ docker --version
   Docker version 19.03.3, build a872fc2f86

   $ docker-compose --version
   docker-compose version 1.24.1, build 4667896b
   ```

2. Copy .env.example

   ensure you have provided the environtment variables that needed inside .env.example

   ```shell
   $ cp .env.example .env
   ```

3. Try to run the application

   ```shell
   $ cd path/to/your/root/app
   $ docker-compose up
   ```

4. Try to run all test using make coverage command

   ```shell
   $ cd path/to/your/root/app
   $ docker-compose run web make coverage
   ```

5. Rebuild docker-compose when you have updated code

   ```shell
   $ cd path/to/your/root/app
   $ docker-compose up --build
   ```

## Logging

The post request of get distance will be logged in logs/results.log

## Authors

- **Saeful Millah** - _Initial work_

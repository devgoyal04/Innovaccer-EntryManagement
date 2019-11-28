# Entry-Management Software
This application is built on Python Django framework which captures the details the of visitor and host on the front-end and at 
the back-end once the user enters the information in the form, the back-end stores all of the information with also the time
stamp of the entry. Which also triggers E-Mail and SMS to the host informing him of the details of the visitor. Fast2sms and 
smtp server is used to send SMS and E-Mail respectively. And, when the user checks-out he should get an E-Mail with the complete
form which includes.
1. Name
2. Phone
3. Check-in time
4. Check-out time
5. Host name
6. Address visited.

## Getting Started
1. Clone the repository using ```git clone```
```bash
https://github.com/devgoyal04/Innovaccer-EntryManagement.git
```
2. ```cd``` into the project directory and run
```bash
pip install -r requirements.txt
```

## Prerequisites
1. [pip](https://pip.pypa.io/en/stable/) and python should be installed on your environment.
2. You should have a gmail account.

## Installation
### pip
```bash
sudo apt install python-pip
```
verify the installation by
```bash
pip --version
```

## Running the Server
1. Open ```settings.py``` in the ```/src/entry_management``` directory and replace your gmail id and password in the 
**EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD** fields respectively.
> allow access for less secure apps in your gmail account [here](https://myaccount.google.com/lesssecureapps).
 
2. Open terminal ```cd``` into ```/src``` folder and run.
```bash
python manage.py runserver
```
The local server will be up, browse to [localhost:8000](http://localhost:8000) to see the app running

## Tech Stack
* [Django](https://www.djangoproject.com/) - Python framework
* [SQLite3](https://www.sqlite.org/index.html)
* HTML, CSS, Bootsrap



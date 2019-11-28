# Entry-Management Software
This application is built on Python Django framework which captures the details the of visitor and host on the front-end and at the back-end once the user enters the information in the form, the back-end stores all of the information with also the time stamp of the entry. Which also triggers E-Mail and SMS to the host informing him of the details of the visitor. Fast2sms and smtp server is used to send SMS and E-Mail respectively. And, when the user checks-out he should get an E-Mail with the complete form which includes.
1. Name
2. Phone
3. Check-in time
4. Check-out time
5. Host name
6. Address visited. 

The Project is hosted on pythonanywhere here [devgoyal04.pythonanywhere.com](devgoyal04.pythonanywhere.com)

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

## Aproach
* A visitor is given the option of check-in and check-out.
* At the time of check-in, Visitor is asked to fill in the details of himself and the Host which will be informed to him via Email and SMS.
* After check-in Visitor can check-out when his meeting with the host is over.
* At the time of checkout, Visitor is asked to provide his EMail Id which he used at the time of check-in.
* After check-out Visitor will be sent an Email with the full information containing also the time stamps of check-in and check-out.

## Validations
* A Visitor cannot check-in again if he/she is already checked-in and has not checked-out.
* A visitor cannot check-out again if he has already checked-out.
* A Visitor cannot check-out before he checks-in.

## Screenshots
Screenshots of Host/Visitor Emails and SMS are in Screenshots folder

## Author
**Dev Goyal**


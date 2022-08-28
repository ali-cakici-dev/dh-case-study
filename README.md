
## Introduction
This repo is an basic implementation of url shortener like bitly with Flask.

## Quick Start

<details>
<summary>Installation</summary>

Step1. Install repo from source.
```shell
git clone https://github.com/alicakici1234/dh-case-study.git
```

Step2. Create virtual environment.
```shell
cd dh-case-study
python -m venv ./venv

## for windows:
cd venv/Scripts/
activate

## for linux
source venv/bin/activate
```
Step3. Install required libraries
```shell
pip3 install -r requirements.txt
```

</details>

<details>
<summary>Demo</summary>

Step1. Create database 
```shell
flask createDB
```

Step2. run flask server

```shell
flask run
```

</details>

<details>
<summary>Insert a website to be shortened</summary>

* Option1. Using url
visit http://127.0.0.1:5000/addUrl/{urlToBeAdded}

* Option2. With rest request
POST {"url": urlToBeAdded} to http://127.0.0.1:5000/addUrl

This will return shortened url in response body.text 
</details>


<details>
<summary>Redirection from shortened url</summary>

GET http://127.0.0.1:5000/{shortenedUrl}

This will redirect to original url

</details>


<details>
<summary>Get all shortened Urls</summary>

GET http://127.0.0.1:5000/getAll

This will return list of urls with url, shortened url and visit counter.

</details>

## Deployment on heroku

1. Connect github repository to heroku with auto-deployment
2. Add plugin for postgre
3. From heroku console create db
```shell
flask createDB
```
4. Deploy manually.
5. To delete db:
```shell
flask dropDB
```

## Live Heroku demo

* Check if server online
https://dh-case-study.herokuapp.com/isOnline

* Add Original Url to be Shortened
https://dh-case-study.herokuapp.com/addUrl/www.mytest.com
 This will return shortened url -> shortenedUrl

* Redirection from shortened url:
https://dh-case-study.herokuapp.com/shortenedUrl

* Get All Urls:
https://dh-case-study.herokuapp.com/getAll

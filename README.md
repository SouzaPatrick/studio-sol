## Valid password - Studio Sol
## Requirements to run the project
- Docker
- Docker-compose
- Possibility to run make

## Starting project
To start the project and install all the dependencies on your machine, just run:
```bash
make install
```

## Expected result

List the last 100 logs from the flask container:
```bash
make log
flask-python-sample  |  * Serving Flask app 'app'
flask-python-sample  |  * Debug mode: off
flask-python-sample  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
flask-python-sample  |  * Running on all addresses (0.0.0.0)
flask-python-sample  |  * Running on http://127.0.0.1:5000
flask-python-sample  |  * Running on http://172.22.0.2:5000
flask-python-sample  | Press CTRL+C to quit
```

After the application starts, navigate to `http://localhost:5000/verify` in your web postman or run:
```bash
curl --location --request POST 'http://localhost:5000/verify' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=iGcHNLTZCfmv0QCgmVJe5pvnOAbpSMpO4AzN5fM9AKE63kKtx554im3layMdiFqX; sessionid=fvbgx3ff7re73c8erxmo13387w1x7hqu' \
--data-raw '{
    "password": "T2eesteSenhaForte!123&",
    "rules": [
        {"rule": "minSize","value": 8},
        {"rule": "minSpecialChars","value": 10},
        {"rule": "noRepeted","value": 1},
        {"rule": "minDigit","value": 0},
        {"rule": "minUppercase","value": 2},
        {"rule": "minLowercase","value": 4}
    ]
}'
```
Response:
```bash
{
    "noMatch": [
        "noRepeted"
    ],
    "verify": false
}
```

### Run tests
```bash
make test
```

###### Ps: The container must be running because the test checks if it is up and then runs the tests inside. To upload the container just type the command ```make up```

### Stop and remove the containers
```bash
make down
```
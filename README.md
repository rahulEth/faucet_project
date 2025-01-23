# About The Project

This assignment is to develop a simple faucet application, allows customers to receive Sepolia ETH for free.

## Dependencies 

- docker, docker-compose, python


# Setup Instructions

1. clone this repo

```
git clone https://github.com/rahulEth/faucet_project.git

```

2. create .env

```
cp .env.example .env

```

3. setup all the environment variables and fund the wallet associated with PRIVATE_KEY

4. create migration

```
python3 manage.py makemigrations
python3 manage.py migrate

```

5. run container
```
   docker-compose up --build
```
Starting development server at http://0.0.0.0:8000/

6. calling POST /faucet/fund API
```
    POST : http://localhost:8000/faucet/fund/
    {
       "wallet_address": "0xfa5956B70514eE7273b1Af5D34454E9100cF40C8"
    }

    Result: 
    {
       "transaction_id": "0x28771f272481cdaeb4923ec298de4848adc6e630c12c68df1f866de0265171ff"
    }
   
```

7. calling GET /faucet/stats API
```
    GET : http://localhost:8000/faucet/stats/
    Result: 
    {
        "successful_transactions": 10,
        "failed_transactions": 0
    }
   
``` 
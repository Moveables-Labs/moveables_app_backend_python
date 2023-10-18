﻿# Moveables App Backend Python API

## Usage

Go to the Contribution page and follow the Installation and Usage steps. When you have a running server that runs on \
`http://localhost:5000/` in your local machine, you can start performing your request to the database using the api.
*******************************************************************************************************************************************************************
## USERS
Create Users Url `/user/movableuser/create` the Id for the user is authomatically created.
```
{
	'firstName' : <firstName>,
	'surname' : <surname>,
	'email' : <example@email.com>,
	'state' : <state>,
	'deliveryAddress' : <deliveryAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
Update Users Url `/user/movableuser/update/userid=<string:id>`\
```
{
	'firstName' : <firstName>,
	'surname' : <surname>,
	'email' : <example@email.com>,
	'state' : <state>,
	'deliveryAddress' : <deliveryAddress>,
	'phoneNumber' : <phoneNumber>,
}
```

Get All Users Url `/user/movableuser/all`. This returns a list of user in JSON format.\
Get Specific Users Url `/user/movableuser/get/userid=<string:id>`. This returns a user in JSON format.\
Get Specific Users Url `/user/movableuser/delete/userid=<string:id>`. This will delete the user with the specific id from the database. But not from the Authentication.
*******************************************************************************************************************************************************************
## PROVIDERS
Create Users Url `/provider/providermovableuser/create` the Id for the user is authomatically created.
```
{
	'companyName' : <companyName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'companyAddress' : <deliveryAddress>,
	'phoneNumber' : <phoneNumber>,
	'compaDeliveryMethod' : <companyDeliveryMethod>,
}
```
Update Users Url `/provider/providermovableuser/update/userid=<string:id>`\
```
{
	'companyName' : <companyName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'companyAddress' : <deliveryAddress>,
	'phoneNumber' : <phoneNumber>,
	'compaDeliveryMethod' : <companyDeliveryMethod>,
}
```
Get All Users Url `/provider/providermovableuser/all`. This returns a list of user in JSON format.\
Get Specific Users Url `/provider/providermovableuser/get/userid=<string:id>`. This returns a user in JSON format.\
Delete Specific Users Url `/provider/providermovableuser/delete/userid=<string:id>`. This will delete the user with the specific id from the database.
*******************************************************************************************************************************************************************
## AUTHROZATION
* Sign up and create an authrization for a User. Url : ` /auth/signup` Body : `{'email' : <example@email.com>, 'password' : <password>}`

* Sign up and create an authrization for a User. Url : ` /auth/signupwithdata`
```
{
	'firstName' : <firstName>,
	'surname' : <surname>,
	'email' : <example@email.com>,
	'state' : <state>,
	'deliveryAddress' : <deliveryAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
##### NOTE : Use the second method when creating a user because this will authomatically create and ID and also save the user password that you can access later in the code
*******************************************************************************************************************************************************************
##### All request using the api also returns a body of `{'status' : <bool>, 'message' : <string>, 'data' : <json_responce>}`. From this responce you can tell the success or failiure of the request

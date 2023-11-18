# Movables App Backend Python API

## Usage

Go to the Contribution page and follow the Installation and Usage steps. When you have a running server that runs on \
`http://localhost:5000/` in your local machine, you can start performing your request to the database using the api.
*******************************************************************************************************************************************************************
## USERS
Create Users Url `/user/movablesuser/create` the Id for the user is automatically created.
```
{
	'firstName' : <firstName>,
	'lastname' : <lastName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'phoneNumber' : <phoneNumber>,
}
```
Update Users Url `/user/movablesuser/update/userid=<string:id>`\
```
{
	'firstName' : <firstName>,
	'lastName' : <lastName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'phoneNumber' : <phoneNumber>,
}
```

Get All Users Url `/user/movablesuser/all`. This returns a list of user in JSON format.\
Get Specific Users Url `/user/movablesuser/get/userid=<string:id>`. This returns a user in JSON format.\
Get Specific Users Url `/user/movablesuser/delete/userid=<string:id>`. This will delete the user with the specific id from the database. But not from the Authentication.
*******************************************************************************************************************************************************************
## PROVIDERS
Create Users Url `/provider/movablesprovider/create` the Id for the user is automatically created.
```
{
	'companyName' : <companyName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'companyAddress' : <companyAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
Update Users Url `/provider/movablesprovider/update/userid=<string:id>`\
```
{
	'companyName' : <companyName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'companyAddress' : <companyAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
Get All Users Url `/provider/movablesprovider/all`. This returns a list of user in JSON format.\
Get Specific Users Url `/provider/movablesprovider/get/userid=<string:id>`. This returns a user in JSON format.\
Get Specific Users Url `/provider/movablesprovider/delete/userid=<string:id>`. This will delete the user with the specific id from the database.
*******************************************************************************************************************************************************************
## AUTHORIZATION
### User
* Log in a User is a PUT request. Url : ` /auth/loginuser`
* Log Out a User is a PUT request. Url : ` /auth/logoutuser`
* Sign up and create an authorization for a User. Url : `/auth/signupuser`
### Provider
* Log in a User is a PUT request. Url : ` /auth/loginprovider`
* Log Out a User is a PUT request. Url : ` /auth/logoutprovider`
* Sign up and create an authorization for a Provider. Url : ` /auth/signupprovider`
```
{
	'firstName' : <firstName>,
	'lastName' : <lastNname>,
	'email' : <example@email.com>,
	'state' : <state>,
	'phoneNumber' : <phoneNumber>,
}
```
##### NOTE : Use the second method when creating a user because this will automatically create and ID and also save the user password that you can access later in the code
*******************************************************************************************************************************************************************
## EMAIL VERIFICATION
Verifying Email is straight forward using this api Url : `/auth/verify_email/receiver_email=<string:receiver_email>` A five-digit code is sent to the receiver email, and a response is returned if successfully.
```
{
    "data": {
        "code": <code>,
        "reciveremail": <email>
    },
    "message": "Email sent successfully",
    "status": true
}
```
On the event that the email was not successful an error response is returned
```
{
	"status": False, 
	"message": f"An Error Has Occured: {e}",
	"data": {}}
}
```
*******************************************************************************************************************************************************************
##### All request using the api also returns a body of `{'status' : <bool>, 'message' : <string>, 'data' : <json_responce>}`. From this response you can tell the success or failure of the request

**********************************************************************************

> ### CREATING USER FLOW
> ##### User Enters Email and password -> Send Verification Code -> Verify User Code ->Sign Up User and Create User Database
*********************************************************************************

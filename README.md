# Moveables App Backend Python API

## Usage

Go to the Contribution page and follow the Installation and Usage steps. When you have a running server that runs on \
`http://localhost:5000/` in your local machine, you can start performing your request to the database using the api.
*******************************************************************************************************************************************************************
## USERS
Create Users Url `/user/movableuser/create` the Id for the user is authomatically created.
```
{
	'firstName' : <firstName>,
	'lastname' : <lastName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'phoneNumber' : <phoneNumber>,
}
```
Update Users Url `/user/movableuser/update/userid=<string:id>`\
```
{
	'firstName' : <firstName>,
	'lastName' : <lastName>,
	'email' : <example@email.com>,
	'state' : <state>,
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
	'companyAddress' : <companyAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
Update Users Url `/provider/providermovableuser/update/userid=<string:id>`\
```
{
	'companyName' : <companyName>,
	'email' : <example@email.com>,
	'state' : <state>,
	'companyAddress' : <companyAddress>,
	'phoneNumber' : <phoneNumber>,
}
```
Get All Users Url `/provider/providermovableuser/all`. This returns a list of user in JSON format.\
Get Specific Users Url `/provider/providermovableuser/get/userid=<string:id>`. This returns a user in JSON format.\
Get Specific Users Url `/provider/providermovableuser/delete/userid=<string:id>`. This will delete the user with the specific id from the database.
*******************************************************************************************************************************************************************
## AUTHROZATION
* Sign up and create an authrization for a User. Url : ` /auth/signup` Body : `{'email' : <example@email.com>, 'password' : <password>}`

* Sign up and create an authrization for a User. Url : ` /auth/signupuser`
* Sign up and create an authrization for a Provider. Url : ` /auth/signupprovider`
```
{
	'firstName' : <firstName>,
	'lastName' : <lastNname>,
	'email' : <example@email.com>,
	'state' : <state>,
	'phoneNumber' : <phoneNumber>,
}
```
##### NOTE : Use the second method when creating a user because this will authomatically create and ID and also save the user password that you can access later in the code
*******************************************************************************************************************************************************************
## EMAIL VERIFICATION
Verifying Email is straight forword usint this api Url : `/auth/verifyemail/recivermail=<email>` A five digit code is sent to the reciever email, and a responce is returned if successfull.
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
On the event that the email was not successful an error responce is returned
```
{
	"status": False, 
	"message": f"An Error Has Occured: {e}",
	"data": {}}
}
```
*******************************************************************************************************************************************************************
##### All request using the api also returns a body of `{'status' : <bool>, 'message' : <string>, 'data' : <json_responce>}`. From this responce you can tell the success or failiure of the request

**********************************************************************************

> ### CREATING USER FLOW
> ##### User Enters Email and password -> Send Verification Code -> Verify User Code ->Sign Up User and Create User Database
*********************************************************************************

# HOODS
A web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts

## By tumaa
A student at Moringa School and an aspiring software developer.

## Specifications
* Users can sign up to use the application
* Users can set up a profile with a location and neighbourhood
* Users can find a list of business in the neighbourhood
* Users can find contact of health department and police authorities
* Users can post updates and are visible to neighbours
* Users can leave neighborhood and change
* Users can only view the details of one hood



### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Load home page | Default link | home page is displayed if user is authenticated else user is prompted to login |
| Join neighbourhood  | click on Join Hood in any of the hood  | The hood page is loaded with details of businesses and contact information on the hood |
| Display only one hood | On home page click on view current hood if user has joined a hood | The hood page is loaded with details of businesses and contact information|
| Add business | Click on add business or business icon on hood page | Form to upload a business|
| Add Update posts | Click on Street Smarts | Form to upload a post|
| View Profile | Click on profile | Profile page displays the hood and details of user if they join a hood otherwise a text prompts them to join a hood|
| Edit profile | Click on edit profile | Form where users can edit profiles|
| Exit the application | Click on logout | Login prompt |


## Technologies Used
* Python
* HTML
* Bootstrap
* Django

## Application link
https:

## Prerequisites
* Python 3.6 required
* Postgresql

## Setup/Installation Requirements
Follow the following commands to run the project
* git clone/download ```https://github.com/tumaa/Hood.git```
* cd Hood
* Install required files in requirements.txt
* Run ```python3.6 manage.py runserver```



## Known Bugs
None known at the moment.

## Support and contact details
In case of clarification email me at ramanfatuu@gmail.com

### License
Copyright (c) 2019 **Tumaa**

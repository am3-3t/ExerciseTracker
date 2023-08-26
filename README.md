# ExerciseTracker
A python script to track your exercise where you input what exercise you did and script will understand the natural language using an API.

An API is used to get data related to exercise with Natural Language processing from Nutrionix. (Accessible at: https://www.nutritionix.com/)
Another API is used to push the data we got from Nutritionix to a Google Sheet. This API is used from a site called Sheety. (Accessible at: https://sheety.co)\

What does this script do?
This code takes in input in a natural language format: For example: 'I took a run of 5 km'
The input is then parsed using API from Nutritionix which segregates the language and determine what was the exercise.
In our case Exercise is Running and 5 Kilometers is then converted to estimated duration. Likewise according to duration calorie burn is also mentioned. 
These data from nutrionix is then updated in a Google sheet using Sheety API. 

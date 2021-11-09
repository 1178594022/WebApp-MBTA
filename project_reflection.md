# Project Refelction
**Project Overview** 

The project focus on the purpose of developing a website app that allow the app user to input a address or a city name to find the closest MBTA station and its station wheel chair accessability. 

The project consist of two parts, which is the underlying logistics, and the web app development. For the underlying logistics development, it is in the file mbta_finder.py. The first function in this file generate a latitude and longtitude position of the entered location from the desinated api. The second fuction get_nearest_station takes two arguement which are latitude and longitude and returnd the name of the station and the accessability from the desinated api. The last function find_stop_near puts the previous two functions together. It will takes one arguement which is the location name and returns the name of the mbta station name and the accessability. If the input of the user can not be found, the function will return None.

In the file app.py, we route a website to the defult address http://127.0.0.1:5000/. The website will post a input request for the user to enter the address and return the closest station name and accessability. If there is a erro with the input, the webpage will ask the user to try again.

**Project Reflection**

From the process point of view, the group collaboration went well. The two members of the group are able to sit down and contribute to the code evenly during the coding process. Sam contribute mainly to the development to the underlying logistics and Mengyu contribute to the web app design. This project is appropriately scoped which we are able to figure out most of the structure and logistics by our selves. We do have a good plan for the unit testing and figure out most of the problems. We did most of the self-studying on learning about how to use the api and how to construct the flask and web structure. We wish that we can have more session learning about html before the task assignment. Mengyu learnt html before and helped the project a lot. It would be very helpful for all of the team member to have some understanding about html and construct our own templet from scratch. 

In terms of working in a team, we majorly work together. Having a peer together to brain storm together about the structure is very helpful. Also, we have one member of the team to take the lead of the part that he or her feel the most confident about. There are not many problem happened during the process of the team work. To work better next time, we could possibly try to divide the work and use the forked repository to contribute to the work to see if that will make the completion of the job more efficiently.


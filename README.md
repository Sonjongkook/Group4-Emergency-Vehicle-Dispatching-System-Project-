# Group4-Emergency-Vehicle-Dispatching-System-Project-

Emergency Vehicle Dispatching System
IMPLEMENTED USING PYTHON

Anna Johnson | Kyle Son | Computer Science 404 Project 1 

Assumptions
1.	Requests are processed by order of their ID. Once a vehicle is assigned to a request, it becomes unavailable for use in later requests.
2.	When building the graph, edges are assumed to be undirected.
3.	The number of vehicles available is greater than the number of vehicles requested. 
4.	If the distance is the same for multiple vehicles, we make the selection based on ID number in ascending order (if there are two vehicles equidistance from a request zip code, we would send vehicle with ID 1 over vehicle with ID 2).

Project Workflow
1.	Make json data according to Project guidelines
2.	Process the information from the Json file
3.	Find shortest path from request zip code to zip code with available vehicle of the correct type using Dijkstra’s Shortest Path Algorithm 
4.	Dispatch most suitable vehicle to the request and set it to unavailable




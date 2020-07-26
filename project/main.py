import json
from graph import Graph
from vertex import Vertex
from dijkstra import dijkstra
from Json_generator import json_data
import pandas as pd

if __name__ == '__main__':
    opened_data = json.load(open('data.json', 'r'))
    # opened_data = json.load(open('data2.json', 'r')) (another json data)
    # opened_data = json_data
    vehicles = opened_data['vehicles']  # getting vehicle
    requests = opened_data['requests']
    distances = opened_data['distances']

    for vehicle in vehicles:
        vehicle['avaliable'] = True  # add a boolean variable to vehicle

    graph = Graph()  # make an graph object

    for distance in distances:
        if distance['zipcode1'] not in graph.vert_dict.keys():
            # make a node for each zipcode and add it to the graph
            graph.add_vertax(distance['zipcode1'])
        if distance['zipcode2'] not in graph.vert_dict.keys():
            graph.add_vertax(distance['zipcode2'])
        graph.add_edge(distance['zipcode1'],
                       distance['zipcode2'], distance['distance'])

    for requset in requests:  # Implement an algorithm that processes requests one by one
        avaliable_vehicles = []
        for vehicle in vehicles:
            # we need to initialize the status to implement dijkstra
            if vehicle['type'] == requset['vehicle_type'] and vehicle['avaliable']:
                avaliable_vehicles.append(vehicle)

        if avaliable_vehicles:
            graph.reset_verticles()  # we need to initialize the status to implement dijkstra
            # using a dijkstra method
            # assign start point as requste node
            dijkstra(graph, graph.get_vertax(requset['zipcode']))

        for aval in avaliable_vehicles:
            aval['distance'] = graph.get_vertax(
                aval['zipcode']).get_distance()  # get a distance from a dijkstra and record it in aval

        # sort based on distance so we can find minimum one as an best one
        avaliable_vehicles = sorted(
            avaliable_vehicles, key=lambda x: x['distance'])

        if avaliable_vehicles:
            print("Using Dijkstra algorithm")
            for aval in avaliable_vehicles:
                print("id {} vehicle is ready at zipcode {} and distance is {}".format(aval['id'],
                                                                                       aval['zipcode'], aval['distance']))
            vehicles[vehicles.index(avaliable_vehicles[0])
                     ]['avaliable'] = False  # since avaliable vehicle is sorted based on distance 0 index element is most closest one.
            # and make this vehicle unavaliable
            requset['vehicle_id'] = avaliable_vehicles[0]['id'] # fill in vehicle_id and distance for each request.
            requset['distance'] = avaliable_vehicles[0]['distance']
            print("the best solution for request id:{} zipcode:{} is id:{} zipcode:{} distance with {} ".format(
                requset["id"], requset["zipcode"], avaliable_vehicles[0]['id'], avaliable_vehicles[0]['zipcode'], avaliable_vehicles[0]['distance']))
            print("requset id {} is processed".format(requset["id"]))
            print('-----------')

        else:
            print("There is no way to dispatch your request")

    print('-----------')
    print("all request has been processed")
    print()
    print("[completed request table]")
    completed_requests = pd.DataFrame(requests)
    completed_requests = completed_requests.set_index("id")
    print(completed_requests)

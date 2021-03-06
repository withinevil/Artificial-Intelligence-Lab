print("\nThis Uniformed Cost Search Program is made by Muhammad Talha Butt \n")

import queue as Q
from queue import PriorityQueue
def UCS():
    print("Enter the 13 Inputs to Guide Graph of Karachi Map")
    def search(graph, start, end):
        if start not in graph:
            raise TypeError(str(start) + ' not found in graph !')
            return
        if end not in graph:
            raise TypeError(str(end) + ' not found in graph !')
            return

        queue = Q.PriorityQueue()
        queue.put((0, [start]))

        while not queue.empty():
            node = queue.get()
            current = node[1][len(node[1]) - 1]

            if end in node[1]:
                print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]) + " Kilometers")
                break

            cost = node[0]
            for neighbor in graph[current]:
                temp = node[1][:]
                temp.append(neighbor)
                queue.put((cost + graph[current][neighbor], temp))

    def readGraphdata():
        lines = int(input())
        graph = {}

        for line in range(lines):
            line = input()

            tokens = line.split()
            node = tokens[0]
            graph[node] = {}

            for i in range(1, len(tokens) - 1, 2):
                # print(node, tokens[i], tokens[i + 1])
                # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
                graph[node][tokens[i]] = int(tokens[i + 1])
        return graph

    def main():
        graph = readGraphdata()
        search(graph, 'IUGC', 'IUMainCampus')




    if __name__ == "__main__":
        main()

def Astar():

    from queue import PriorityQueue

    Karachi_Map = {
        "IUGC": {"SirSyedStop": 6, "PatelHospital": 3, "Waterpump": 5},

        "SirSyedStop": {"ExpoCentre": 3, "UrduUniversity": 1, "RashidMinhasRoad": 3},

        "PatelHospital": {"AllamaShabbirRoad": 2},

        "Waterpump": {"TeenHatti": 7},

        "ExpoCentre": {"NationalStadium": 4},

        "UrduUniversity": {"JailChawrangi": 6},

        "AllamaShabbirRoad": {"RashidMinhasRoad": 7},

        "TeenHatti": {"JailChawrangi": 9},

        "NationalStadium": {"ShahrahFaisal": 6},

        "JailChawrangi": {"IUMainCampus": 12},

        "RashidMinhasRoad": {"ShahrahFaisal": 8},

        "ShahrahFaisal": {"IUMainCampus": 15}

    }

    # This function does the A* search.
    def a_star(start_city, end_city):
        # Heuristc values as straight line distances.
        heuristics = {
            'IUGC': 399,
            'ExpoCentre': 190,
            'SirSyedStop': 57,
            'PatelHospital': 272,
            'UrduUniversity': 156,
            'JailChawrangi': 101,
            'AllamaShabbirRoad': 200,
            'NationalStadium': 45,
            'RashidMinhasRoad': 89,
            'ShahrahFaisal': 25,
            'Waterpump': 244,
            'Teenhatti': 350,
            'IUMainCampus': 0,

        }

        # Create instances of PriorityQueue
        frontier, marked = PriorityQueue(), {}

        # Store the straight line distance values inside the priority queue
        frontier.put((heuristics[start_city], 0, start_city, [start_city]))

        # Set marked city's straight line distances
        marked[start_city] = heuristics[start_city]
        while not frontier.empty():

            # Get the heuristic , initial cost , straight line distance , path cost values from priority queue.
            (h, cost, v, path) = frontier.get()

            # If reached return cost.
            if v == end_city:
                return h, cost, path

            # Expand a city's neighbors
            for neighbor in Karachi_Map[v].keys():

                # Calculate cost of current city so far.
                cost_from_start = cost + Karachi_Map[v][neighbor]

                # updates the h value
                h = cost_from_start + heuristics[neighbor]

                # include unmarked neighbors.
                if not neighbor in marked or marked[neighbor] >= h:
                    marked[neighbor] = h

                    # Store the new neighbor values in the queue.
                    frontier.put((h, cost_from_start, neighbor, path + [neighbor]))

    def main():
        print("\nNote: Starting and Destination Stop ('Letters, Numbers or Special Characters) should typed as Given' ")

        print('\nEnter the Starting Stop e.g: Start(IUGC), Destination(IUMainCampus)')

        start_city = input("Start from?  \n")
        print('Enter the Destination Stop e.g: IUMainCampus')

        end_city = input("Destination?  \n")

        # If the city does not exist return error.
        if start_city not in Karachi_Map or end_city not in Karachi_Map:
            h, cost, short_path = a_star(start_city, end_city)
            # Prints the path cost.
            print("A* Search For Path(Iqra University Gulshan Campus to Main Campus)")
            # Prints the path cost.
            print('Path Cost = ', cost)

            # Prints the shortest path from Lugoj to Bucharest
            print(' -> '.join(city for city in short_path))
        else:

            print("Stop is not Available")

    if __name__ == '__main__':
        main()


for i in range(1):
    print("\nSearch Engine (A Trip from IUGC to IUMainCampus)\n")
    choice = int(input("Enter 1 For Uniformed Cost Search of IUGC to Main Campus\nEnter 2 For A* Search of IUGC to Main Campus\n"))

    if choice == 1:
        print(UCS())
        break

    elif choice == 2:
        print(Astar())
        break


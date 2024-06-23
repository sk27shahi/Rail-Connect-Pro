import random 
class RailConnectPro: 
    def __init__(self): 
# Assume we have a list of train routes with their details 
        self.train_routes = { 
"Ongole to Hyderabad": {"train_ids": ["TRN123", "TRN456", "TRN789"],  "min_cost": 500, "max_cost": 1100, "distance": 300, "arrival_time": "10:00 AM",  "reaching_time": "06:00 PM"}, 
"Hyderabad to Mumbai": {"train_ids": ["TRN987", "TRN654", "TRN321"],  "min_cost": 650, "max_cost": 1300, "distance": 800, "arrival_time": "04:00 PM",  "reaching_time": "09:00 AM"}, 
"Mumbai to Bangalore": {"train_ids": ["TRN246", "TRN579", "TRN135"],  "min_cost": 700, "max_cost": 1700, "distance": 1000, "arrival_time": "12:00 PM",  "reaching_time": "05:00 AM"}, 
"Bangalore to Chennai": {"train_ids": ["TRN864", "TRN357", "TRN951"],  "min_cost": 900, "max_cost": 1150, "distance": 350, "arrival_time": "02:00 PM",  "reaching_time": "09:00 AM"}, 
# Add more routes as needed 
} 
    def get_available_trains(self, source, destination): 
        available_trains = [] 
        route_name = f"{source} to {destination}" 
        if route_name in self.train_routes: 
            available_trains.extend(self.train_routes[route_name]["train_ids"]) 
        return available_trains 
    def get_ticket_and_price(self, train_id): 
        for route, details in self.train_routes.items(): 
            if train_id in details["train_ids"]: 
            # Generate a random price within the specified range 
                ticket_price = random.randint(details["min_cost"], details["max_cost"]) 
            return ticket_price 
        return None 
    def get_distance(self, source, destination): 
        route_name = f"{source} to {destination}" 
        if route_name in self.train_routes: 
            return self.train_routes[route_name]["distance"] 
        return None
    def get_arrival_time(self, source, destination): 
        route_name = f"{source} to {destination}" 
        if route_name in self.train_routes: 
            return self.train_routes[route_name]["arrival_time"] 
        return None 
    def get_reaching_time(self, source, destination): 
        route_name = f"{source} to {destination}" 
        if route_name in self.train_routes: 
            return self.train_routes[route_name]["reaching_time"] 
        return None 
# Example usage 
def main(): 
    rail_connect = RailConnectPro() 
    source = input("Enter the source city: ").strip().title() 
    destination = input("Enter the destination city: ").strip().title() 
    available_trains = rail_connect.get_available_trains(source, destination) 
    print(f"Number of trains available from {source} to {destination}:  {len(available_trains)}") 
    print(f"Distance between {source} and {destination}:{rail_connect.get_distance(source, destination)} km") 
    print(f"Arrival time at {destination}: {rail_connect.get_arrival_time(source,  destination)}") 
    print(f"Reaching time at {source}: {rail_connect.get_reaching_time(source,  destination)}") 
    print("Train IDs and Ticket Prices:") 
    for train_id in available_trains: 
        ticket_price = rail_connect.get_ticket_and_price(train_id) 
        print(f"Train ID: {train_id}, Ticket Price: ₹{ticket_price}") 
if __name__ == "__main__": 
    main()
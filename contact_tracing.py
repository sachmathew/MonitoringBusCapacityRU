import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor() 

def contact_tracing(student_id):
	for bus_id in get_student(student_id)['buslist'].split(','):
		for student in get_passengers(bus_id)['netid']:
			notify(student)

def get_student(netid):
	return cur.execute('select * from students where netid=:i', {'i': netid}).fetchone()

def get_passengers(id):
	return cur.execute('select * from students where buslist like i', {'i': id}).fetchall()

def get_bus(id):
	return cur.execute('select * from busses where id=:i', {'i': id}).fetchone()

def get_route(id):
	return cur.execute('select * from routes where id=:i', {'i': id}).fetchone()

def get_stop_ids_on_route(id):
	return get_route(id)['stops'].split(',')

def get_stop(id):
	return cur.execute('select * from stops where netid=:i', {'i': id}).fetchone()

def update_busses():

def input_vehicles(self, capacity):
	def __init__(self):
    response = requests.request("GET", "https://transloc-api-1-2.p.rapidapi.com/vehicles.json", headers={'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",'x-rapidapi-key': "bd2742fe0bmshb1a756f4de0628fp1c01a2jsn774567dec941"}, params={"agencies": "1323", "callback": "call"})
    resp_vehicles = json.loads(response.text.encode('utf8'))
    ID_idx = 1

    for ct in range(0, len(resp_vehicles['data']['1323'])):\
        curr_routeID = resp_vehicles['data']['1323'][ct]['route_id']
        ag_route_name_fetch = cur.execute("SELECT routeNAME FROM TEST_ROUTES WHERE routeID = ?",
                                        (curr_routeID,)).fetchone()
        ag_route_str = ag_route_name_fetch[0]

        stop_list = []
        arrive_list = []
        stop_name = []
        lat_long = []

        for idx1 in range(len(resp_vehicles['data']['1323'][ct]['arrival_estimates'])):
            stop_list.append(resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['stop_id'])
            arrive_list.append(resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['arrival_at'])
            stop_string = ' '.join(stop_list)
            arrive_string = ' '.join(arrive_list)

            curr_stop_id = resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['stop_id']
            curr_stop_name_tup = cur.execute("SELECT stopNAME FROM STOPS WHERE stopID = ?",
                                           (curr_stop_id,)).fetchone()
            curr_stop_name = curr_stop_name_tup[0]
            stop_name.append(curr_stop_name)
            stop_name_str = ', '.join(stop_name)

            lat = resp_vehicles['data']['1323'][ct]['location']['lat']
            long = resp_vehicles['data']['1323'][ct]['location']['lng']

            lat = str(lat)
            lon = str(lon)
            lat_long = lat + ',' + lon

        if len(resp_vehicles['data']['1323'][ct]['arrival_estimates']) >= 1:
            cur.execute(
                "INSERT OR REPLACE INTO TEST_TABLE VALUES (:ID, :vehicleID, :capacity, :routeNAME, :routeID, :stopName, :nextSTOP, :arrivals, :lat_long)",
                {'ID': ID_idx,
                 'vehicleID': resp_vehicles['data']['1323'][ct]['call_name'],
                 'capacity': capacity,
                 'routeNAME': ag_route_str,
                 'routeID': resp_vehicles['data']['1323'][ct]['route_id'],
                 'stopName': stop_name_str,
                 'nextSTOP': stop_string,
                 'arrivals': arrive_string,
                 'lat_long': lat_long})
        else:
            cur.execute(
                "INSERT OR REPLACE INTO TEST_TABLE VALUES (:ID, :vehicleID, :capacity, :routeNAME, :routeID, :stopName, :nextSTOP, :arrivals, :lat_long)",
                {'ID': ID_idx,
                 'vehicleID': resp_vehicles['data']['1323'][ct]['call_name'],
                 'capacity': capacity,
                 'routeNAME': ag_route_str,
                 'routeID': resp_vehicles['data']['1323'][ct]['route_id'],
                 'stopName': 'n/a',
                 'nextSTOP': 'n/a',
                 'arrivals': 'n/a',
                 'lat_long': 'n/a'})

        ID_idx = ID_idx + 1
        con.commit()  
	
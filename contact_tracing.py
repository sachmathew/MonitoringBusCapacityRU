import sqlite3
import time

con = sqlite3.connect('example.db')
cur = con.cursor() 

def contact_tracing(netid):
	#add items to see if students are on bus at the same time
	contact_list = []
	for bus in get_buslist(netid):
		bus1 = bus1.split('|')
		for student in get_passengers(bus1[0])['netid']:
			bus2 = []
			for bus_n in get_buslist(student)
				if bus_n.split('|')[0] == bus_id:
					bus2 = bus_n.split('|')
			if check_overlap(time.strptime(bus1[1]), time.strptime(bus1[2]), time.strptime(bus2[1]), time.strptime(bus2[2])):
				contact_list.append(student)
				notify(student)

def get_buslist(netid):
	get_student(netid)['buslist'].split(',')

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

def got_on_bus(vehicle_id, netid, time):
	#map student to id, date and time
	buslist = get_buslist(netid)
	buslist = buslist.append(vehicle_id + '|' + time + '|' +'')
	b = ",".join(buslist)
	cur.execute('update students set buslist=:b', {'b': b})

def undo_get_on_bus(vehicle_id, netid):
	buslist = get_buslist(netid)
	val = buslist[-1].split('|')
	if val[0] == vehicle_id:
		del buslist[-1]
		b = ",".join(buslist)
		cur.execute('update students set buslist=:b', {'b': b})

def got_off_bus(vehicle_id, netid, time):
	#map get off bus time
	buslist = get_buslist(netid)
	val = buslist[-1].split('|')
	if val[0] == vehicle_id:
		buslist[-1] = val[0]+'|'+val[1]+'|'+time
		b = ",".join(buslist)
		cur.execute('update students set buslist=:b', {'b': b})

def check_overlap(enter1, exit1, enter2, exit2):
	return ((enter1 <= exit2) && (exit1 >= exit2)) || ((enter2 <= exit1) && (exit2 >= exit1))
from classes import Route

conn = ['201', '203']

route_test = Route('202', conn)

route_test.show_test()

print(route_test.connections[0])
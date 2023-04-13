import OpenOPC

opc = OpenOPC.client()
server_name = 'Matrikon.OPC.Simulation.1'
host_name = 'localhost'
username = 'myusername'
password = 'mypassword'

# Connect to OPC server
opc = OpenOPC.client()
#opc = OpenOPC.open_client('localhost')
print(opc.servers())
opc.connect(server_name)
#opc.connect(server_name, host_name, username, password)
print(opc.list('Configured Aliases.*'))
print(opc.properties('.Apertura'))
opc.close()

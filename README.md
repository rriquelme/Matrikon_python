# Matrikon_python
## Steps to work with matrikon OPC Server for Simulation and Python on windows

1. Download and install matrikon OPC Server for Simulation from the official web page
2. Download and install http://www.gray-box.net/download_daawrapper.php info obtained at https://www.youtube.com/watch?v=lbubVMlPP6Y , then use regsvr32 gbda_aut.dll on windows cmd
3. install OPC ua, using pip install OpenOPC-Python3x

## Quick Explanation:

1. Initialize opc:
    opc = OpenOPC.client()

2. List all servers:
    print(opc.servers())

3. Connect to the server, in my case the Matrikon OPC Server: 
    opc.connect('Matrikon.OPC.Simulation.1')

4. view information of the opc:
    print(opc.info())
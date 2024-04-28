from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(baudrate=9600, port="/dev/ttyUSB0", method="rtu")
if client.connect():
    res = client.read_holding_registers(address=0, count=2, unit=1)
    temperature = res.registers[0]/10
    print(f"Temperature:\t{temperature} ˚C")
    humidity  = res.registers[1]/10
    print(f"Humidity:\t{humidity} %")
    client.close()
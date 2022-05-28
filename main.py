import netmiko
from netmiko import ConnectHandler
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.88.151',
    'username': 'root',
    'password': '1234',
    'secret': '123'    
}
net_connect =ConnectHandler(**iosv_l2)
#cCommand = input("Wht is the command")
#output =net_connect.send_command('{}'.format(cCommand))
#print(output)
net_connect.enable()
config_commands = [ 'int loop 0', 'ip addre 2.2.2.2 255.255.255.0', 'no sh','do wr']
output = net_connect.send_config_set(config_commands)
show_command = ['show conf']
output2 =net_connect.send_command('show conf')
print(output2)

from statistics import quantiles
from tkinter.font import names

for t in range(5):
    print (t)

names = ["Tim", "John", "James"]
for name in names:
    print (name)
#
dc_inventory = {"switches":5, "routers":10, "firewalls":9}
for device in dc_inventory:
    print (device)
#
#
for device, quantity in dc_inventory.items():
    print("You have {} {} in the SW data center.".format(quantity, device))
#
from time import sleep
while True:
     try:
         print("Polling.")
         # Poll some resource
         sleep(1)
     except KeyboardInterrupt:
         break
        

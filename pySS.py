from PySS_Support.Grabbing.Classes import get_all_server
from PySS_Support.Classes import SSServer
from PySS_Support.Validating.Classes import ValidateTest
from multiprocessing import Process

debug = True

if debug:
    all_server_collection = get_all_server(True)
else:
    all_server_collection = get_all_server()

count=1
for ser in all_server_collection:
    if isinstance(ser, SSServer):
        print("Testing server %s :%s......" % (count, ser.ip))
        result = ValidateTest(ser).test()
        ser.delay = result
        if result:
            print("Pass!")
        count+=1


min_delay = False
min_delay_server = False

# get the smallest delay server
for ser in all_server_collection:

    if ser.delay:

        delay = int(ser.delay)

        if not min_delay:
            min_delay = delay
            min_delay_server = ser
        elif delay < min_delay:
            min_delay = delay
            min_delay_server = ser
print(min_delay_server)

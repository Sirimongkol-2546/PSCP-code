"""BusStop I"""
def main():
    """inp"""
    amount = int(input())
    count = int(input())
    passenger1 = []
    passenger_of_list_integer = []
    at_home = 0
    for _ in range(count):
        bus = input().split()
        passenger1.append(bus)
    passenger1.sort(key=lambda i: int(i[0]))
    for i in passenger1:
        stage_bus_stop = int(i[0])
        if len(passenger_of_list_integer) != 0:
            passenger_of_list_integer2 = passenger_of_list_integer.copy()
            for arrive in passenger_of_list_integer:
                if arrive == stage_bus_stop:
                    passenger_of_list_integer2.remove(arrive)
                    at_home += 1
            passenger_of_list_integer = passenger_of_list_integer2
        for j in range(1, len(i)):
            if len(passenger_of_list_integer) == amount:
                break
            if stage_bus_stop < int(i[j]):
                passenger_of_list_integer.append(int(i[j]))
    print(at_home)
main()

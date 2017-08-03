import csv

def find_nth_longest_flight(n):
    with open('more_route_info.csv') as f:
        route_info = csv.reader(f)
        h = next(route_info)

        i = 0
        for row in route_info:
            l = list(row)
            if row[6] == n:
                print(l)
                return row
            else:
                if i<5:
                    print(row[6])
                    i += 1


x = find_nth_longest_flight(12750)
type(x)
# for item in x:
#     print(x)
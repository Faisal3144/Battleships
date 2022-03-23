cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]
def total(b):
    sum=0
    for row in range(len(b)):
        sum += b[row][2] 
        return sum
print(total(cities))                  
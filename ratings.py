"""Restaurant rating lister."""
def print_restaurant_ratings(filename):

    file_name = open(filename)
    restaurant_ratings = {}
    for line in file_name:
       line_strip = line.rstrip()
       items = line_strip.split(':')

       restaurant_ratings[items[0]] = items[1]
       
       new_restaurant_ratings = sorted(restaurant_ratings.items())

    for k, v in new_restaurant_ratings:
        print(f"{k} is rated at {v}.")
    return

print_restaurant_ratings('scores.txt')
# put your code here

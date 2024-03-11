import textfile
file = open('textfile.txt', 'w')

car_brands = ['Tesla', 'BMW', 'Ferrari', 'Lamborghini', 'Audi', 'Mercedes-Benz']
car_brands_pris =['1 million', '600 thousand', '2 million', '400 thousand', '400-500 thousand']

for i in range(0, 5):
    entry = car_brands[i] + "- " + str(car_brands_pris[i])+'\n'
    file.write(entry)

file.close()

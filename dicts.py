

sample_dict = dict()
first_key = ('300', '1')
second_key = ('300', '2')
sample_dict[first_key] = (1, {'7', '9', '11'})
sample_dict[second_key] = (2, {'7', '9'})

print(sample_dict[first_key])
print(sample_dict[second_key])

set1 = {'1', '2', '3'}
set2 = {'3', '2', '1', '4'}

print("Sets are equal: {0}".format(set1 == set2))
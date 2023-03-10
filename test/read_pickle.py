import pickle

mesh_size_list = [1, 2, 3]
dt = 0.1

# read the data from the pickle file
for mesh_size in mesh_size_list:
    file_name = f'mesh_size_{mesh_size}_dt_{dt}.pickle'
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
    print(data)



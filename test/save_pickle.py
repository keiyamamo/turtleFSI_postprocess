import pickle
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('-nx', type=int, help='number of elements in x direction')

args = parser.parse_args()

Nx = args.nx

save_data = {}

dt = 0.1
v_deg = 2
p_deg = 1
error_v = 1e-2

save_data['mesh_size'] = Nx
save_data['time_step_size'] = dt
save_data['velocity_degree'] = v_deg
save_data['pressure_degree'] = p_deg
save_data['error_v'] = error_v

file_name = f'mesh_size_{Nx}_dt_{dt}.pickle'
with open(file_name, 'wb') as f:
    pickle.dump(save_data, f)
    


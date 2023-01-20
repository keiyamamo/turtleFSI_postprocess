import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_data = "case9_undamped_SVKmodel_velocity_sac_center.csv"
data = pd.read_csv(input_data,sep=',')
velocity_magnitude = data['avg(velocity_save_deg_1 (Magnitude))'] 
time = data['Time']

# extract only the second cardiac cycle
time = time.iloc[2801:5600]
velocity_magnitude = velocity_magnitude.iloc[2801:5600]
fig, ax = plt.subplots()
ax.plot(time, velocity_magnitude, color="white", linewidth=3, alpha=1, label = 'velocity')
ax.tick_params(colors="white", axis="both", which='both', labelsize=22)

[ax.spines[i].set_color("white") for i in ax.spines]

plt.savefig("velocity_undamped_SVK.png", transparent=True, bbox_inches='tight')
# plt.show()

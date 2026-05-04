import subprocess
import pandas as pd
import os

df_E3=pd.DataFrame()
df_tripinfo=pd.DataFrame()
df_edgedata=pd.DataFrame()
processes=[]
sim_folder = "aaa_simulation_file_folder_fixed"
sim_dir_abs = os.path.abspath(sim_folder)
combos = [
    {"num": 1, "cd": 5, "coeff": [0.0]},
    {"num": 2, "cd": 30, "coeff": [0.0]},
    {"num": 3, "cd": 60, "coeff": [0.0]},
    {"num": 4, "cd": 90, "coeff": [0.0]},
    {"num": 5, "cd": 120, "coeff": [0.0]},
    {"num": 6, "cd": 5, "coeff": [0.25]},
    {"num": 7, "cd": 30, "coeff": [0.25]},
    {"num": 8, "cd": 60, "coeff": [0.25]},
    {"num": 9, "cd": 90, "coeff": [0.25]},
    {"num": 10, "cd": 120, "coeff": [0.25]},
    {"num": 11, "cd": 5, "coeff": [0.5,0.75]},
    {"num": 12, "cd": 30, "coeff": [0.5,0.75]},
    {"num": 13, "cd": 60, "coeff": [0.5,0.75]},
    {"num": 14, "cd": 90, "coeff": [0.5,0.75]},
    {"num": 15, "cd": 120, "coeff": [0.5,0.75]},
]

for c in combos:
    # Build the base command
    cmd = [
        "python3", "main_1.py", 
        "--number", str(c["num"]), 
        "--cooldown", str(c["cd"]), 
        "--red_coeff"
    ]
    
    # Add all coefficients from the list to the command
    for val in c["coeff"]:
        cmd.append(str(val))

    # Launch process
    p = subprocess.Popen(cmd, cwd=sim_dir_abs)
    processes.append(p)

for p in processes:
    p.wait()

print("All processes have finished. For fixed schedule cases.")

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    df = pd.read_csv(f"aaa_simulation_file_folder_fixed/E3_output_{i}.csv")
    df_E3 = pd.concat([df_E3, df], ignore_index=True)
    df_E3.to_csv("DODE_E3_output_fixed.csv")
    df = pd.read_csv(f"aaa_simulation_file_folder_fixed/tripinfo_{i}.csv")
    df_tripinfo = pd.concat([df_tripinfo, df], ignore_index=True)
    df_tripinfo.to_csv("tripinfo_fixed.csv")
    df = pd.read_csv(f"aaa_simulation_file_folder_fixed/edgedata_{i}.csv")
    df_edgedata = pd.concat([df_edgedata, df], ignore_index=True)
    df_edgedata.to_csv("edgedata_fixed.csv")

## Actuated cases
df_E3=pd.DataFrame()
df_tripinfo=pd.DataFrame()
df_edgedata=pd.DataFrame()
processes=[]
sim_folder = "aaa_simulation_file_folder_actuated"
sim_dir_abs = os.path.abspath(sim_folder)

combos = [
    {"num": 1, "cd": 5, "coeff": [0.0]},
    {"num": 2, "cd": 30, "coeff": [0.0]},
    {"num": 3, "cd": 60, "coeff": [0.0]},
    {"num": 4, "cd": 90, "coeff": [0.0]},
    {"num": 5, "cd": 120, "coeff": [0.0]},
    {"num": 6, "cd": 5, "coeff": [0.25]},
    {"num": 7, "cd": 30, "coeff": [0.25]},
    {"num": 8, "cd": 60, "coeff": [0.25]},
    {"num": 9, "cd": 90, "coeff": [0.25]},
    {"num": 10, "cd": 120, "coeff": [0.25]},
    {"num": 11, "cd": 5, "coeff": [0.5,0.75]},
    {"num": 12, "cd": 30, "coeff": [0.5,0.75]},
    {"num": 13, "cd": 60, "coeff": [0.5,0.75]},
    {"num": 14, "cd": 90, "coeff": [0.5,0.75]},
    {"num": 15, "cd": 120, "coeff": [0.5,0.75]},
]

for c in combos:
    # Build the base command
    cmd = [
        "python3", "main_1.py", 
        "--number", str(c["num"]), 
        "--cooldown", str(c["cd"]), 
        "--red_coeff"
    ]
    
    # Add all coefficients from the list to the command
    for val in c["coeff"]:
        cmd.append(str(val))

    # Launch process
    p = subprocess.Popen(cmd, cwd=sim_dir_abs)
    processes.append(p)

for p in processes:
    p.wait()

print("All processes have finished. For actuated schedule cases.")

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    df = pd.read_csv(f"aaa_simulation_file_folder_actuated/E3_output_{i}.csv")
    df_E3 = pd.concat([df_E3, df], ignore_index=True)
    df_E3.to_csv("DODE_E3_output_actuated.csv")
    df = pd.read_csv(f"aaa_simulation_file_folder_actuated/tripinfo_{i}.csv")
    df_tripinfo = pd.concat([df_tripinfo, df], ignore_index=True)
    df_tripinfo.to_csv("tripinfo_actuated.csv")
    df = pd.read_csv(f"aaa_simulation_file_folder_actuated/edgedata_{i}.csv")
    df_edgedata = pd.concat([df_edgedata, df], ignore_index=True)
    df_edgedata.to_csv("edgedata_actuated.csv")
import argparse
import shutil
import os 
 
def create_paths_to_disks(disks):
    return [disk.upper() + ":\\copySrc" for disk in disks]

# Initialize parser
parser = argparse.ArgumentParser(description="Python script to copy over data from multiple disks to current working dir")
# Adding optional argument
parser.add_argument("-d", "--disks", help = "String that contains all disk letters of disks to copy data from -- required")
parser.add_argument("-n", "--name", default="data", help = "Name for output directory in current working directory -- default: data")

args = parser.parse_args()
paths = create_paths_to_disks(args.disks)
curr_dir = os.getcwd()
print(paths)
for i in range(len(paths)):
    path = paths[i]
    #dest_dir = curr_dir + f"\\{args.name}\\" + path[0] + "_disk\\"
    dest_dir = curr_dir + f"\\{args.name}\\"
    print(f"Writing from: {path}")
    print(f"Writing to: {dest_dir}")
    shutil.copytree(path, dest_dir, dirs_exist_ok=True)

#Do other stuff here, like process data for nerfstudio - start render etc
#os.system('ls -l')

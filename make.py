# Assembles ready-to-import directory for C:S
from shutil import copyfile
import os
import pathlib

dirname = os.path.dirname(__file__)

name = "Realistic Highway"

sizes = ["2L"]
elevations = [""," Elevated"] # Bridge, Tunnel
mtypes = ["", "_node"]
details = ["", "_lod"]
textures = ["_a", "_d", "_p", "_r"]

dist_dir = "dist/"

#filename1 = os.path.join(dirname, 'Mesh/2L/Realistic Highway 2L.obj')
#filename2 = os.path.join(dirname, 'dist/2L/Realistic Highway 2L.obj')
#copyfile(filename1, filename2)

# List mesh files
for size in sizes:
  output_dir = dist_dir + size + "/"
  pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

  for elevation in elevations:
    for mtype in mtypes:
      for detail in details:
        input_file = "Mesh/" + size + "/" + name + " " + size + elevation + mtype + ".obj"
        output_file =  output_dir + name + " " + size + elevation + mtype + detail + ".obj"

        try: 
          copyfile(input_file, output_file)
          print("Done: %-50s  ->  %10s" % (input_file, output_file))
        except FileNotFoundError:
          print("Warning: Input file %s not found!" % input_file)

# List textures
for size in sizes:
  for elevation in elevations:
    for mtype in mtypes:
      for detail in details:
        for texture in textures:
          if mtype == "_node" and texture == "_a":
            # No alpha texture for nodes
            continue

          input_file = "Textures/" + name + mtype + detail + texture + ".png"
          output_file = output_dir + name + " " + size + elevation + mtype + detail + texture + ".png"
          
          try: 
            copyfile(input_file, output_file)
            print("Done: %-50s  ->  %10s" % (input_file, output_file))
          except FileNotFoundError:
            print("Warning: Input file %s not found!" % input_file)
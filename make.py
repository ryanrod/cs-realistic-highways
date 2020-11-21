# Assembles ready-to-import directory for C:S
from shutil import copyfile

name = "Realistic Highway"

sizes = ["2L", "3L"]
elevations = [""," Elevated"," Bridge"]
mtypes = ["", "_node"]
details = ["", "_lod"]
textures = ["_a", "_d", "_p", "_r"]

output_folder = "dist/"



# List mesh files
for size in sizes:
  for elevation in elevations:
    for mtype in mtypes:
      for detail in details:
        filename = name + " " + size + elevation + mtype + detail + ".obj"
        input_file = "Mesh/" + size + "/" + filename
        output_file = output_folder + size + "/" + filename
        
        print("%-50s  ->  %10s" % (input_file, output_file))
        #print(input_file + " -> " + output_file)

# List textures
for size in sizes:
  for elevation in elevations:
    for mtype in mtypes:
      for detail in details:
        for texture in textures:
          input_file = "Textures/" + name + mtype + detail + texture + ".png"
          output_file = output_folder + size + "/" + name + " " + size + elevation + mtype + detail + texture + ".png"
          
          print("%-50s  ->  %10s" % (input_file, output_file))
          #print(input_file + " -> " + output_file)
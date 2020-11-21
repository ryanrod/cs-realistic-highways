# Assembles ready-to-import directory for C:S
# Steps:
#   For each road size:
#     For each elevation:
#       For each type (segment/node):
#         Create output folder
#         Copy mesh
#         Copy global textures, rename
name = "Realistic Highway"

sizes = ["2L"]
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
        output_file = output_folder + name + " " + size + elevation + mtype + detail + ".obj"
        print(output_file)

# List textures
for size in sizes:
  for elevation in elevations:
    for mtype in mtypes:
      for detail in details:
        for texture in textures:
          input_file = output_folder + name + " " + size + elevation + mtype + detail + texture + ".png"
          print(input_file)
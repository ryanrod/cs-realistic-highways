import bpy
import bmesh
import sys
import os

# Read arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

if len(argv) != 2:
  print(len(argv))
  print("Usage: blender --background --python <script.py> -- input_dir output_dir")
  exit(0)

def convert(input_file, output_file):

  # Load a Wavefront OBJ File
  bpy.ops.wm.read_factory_settings(use_empty=True)
  bpy.ops.import_scene.obj(filepath=input_file, filter_glob="*.obj;*.mtl", 
  use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,
  use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',
  axis_forward='-Z', axis_up='Y')

  #-------------------------------------------------
  #import bpy
  #import bmesh
  #import sys

  # Select object at index 0 (should be imported model)
  ob = bpy.data.objects[0]

  # Find faces that contain edges of length 3.74
  mesh = ob.data
  bm = bmesh.new()
  bm.from_mesh(mesh)
  uv_layer = bm.loops.layers.uv.verify()
  modified_faces = 0

  for face in bm.faces:
      #for attr in dir(face):
      #    print("face.%s = %r" % (attr, getattr(face, attr)))
      for edge in face.edges:
          if edge.calc_length() > 3.7 and edge.calc_length() < 3.8:
              #print(edge.calc_length())
              modified_faces += 1

              # Shift uv map
              for loop in face.loops:
                  #print(loop[uv_layer].uv, end='')
                  #print(' -> ', end='')
                  loop[uv_layer].uv.x += 0.255
                  #print(loop[uv_layer].uv)
              break

  print('------------------------')
  print('UV shifted %i faces' % modified_faces)
  print('------------------------')

  # Write the mesh back
  bm.to_mesh(mesh)

  #-------------------------------------------------

  # Export
  bpy.ops.export_scene.obj(filepath=output_file, use_materials=False)


dir_in = argv[0]
dir_out = argv[1]

directory = os.fsencode(dir_in)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".obj"): 
        convert(os.path.join(dir_in, filename), os.path.join(dir_out, filename))
     else:
         continue
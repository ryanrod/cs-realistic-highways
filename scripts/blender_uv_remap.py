import bpy
import bmesh
import sys

# Read arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

if len(argv) != 2:
  print(len(argv))
  print("Usage: blender --background --python <script.py> -- input_file output_file")
  exit(0)

file_in = argv[0]
file_out = argv[1]

# Load a Wavefront OBJ File
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.obj(filepath=file_in, filter_glob="*.obj;*.mtl", 
use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,
use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',
axis_forward='-Z', axis_up='Y')

#-------------------------------------------------

# Select object at index 0 (should be imported model)
ob = bpy.data.objects[0]

# Find faces that contain edges of length 4.x
mesh = ob.data
bm = bmesh.new()
bm.from_mesh(mesh)
uv_layer = bm.loops.layers.uv.verify()

for face in bm.faces:
    #for attr in dir(face):
    #    print("face.%s = %r" % (attr, getattr(face, attr)))
    for edge in face.edges:
        if edge.calc_length() > 4 and edge.calc_length() < 5:
            print(edge.calc_length())
            
            # Shift uv map
            for loop in face.loops:
                print(loop[uv_layer].uv, end='')
                print(' -> ', end='')
                loop[uv_layer].uv.x += 0.255
                print(loop[uv_layer].uv)
            break

# Write the mesh back and export
bm.to_mesh(mesh)
bpy.ops.export_scene.obj(filepath=file_out, use_materials=False)
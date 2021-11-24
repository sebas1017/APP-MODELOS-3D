import vtkplotlib as vpl
from stl.mesh import Mesh


path = "MODELO_FINAL.stl"
def render_model(path=path):
    # Read the STL using numpy-stl
    mesh = Mesh.from_file(path)

    # Plot the mesh
    vpl.mesh_plot(mesh, color="blue")

    # Show the figure
    vpl.show()

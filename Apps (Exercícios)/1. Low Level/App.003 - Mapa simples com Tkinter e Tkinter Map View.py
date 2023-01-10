import tkinter
from tkintermapview import TkinterMapView

root_tk = tkinter.Tk()
root_tk.geometry(f"{600}x{400}")
root_tk.title("map_view_simple_example.py")

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# google normal tile server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=15)

map_widget.set_address("São joão de Meriti", marker=True)

root_tk.mainloop()

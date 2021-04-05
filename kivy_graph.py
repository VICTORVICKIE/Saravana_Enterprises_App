from math import sin
from kivy_garden.graph import Graph, MeshLinePlot, BarPlot
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import itertools    
from random import randrange
from kivy.utils import get_color_from_hex as rgb

class BoxLayoutApp(App):
        
    def build(self):
        colors = itertools.cycle([
                rgb('7dac9f'), rgb('dc7062'), rgb('66a8d4'), rgb('e5b060')])
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-10, ymax=20)
        plot = BarPlot(color=next(colors), bar_spacing=.72)
        plot.bind_to_graph(graph)
        plot.points = [(1,1),(10,2)]
        print(plot.points)
        graph.add_plot(plot)
        superBox = BoxLayout()
        superBox.add_widget(graph)
        print(superBox.children[0].children[0].children)
        return superBox

root = BoxLayoutApp()

root.run()

from math import sin
from graph import Graph, MeshLinePlot, BarPlot
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import itertools    
from random import randrange
from kivy.utils import get_color_from_hex as rgb

class BoxLayoutApp(MDApp):
        
    def build(self):
        colors = itertools.cycle([
                rgb('7dac9f'), rgb('dc7062'), rgb('66a8d4'), rgb('e5b060')])
        graph = Graph(xlabel='X', ylabel='Y', padding=5, xmin=0, xmax=5, ymin=0, ymax=5)
        plot = BarPlot(bar_spacing=.1)
        plot.color = rgb('dc7062')
        plot.points = [(1,1),(2,2)]
        plot.bind_to_graph(graph)
        graph.add_plot(plot)
        graph2 = Graph(xlabel='X', ylabel='Y', padding=5, xmin=0, xmax=5, ymin=0, ymax=5)
        plot2 = BarPlot(bar_spacing=.1)
        plot2.color = rgb('dc7062')
        plot2.points = [(1,1),(2,2)]
        plot2.bind_to_graph(graph2)
        graph2.add_plot(plot2)
        superBox = MDBoxLayout()
        superBox.add_widget(graph)
        superBox.add_widget(graph2)
        return superBox

root = BoxLayoutApp()

root.run()

"""Prints the the relationships between stacks as a graph.

"""

from .base import BaseCommand
from ...actions import graph


class Graph(BaseCommand):

    name = "graph"
    description = __doc__

    def add_arguments(self, parser):
        super(Graph, self).add_arguments(parser)
        parser.add_argument("-f", "--format", action="store_true",
                            default="dot",
                            help="The format the print the graph in.")

    def run(self, options, **kwargs):
        super(Graph, self).run(options, **kwargs)
        action = graph.Action(options.context, provider=options.provider)
        action.execute(format=options.format)

import logging

from .base import BaseAction, plan


logger = logging.getLogger(__name__)


class Action(BaseAction):

    def _generate_plan(self):
        return plan(
            description="Print graph",
            action=None,
            stacks=self.context.get_stacks(),
            targets=self.context.stack_names)

    def run(self, format=None, *args, **kwargs):
        """Generates the underlying graph and brings it.

        """
        plan = self._generate_plan()
        if format == "dot":
            print(plan.graph.to_dot())
        else:
            raise ValueError("Unknown format %s" % format)

"""
Document and automate most commonly performed tasks.

List all commands:
inv --list

Shell tab completion:
http://docs.pyinvoke.org/en/latest/cli.html#shell-tab-completion
"""
from invoke import Collection
from build import tools

ns = Collection(
    tools.build, tools.clean, tools.run, tools.update, tools.html,
    tools.rundocs,
)

Title: Dynamic Click  
Date: 2023-07-10  
Tags: notes, click   
Category: Note  
Summary: Dynamic Click groups and commands.  

Here you will find a Python code snippet that introduces dynamic subcommand loading to your command-line applications
using the Click
library. This innovative approach enhances the efficiency and organization of your CLI tools by loading subcommands on
demand, resulting in faster startup times, reduced memory usage, and a more streamlined user experience.

## How It Works

`LazyLoadGroup` is built upon the concept of lazy loading, which means subcommands are loaded into memory only when they
are actually invoked. This clever strategy offers significant benefits:

1. **Efficient Memory Usage:** Subcommands are loaded as needed, preventing unnecessary memory consumption during the
   application's startup. This is particularly advantageous for larger CLI tools with numerous subcommands.

2. **Faster Startup:** With subcommands loading on demand, your application starts up more quickly, enabling users to
   engage with the CLI almost instantaneously.

3. **Modular Organization:** Subcommands are grouped into separate folders, maintaining a tidy and structured codebase.
   LazyLoadGroup fetches subcommands from their designated locations, ensuring a clean organizational structure.

## Getting Started

1. **Requirements:** Ensure you have Python installed on your system.

2. **Installation:** Copy the provided `LazyLoadGroup` class into your Python project or create a new module containing
   this class.

3. **Integration:** Import the `LazyLoadGroup` class into your Click-based command-line application. Utilize it as a
   replacement for Click's `click.Group` class to leverage the dynamic subcommand loading feature.

4. **Usage:** Add subcommands to their designated folders within your project directory. LazyLoadGroup will
   automatically load these subcommands when invoked by the user.

## Benefits

- Faster startup times
- Reduced memory usage
- Neat and organized subcommand structure
- Seamless integration with Click-based applications
- Easy addition of new features without clutter

## Example

```python
import click
from lazy_load_group import LazyLoadGroup


@click.group(cls=LazyLoadGroup, no_args_is_help=True)
def cli():
    """
    Your main command entry point.
    """


if __name__ == '__main__':
    cli()

```

Example package structure

```shell
project_root/
│
├── cli.py      # Your main script containing the LazyLoadGroup integration
├── lazy_load_group.py  # The provided LazyLoadGroup class
│
└── tasks/              # Directory for organizing subcommands
    │
    ├── group1/         # Example subcommand group 1
    │   ├── command1.py # Subcommand 1 for group 1
    │   ├── command2.py # Subcommand 2 for group 1
    │   └── ...
    │
    ├── group2/         # Example subcommand group 2
    │   ├── command3.py # Subcommand 3 for group 2
    │   ├── command4.py # Subcommand 4 for group 2
    │   └── ...
    │
    └── ...
```

In this example, your main script your_script.py would contain the integration of the LazyLoadGroup class, as shown in
the previous README examples. The lazy_load_group.py file contains the implementation of the LazyLoadGroup class.

The tasks/ directory is where you can organize your subcommands. Each subcommand group has its own folder (e.g.,
group1/, group2/) for better organization. Inside each group folder, you have individual subcommand files (e.g.,
command1.py, command2.py, etc.).

This directory structure allows LazyLoadGroup to dynamically load subcommands from the tasks/ directory on demand,
creating a modular and efficient command-line interface.

## The code

```python
import importlib
import logging
import os
from typing import Callable, List

import click

logger = logging.getLogger(__name__)


class LazyLoadGroup(click.Group):
    """A custom Click Group that lazily loads subcommands from specified packages."""

    def __init__(self, commands_dir: str = "tasks", *args, **kwargs):
        """
        Initialize the LazyLoadGroup.

        Args:
            commands_dir (str): Name of the inner package directory with groups..
        """
        super(LazyLoadGroup, self).__init__(*args, **kwargs)
        self._subcommands_loaded = False
        self.commands_dir = commands_dir

        self._curr_dirname = os.path.dirname(__file__)
        self.source_dir = os.path.join(self._curr_dirname, self.commands_dir)
        self.source_package = os.path.basename(self._curr_dirname) + "." + self.commands_dir

        logger.debug(
            f"LazyLoadGroup initialized with source_dir: {self.source_dir}, source_package: {self.source_package}")

    def list_commands(self, ctx: click.Context) -> List[str]:
        """
        List available subcommands.

        Args:
            ctx (click.Context): Click context.

        Returns:
            List[str]: List of available subcommands.
        """
        if not self._subcommands_loaded:
            self.load_subcommands(ctx)
        return super(LazyLoadGroup, self).list_commands(ctx)

    def load_subcommands(self, ctx: click.Context) -> None:
        """
        Load subcommands dynamically from specified packages.

        Args:
            ctx (click.Context): Click context.
        """
        src_dir = self.source_dir
        logger.debug(f"Loading subcommands from {src_dir}")

        for path in os.listdir(src_dir):
            if path.startswith("_") or path.startswith("."):
                continue
            if not os.path.isdir(os.path.join(src_dir, path)):
                continue
            self.load_group(path)

    def load_group(self, group_name: str):
        logger.debug(f"[Group:{group_name}] Loading new group")
        group = click.Group(name=group_name)
        group_dir = os.path.join(self.source_dir, group_name)

        logger.debug(f"[Group:{group_name}] Looking for commands in path: {group_dir}")
        for filename in os.listdir(group_dir):
            if not filename.endswith('.py'):
                continue
            if filename.startswith("__"):
                continue
            command_name = os.path.splitext(filename)[0]
            logger.debug(f"[Group:{group_name}] Importing a module [{filename}]. Looking for function [{command_name}]")

            command = self.import_command(group_name, command_name)
            group.add_command(command, name=command_name)

            logger.debug(f"[Group:{group_name}] Added command: {command_name}")

        self.add_command(group, name=group_name)

    def import_command(self, module_name: str, command_name: str):
        """
        Import a module dynamically.

        Args:
            module_name (str): Path to the module.
            command_name (str): Name of the command.

        Returns:
            Callable: Imported module.
        """
        module_path = f'{self.source_package}.{module_name}.{command_name}'
        logger.debug(f"Importing module: {module_path}")
        module = importlib.import_module(module_path)
        logger.debug(f"Getting a function: {command_name}")
        function = getattr(module, command_name)
        return function

    def get_command(self, ctx: click.Context, cmd_name: str) -> Callable:
        """
        Get the command function based on the command name.

        Args:
            ctx (click.Context): Click context.
            cmd_name (str): Name of the command.

        Returns:
            Callable: The command function.

        Raises:
            click.ClickException: Raised if the command is not found.
        """
        if cmd_name not in self.commands:
            self.load_group(cmd_name)
        return self.commands[cmd_name]


@click.group(cls=LazyLoadGroup, no_args_is_help=True)
def cli() -> None:
    """
    Main command entry point.
    """


```
Title: Dynamic Click
Date: 10/07/2023  
Tags: notes, click
Status: hidden
Summary: Dynamic Click groups and commands.

As a coding enthusiast, I recently embarked on an intriguing journey to create a dynamic command-line interface (CLI)
using Python's Click library. The challenge? To build a tool that could seamlessly find and execute various commands
based on user input, all while optimizing efficiency and user-friendliness.

### The Challenge

The task at hand was to develop a CLI tool that dynamically recognizes and runs commands from different modules. The
tool needed to decipher user-provided CLI commands, associate them with specific modules, and execute the corresponding
command functions. Additionally, the CLI should load commands only when needed and showcase a clear tree of available
groups and commands for users.

### The Solution

Enter Click, a powerful Python library tailor-made for crafting CLI interfaces. I started by creating a custom Click
Group called LazyLoadGroup. This specialized group was designed to load subcommands from chosen packages only when
required, thus saving resources and boosting performance.

Click's option decorator allowed me to effortlessly integrate options like --config into the main command. Callback
functions paired with these options further streamlined the handling of user input.

To enhance the user experience, I harnessed Python's logging module. This enabled me to provide helpful debug messages,
facilitating a smoother understanding of the CLI's inner workings and aiding in troubleshooting.

### The Learning Experience

My journey in crafting this dynamic CLI opened doors to understanding dynamic module loading, the power of decorators,
and the mechanics of command-line interfaces. Throughout the process, I came to appreciate Python's elegance and the
versatility that libraries like Click bring to the table.

While I encountered some challenges, the experience was incredibly rewarding. I gained insights into the importance of
proper design, modularization, and documentation. Click's capabilities allowed me to create a user-friendly tool that
seamlessly interacts with users.

### The Takeaway

This journey reiterated the joy of exploration and the satisfaction of mastering something new. Python's Click library
became an invaluable asset, and building a dynamic CLI proved to be both a fun and educational endeavor. The project
reinforced the idea that coding is an art, offering opportunities to create meaningful and unique tools.

With Click, I've added a practical skill to my coding toolkit. I look forward to applying this knowledge in future
projects and continuing to explore the ever-evolving world of software development.

```python

import click
import importlib
import json
import os
import logging
from typing import Optional, Callable, ModuleType

logger = logging.getLogger(__name__)


class LazyLoadGroup(click.Group):
    """A custom Click Group that lazily loads subcommands from specified packages."""

    def __init__(self, source_dir: str = 'program/tasks', source_package: Optional[str] = None, *args, **kwargs):
        """
        Initialize the LazyLoadGroup.

        Args:
            source_dir (str): Base directory path for module imports.
            source_package (str): Base package name for module imports.
        """
        super(LazyLoadGroup, self).__init__(*args, **kwargs)
        self._subcommands_loaded = False
        self.source_dir = source_dir
        self.source_package = source_package or source_dir.replace('/', '.')
        logger.debug(
            f"LazyLoadGroup initialized with source_dir: {self.source_dir}, source_package: {self.source_package}")

    def list_commands(self, ctx: click.Context) -> list[str]:
        """
        List available subcommands.

        Args:
            ctx (click.Context): Click context.

        Returns:
            List[str]: List of available subcommands.
        """
        if not self._subcommands_loaded:
            logger.debug("Loading subcommands...")
            self.load_subcommands(ctx)
        return super(LazyLoadGroup, self).list_commands(ctx)

    def load_subcommands(self, ctx: click.Context) -> None:
        """
        Load subcommands dynamically from specified packages.

        Args:
            ctx (click.Context): Click context.
        """
        tasks_dir = self.source_dir
        logger.debug(f"Loading subcommands from {tasks_dir}")

        for dirpath, dirnames, filenames in os.walk(tasks_dir):
            module_name = os.path.basename(dirpath)
            if module_name == 'tasks':
                continue
            self.add_group_with_commands(module_name, filenames)

    def add_group_with_commands(self, module_name: str, filenames: list[str]) -> None:
        """
        Add a group with associated commands.

        Args:
            module_name (str): Name of the module.
            filenames (List[str]): List of filenames in the module directory.
        """
        group = click.Group(name=module_name)
        logger.debug(f"Adding group: {module_name}")

        for filename in filenames:
            if filename.endswith('.py') and filename != '__init__.py':
                submodule_name = os.path.splitext(filename)[0]
                command = self.import_module(f'{module_name}.{submodule_name}')
                group.add_command(command, name=submodule_name)
                logger.debug(f"Added command: {submodule_name}")

        self.add_command(group, name=module_name)
        logger.debug(f"Added group: {module_name}")

    def import_module(self, module_path: str) -> ModuleType:
        """
        Import a module dynamically.

        Args:
            module_path (str): Path to the module.

        Returns:
            Callable: Imported module.
        """
        logger.debug(f"Importing module: {module_path}")
        return importlib.import_module(f'{self.source_package}.{module_path}')

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
        try:
            module = self.import_module(cmd_name)
            function = module.cmd_name
            return function
        except ImportError:
            raise click.ClickException(f"Command '{cmd_name}' not found.")


@click.group(cls=LazyLoadGroup, no_args_is_help=True)
@click.option('--config', type=click.Path(exists=True), callback=load_config, help='Path to configuration file')
def main(config: str) -> None:
    """
    Main command entry point.

    Args:
        config (str): Path to the configuration file.
    """
    if config:
        ctx = click.get_current_context()
        ctx.obj = {'config': config}


if __name__ == '__main__':
    main()


```


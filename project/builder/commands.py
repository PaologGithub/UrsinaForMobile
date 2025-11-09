from setuptools import Command
from project.builder.assets_generator import setup_assets
from direct.dist import commands

class BuildAssetsCommand(Command):
    description = "Generate assets.gen before building UfM"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        print("[build_assets] Generating assets...")
        setup_assets()
        print("[build_assets] Done")

class BDistApps(commands.bdist_apps):
    def run(self) -> None:
        self.run_command("build_assets")
        super().run()
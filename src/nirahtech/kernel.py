import importlib
import os
import sys
from pathlib import Path
from typing import List
import zipimport

class SimpleMicroKernel:
    def __init__(self, plugin_folder: Path = Path("plugins")):
        self.__plugin_folder: Path = plugin_folder
        self.__plugins = {}
    
    def discover_plugins(self) -> List[str]:
        if not self.__plugin_folder.exists():
            self.__plugin_folder.mkdir(parents=True)

        
        plugin_files_names: List[str] = [
                file[:-3] 
                for file in os.listdir(self.__plugin_folder) 
                if Path(self.__plugin_folder, file).is_file() and file.endswith(".py") and file != "__init__.py"
            ]

        return plugin_files_names

    def load_plugins(self):
        plugins_files_names: List[str] = self.discover_plugins()

        for file_name in plugins_files_names:
            module_path: str = f"{self.__plugin_folder.name}.{file_name}"
            try:
                module = importlib.import_module(module_path)
                print(module)
                # print(dir(module))
                # if hasattr(module, "Plugin"):
                if "Plugin" in dir(module):
                    self.__plugins[file_name] = module.Plugin()
            except Exception as error:
                print(f"Impossible de charger le module: {file_name}: {error}")
    def run(self):
        for plugin_name, plugin_instance in self.__plugins.items():
            if (hasattr(plugin_instance, "load")):
                loaded_plugin_data = plugin_instance.load()


class AdvancedMicroKernel:
    def __init__(self, plugin_folder: Path = Path("plugins")):
        self.__plugin_folder: Path = plugin_folder
        self.__plugins = {}

    def load_zipped_plugins(self):
        zip_files = [
            file 
            for file in os.listdir(self.__plugin_folder)
            if file.endswith(".zip")
        ]

        for zip_file in zip_files:
            zip_path: Path = Path(self.__plugin_folder, zip_file)
            # zip_path: Path = self.__plugin_folder / zip_file
            # zip_path: Path = Path(f"{self.__plugin_folder}/{zip_file}")
            plugin_name: str = zip_file[:-4]
            # try:
            if zip_path not in sys.path:
                sys.path.insert(0, zip_path)
                module_name: str = f"{str(self.__plugin_folder)}.{plugin_name}.{plugin_name}"
                module_name: str = f"{str(self.__plugin_folder)}.{plugin_name}"
            # module = importlib.import_module(module_name) # charger __init__.py
            module = zipimport.zipimporter(str(zip_path)).create_module(plugin_name)
            if hasattr(module, "StuffPlugin"):
                self.__plugins[plugin_name] = module.StuffPlugin()
            # except Exception as error:
            #     import traceback
            #     traceback.print_stack(error)
    
    def run_all(self, task_name: str):
        for name, instance in self.__plugins.items():
            if hasattr(instance, task_name):
                method = getattr(instance, task_name)
                result = method()
                print(result)
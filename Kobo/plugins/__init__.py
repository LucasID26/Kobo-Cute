import os
import importlib

path_f = "Kobo/plugins"
file_list = os.listdir(path_f)
p_file = [file for file in file_list if file.endswith(".py") and file != "__init__.py"]

# Loop untuk mengimpor fungsi 
HELP_LIST = ""
for file in p_file:
  module_name = file[:-3]
  exec(f"from . import {module_name}")
  #module = importlib.import_module(f"Yoi.module.{module_name}")
  #func_name = module_name.upper()
    
    # Impor fungsi
  #exec(f"from Yoi.module.{module_name} import {func_name}")
  #help = exec(f"from Yoi.module.{module_name} import HELP")
  #HELP_LIST += f"{func_name} - {help}\n"
  

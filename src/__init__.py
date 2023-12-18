"""
quickinit - Quick scaffolding for coding projects
Usage: 
    import clitool
    clitool.main()

Requirements:
    inquirer
    gitpython 
"""

import sys
import importlib

required = {"inquirer", "gitpython"}
missing = [] 
for package in required:
    try: 
        importlib.import_module(package) 
    except ImportError:  
        missing.append(package)
        
if missing:
   print(f"Missing required dependencies: {missing}")
   sys.exit(1)
   
__version__ = "0.1.0" 

from .clitool import main
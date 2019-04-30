#!/usr/bin/env python
import os
from pathlib import Path

    
new_dir='\.gemaTest'
home= Path.home()
if not os.path.exists(home):
        os.makedirs(new_dir)
print(os.path.dirname(os.path.abspath(__file__)))




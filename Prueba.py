#!/usr/bin/env python
import os
from pathlib import Path

    
new_dir='\.gemaTest'
home= Path.home()
if not os.path.exists(home+new_dir):
        os.makedirs(new_dir)




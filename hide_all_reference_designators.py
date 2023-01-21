"""Script to hide ALL the `Reference designator`s in a KiCAD PCB file
(e.g. `my_pcb.kicad_pcb`) as well as the `Value`s field. 
Place this script anywhere in your computer, execute it with Python 3 
and follow the instrucitons.

Example:
```
$ python3 hide_all_reference_designators.py 
Path to the `board.kicad_pcb` file? /home/me/Desktop/PCB_project/pcb.kicad_pcb
Finished! A backup of 'pcb.kicad_pcb' was created in '/home/me/Desktop/PCB_project/pcb.kicad_pcb.backup'.
```
"""
import pcbnew
from pathlib import Path

path = Path(input('Path to the `board.kicad_pcb` file? ')).resolve()

board_handle = pcbnew.LoadBoard(str(path))

backup_path = path.with_suffix(path.suffix + '.backup')
path.rename(backup_path)

board = board_handle.GetBoard()

for footprint in board.GetFootprints():
	footprint.Reference().SetVisible(False)
	footprint.Value().SetVisible(False)

board.Save(str(path))

print(f'Finished! A backup of {repr(path.parts[-1])} was created in {repr(str(backup_path))}.')

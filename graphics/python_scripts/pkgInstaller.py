import os
from pathlib import Path


path = str(Path(os.path.abspath(__file__)).parent.parent.parent)
filePath = Path(path + '/thesis-template.cls')

with open(filePath) as f:
    datafile = f.readlines()
    pkgList = list()

    for line in datafile:
        if 'RequirePackage' in line:
            pkgName = line.split('{')[-1].split('}')[0]
            print(pkgName)
            pkgList.append(pkgName)

os.system('tlmgr --version')
os.system('tlmgr update --self')


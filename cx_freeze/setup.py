import sys
from cx_Freeze import setup, Executable

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
]

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    include_files = []
else:
    # Inclusion of extra plugins (new in cx_Freeze 6.8b2)
    # cx_Freeze imports automatically the following plugins depending of the
    # use of some modules:
    # imageformats - QtGui
    # platforms - QtGui
    # mediaservice - QtMultimedia
    # printsupport - QtPrintSupport
    #
    # So, "platforms" is used here for demonstration purposes.
    include_files = get_qt_plugins_paths("PyQt5", "platforms")

# Dependencies are automatically detected, but it might need
# fine tuning.

build_exe_options = {
    "excludes": [],
    "include_msvcr": True,
    "include_files": include_files
}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable(
        'main.py',
        base=base,
        target_name='RVZ Support',
        copyright="Copyright (C) 2021 cx_Freeze",
        icon="./cx_freeze/icon.ico",
        shortcutName="RVZ Support",
        shortcutDir="MyProgramMenu",
    )
]

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, "This is a description", "IconId", None),
    ],
    "Icon": [
        ("IconId", "./cx_freeze/icon.ico"),
    ],
}

bdist_msi_options = {
    "add_to_path": False,
    "data": msi_data,
    "initial_target_dir": "C:\Program Files (x86)\RVZ Support",
    "install_icon": "./cx_freeze/icon.ico",
}

setup(name='rvz_support',
      version='0.1',
      description='Support for RVZ Servers',
      options={
          'build_exe': build_exe_options,
          'bdist_msi': bdist_msi_options
      },
      executables=executables)

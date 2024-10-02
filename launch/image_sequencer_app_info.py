#!/usr/bin/env python
#
# Copyright (c) 2024 Numurus, LLC <https://www.numurus.com>.
#
# This file is part of nepi-engine
# (see https://github.com/nepi-engine).
#
# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#

APP_NAME = 'Image_Sequencer' # Use in display menus
FILE_TYPE = 'APP'
APP_DICT = dict(
    description = 'Application for configuring a single ros topic from multiple sensor or other image sources',
    pkg_name = 'nepi_app_image_sequencer',
    config_file = 'app_image_sequencer.yaml',
    app_file = 'sequential_image_mux.py',
    node_name = 'app_image_sequencer'
)
RUI_DICT = dict(
    rui_menu_name = 'Image Sequencer', # RUI menu name or "None" if no rui support
    rui_files = ['NepiAppImageSequencer.js'],
    rui_main_file ='NepiAppImageSequencer.js',
    rui_main_class = 'NepiAppImageSequencer'
)



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
DESCRIPTION = 'Application for configuring a single ros topic from multiple sensor or other image sources'
PKG_NAME = 'nepi_app_image_sequencer'
APP_FILE = 'sequential_image_mux.py'
NODE_NAME = 'app_image_sequencer'
RUI_FILES = ['NepiAppImageSequencer.js']
RUI_MAIN_FILE = 'NepiAppImageSequencer.js'
RUI_MAIN_CLASS = "NepiAppImageSequencer"
RUI_MENU_NAME = "Image Sequencer"



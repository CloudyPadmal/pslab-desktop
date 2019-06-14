# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from layouts import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pslab_main_window(object):
    def setupUi(self, pslab_main_window):
        pslab_main_window.setObjectName("pslab_main_window")
        pslab_main_window.resize(460, 610)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            pslab_main_window.sizePolicy().hasHeightForWidth())
        pslab_main_window.setSizePolicy(sizePolicy)
        pslab_main_window.setMinimumSize(QtCore.QSize(460, 610))
        pslab_main_window.setMaximumSize(QtCore.QSize(460, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/app_logo/pslab_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pslab_main_window.setWindowIcon(icon)
        pslab_main_window.setWindowOpacity(1.0)
        pslab_main_window.setToolTipDuration(-1)
        pslab_main_window.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        pslab_main_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        pslab_main_window.setUnifiedTitleAndToolBarOnMac(False)
        self.app_window = QtWidgets.QWidget(pslab_main_window)
        self.app_window.setObjectName("app_window")
        self.gridLayout = QtWidgets.QGridLayout(self.app_window)
        self.gridLayout.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.app_tabs = QtWidgets.QTabWidget(self.app_window)
        self.app_tabs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_tabs.setAutoFillBackground(False)
        self.app_tabs.setStyleSheet("QTabWidget::tab-bar {\n"
                                    "    alignment: center;\n"
                                    "}")
        self.app_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.app_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.app_tabs.setIconSize(QtCore.QSize(24, 24))
        self.app_tabs.setElideMode(QtCore.Qt.ElideNone)
        self.app_tabs.setMovable(False)
        self.app_tabs.setTabBarAutoHide(False)
        self.app_tabs.setObjectName("app_tabs")
        self.tab_instruments = QtWidgets.QWidget()
        self.tab_instruments.setObjectName("tab_instruments")
        self.frame_instruments = QtWidgets.QFrame(self.tab_instruments)
        self.frame_instruments.setGeometry(QtCore.QRect(-1, -1, 441, 533))
        self.frame_instruments.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_instruments.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_instruments.setLineWidth(1)
        self.frame_instruments.setObjectName("frame_instruments")
        self.text_instrument_details = QtWidgets.QTextBrowser(
            self.frame_instruments)
        self.text_instrument_details.setGeometry(
            QtCore.QRect(0, 362, 441, 171))
        self.text_instrument_details.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.text_instrument_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_instrument_details.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.text_instrument_details.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.text_instrument_details.setObjectName("text_instrument_details")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_instruments)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_instruments = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_instruments.setContentsMargins(9, 9, 9, 9)
        self.grid_instruments.setHorizontalSpacing(6)
        self.grid_instruments.setVerticalSpacing(10)
        self.grid_instruments.setObjectName("grid_instruments")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/tab_icons/instrument_tab_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_tabs.addTab(self.tab_instruments, icon1, "")
        self.tab_guide = QtWidgets.QWidget()
        self.tab_guide.setObjectName("tab_guide")
        self.frame_guide = QtWidgets.QFrame(self.tab_guide)
        self.frame_guide.setGeometry(QtCore.QRect(-1, -1, 441, 541))
        self.frame_guide.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_guide.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_guide.setObjectName("frame_guide")
        self.scroll_guide = QtWidgets.QScrollArea(self.frame_guide)
        self.scroll_guide.setGeometry(QtCore.QRect(-1, -1, 441, 541))
        self.scroll_guide.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_guide.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scroll_guide.setWidgetResizable(True)
        self.scroll_guide.setObjectName("scroll_guide")
        self.scroll_area_guide = QtWidgets.QWidget()
        self.scroll_area_guide.setGeometry(QtCore.QRect(0, 0, 441, 541))
        self.scroll_area_guide.setObjectName("scroll_area_guide")
        self.text_area_guide = QtWidgets.QTextBrowser(self.scroll_area_guide)
        self.text_area_guide.setGeometry(QtCore.QRect(0, 0, 441, 534))
        self.text_area_guide.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_area_guide.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_area_guide.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.text_area_guide.setTabChangesFocus(True)
        self.text_area_guide.setDocumentTitle("")
        self.text_area_guide.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_area_guide.setCursorWidth(1)
        self.text_area_guide.setOpenExternalLinks(True)
        self.text_area_guide.setObjectName("text_area_guide")
        self.scroll_guide.setWidget(self.scroll_area_guide)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/tab_icons/guide_tab_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_tabs.addTab(self.tab_guide, icon2, "")
        self.tab_sensors = QtWidgets.QWidget()
        self.tab_sensors.setObjectName("tab_sensors")
        self.frame_sensors = QtWidgets.QFrame(self.tab_sensors)
        self.frame_sensors.setGeometry(QtCore.QRect(-1, -1, 441, 541))
        self.frame_sensors.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_sensors.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_sensors.setObjectName("frame_sensors")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_sensors)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 441, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.grid_sensors = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.grid_sensors.setContentsMargins(0, 0, 0, 0)
        self.grid_sensors.setObjectName("grid_sensors")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/tab_icons/sensor_tab_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_tabs.addTab(self.tab_sensors, icon3, "")
        self.tab_console = QtWidgets.QWidget()
        self.tab_console.setObjectName("tab_console")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/tab_icons/ipython_tab_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_tabs.addTab(self.tab_console, icon4, "")
        self.gridLayout.addWidget(self.app_tabs, 0, 0, 1, 1)
        pslab_main_window.setCentralWidget(self.app_window)
        self.pslab_main_menu = QtWidgets.QMenuBar(pslab_main_window)
        self.pslab_main_menu.setGeometry(QtCore.QRect(0, 0, 460, 22))
        self.pslab_main_menu.setObjectName("pslab_main_menu")
        self.menuDevice = QtWidgets.QMenu(self.pslab_main_menu)
        self.menuDevice.setObjectName("menuDevice")
        self.menuHelp = QtWidgets.QMenu(self.pslab_main_menu)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExperiments = QtWidgets.QMenu(self.pslab_main_menu)
        self.menuExperiments.setObjectName("menuExperiments")
        self.menuElectronics = QtWidgets.QMenu(self.menuExperiments)
        self.menuElectronics.setObjectName("menuElectronics")
        self.menuBJTs_and_FETs = QtWidgets.QMenu(self.menuElectronics)
        self.menuBJTs_and_FETs.setObjectName("menuBJTs_and_FETs")
        self.menuDiodes = QtWidgets.QMenu(self.menuElectronics)
        self.menuDiodes.setObjectName("menuDiodes")
        self.menuOpAmps = QtWidgets.QMenu(self.menuElectronics)
        self.menuOpAmps.setObjectName("menuOpAmps")
        self.menuOscillators = QtWidgets.QMenu(self.menuElectronics)
        self.menuOscillators.setObjectName("menuOscillators")
        self.menuCommunication = QtWidgets.QMenu(self.menuElectronics)
        self.menuCommunication.setObjectName("menuCommunication")
        self.menuElectrical = QtWidgets.QMenu(self.menuExperiments)
        self.menuElectrical.setObjectName("menuElectrical")
        self.menuFilters = QtWidgets.QMenu(self.menuElectrical)
        self.menuFilters.setObjectName("menuFilters")
        self.menuPhysics = QtWidgets.QMenu(self.menuExperiments)
        self.menuPhysics.setObjectName("menuPhysics")
        self.menuRobotics = QtWidgets.QMenu(self.menuExperiments)
        self.menuRobotics.setObjectName("menuRobotics")
        self.menuSchool_Experiments = QtWidgets.QMenu(self.menuExperiments)
        self.menuSchool_Experiments.setObjectName("menuSchool_Experiments")
        pslab_main_window.setMenuBar(self.pslab_main_menu)
        self.pslab_status_bar = QtWidgets.QStatusBar(pslab_main_window)
        self.pslab_status_bar.setObjectName("pslab_status_bar")
        pslab_main_window.setStatusBar(self.pslab_status_bar)
        self.action_reconnect = QtWidgets.QAction(pslab_main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/menu_icons/reconnect_menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_reconnect.setIcon(icon5)
        self.action_reconnect.setObjectName("action_reconnect")
        self.action_about_device = QtWidgets.QAction(pslab_main_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/menu_icons/about_device_menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_device.setIcon(icon6)
        self.action_about_device.setObjectName("action_about_device")
        self.action_test_device = QtWidgets.QAction(pslab_main_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/menu_icons/test_device_menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_test_device.setIcon(icon7)
        self.action_test_device.setObjectName("action_test_device")
        self.action_pin_Layout = QtWidgets.QAction(pslab_main_window)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/menu_icons/pin_layout_menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pin_Layout.setIcon(icon8)
        self.action_pin_Layout.setObjectName("action_pin_Layout")
        self.action_datasheet = QtWidgets.QAction(pslab_main_window)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(
            ":/pslab/icons/menu_icons/datasheet_menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_datasheet.setIcon(icon9)
        self.action_datasheet.setObjectName("action_datasheet")
        self.action_about_pslab = QtWidgets.QAction(pslab_main_window)
        self.action_about_pslab.setIcon(icon)
        self.action_about_pslab.setObjectName("action_about_pslab")
        self.action_nfet = QtWidgets.QAction(pslab_main_window)
        self.action_nfet.setObjectName("action_nfet")
        self.action_nfet_gs = QtWidgets.QAction(pslab_main_window)
        self.action_nfet_gs.setObjectName("action_nfet_gs")
        self.action_bjt_cb_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_bjt_cb_characteristics.setObjectName(
            "action_bjt_cb_characteristics")
        self.action_bjt_ce_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_bjt_ce_characteristics.setObjectName(
            "action_bjt_ce_characteristics")
        self.action_bjt_input_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_bjt_input_characteristics.setObjectName(
            "action_bjt_input_characteristics")
        self.action_bjt_transfer_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_bjt_transfer_characteristics.setObjectName(
            "action_bjt_transfer_characteristics")
        self.action_transistor_amplifier = QtWidgets.QAction(pslab_main_window)
        self.action_transistor_amplifier.setObjectName(
            "action_transistor_amplifier")
        self.action_diode_iv_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_diode_iv_characteristics.setObjectName(
            "action_diode_iv_characteristics")
        self.action_zener_iv_characteristics = QtWidgets.QAction(
            pslab_main_window)
        self.action_zener_iv_characteristics.setObjectName(
            "action_zener_iv_characteristics")
        self.action_diode_clamping = QtWidgets.QAction(pslab_main_window)
        self.action_diode_clamping.setObjectName("action_diode_clamping")
        self.action_diode_clipping = QtWidgets.QAction(pslab_main_window)
        self.action_diode_clipping.setObjectName("action_diode_clipping")
        self.action_halfwave_rectifier = QtWidgets.QAction(pslab_main_window)
        self.action_halfwave_rectifier.setObjectName(
            "action_halfwave_rectifier")
        self.action_fullwave_rectifier = QtWidgets.QAction(pslab_main_window)
        self.action_fullwave_rectifier.setObjectName(
            "action_fullwave_rectifier")
        self.action_inverting_opamp = QtWidgets.QAction(pslab_main_window)
        self.action_inverting_opamp.setObjectName("action_inverting_opamp")
        self.action_non_inverting_opamp = QtWidgets.QAction(pslab_main_window)
        self.action_non_inverting_opamp.setObjectName(
            "action_non_inverting_opamp")
        self.action_linear_ramp_generator = QtWidgets.QAction(
            pslab_main_window)
        self.action_linear_ramp_generator.setObjectName(
            "action_linear_ramp_generator")
        self.action_precision_rectifier = QtWidgets.QAction(pslab_main_window)
        self.action_precision_rectifier.setObjectName(
            "action_precision_rectifier")
        self.action_opamp_summer = QtWidgets.QAction(pslab_main_window)
        self.action_opamp_summer.setObjectName("action_opamp_summer")
        self.action_astable_multivibrator = QtWidgets.QAction(
            pslab_main_window)
        self.action_astable_multivibrator.setObjectName(
            "action_astable_multivibrator")
        self.action_colpitts = QtWidgets.QAction(pslab_main_window)
        self.action_colpitts.setObjectName("action_colpitts")
        self.action_wien_bridge = QtWidgets.QAction(pslab_main_window)
        self.action_wien_bridge.setObjectName("action_wien_bridge")
        self.action_monostable_amplifier = QtWidgets.QAction(pslab_main_window)
        self.action_monostable_amplifier.setObjectName(
            "action_monostable_amplifier")
        self.action_phase_shift_oscillator = QtWidgets.QAction(
            pslab_main_window)
        self.action_phase_shift_oscillator.setObjectName(
            "action_phase_shift_oscillator")
        self.action_amplitude_modulation = QtWidgets.QAction(pslab_main_window)
        self.action_amplitude_modulation.setObjectName(
            "action_amplitude_modulation")
        self.actionBode_Plots = QtWidgets.QAction(pslab_main_window)
        self.actionBode_Plots.setObjectName("actionBode_Plots")
        self.action_low_pass = QtWidgets.QAction(pslab_main_window)
        self.action_low_pass.setObjectName("action_low_pass")
        self.action_high_pass = QtWidgets.QAction(pslab_main_window)
        self.action_high_pass.setObjectName("action_high_pass")
        self.action_transient_rlc_response = QtWidgets.QAction(
            pslab_main_window)
        self.action_transient_rlc_response.setObjectName(
            "action_transient_rlc_response")
        self.action_capacitive_phase_shift = QtWidgets.QAction(
            pslab_main_window)
        self.action_capacitive_phase_shift.setObjectName(
            "action_capacitive_phase_shift")
        self.action_inductive_phase_shift = QtWidgets.QAction(
            pslab_main_window)
        self.action_inductive_phase_shift.setObjectName(
            "action_inductive_phase_shift")
        self.action_lcr_steady_state_response = QtWidgets.QAction(
            pslab_main_window)
        self.action_lcr_steady_state_response.setObjectName(
            "action_lcr_steady_state_response")
        self.action_ohms_law = QtWidgets.QAction(pslab_main_window)
        self.action_ohms_law.setObjectName("action_ohms_law")
        self.action_capacitive_reactance = QtWidgets.QAction(pslab_main_window)
        self.action_capacitive_reactance.setObjectName(
            "action_capacitive_reactance")
        self.action_inductive_reactance = QtWidgets.QAction(pslab_main_window)
        self.action_inductive_reactance.setObjectName(
            "action_inductive_reactance")
        self.action_speed_of_sound = QtWidgets.QAction(pslab_main_window)
        self.action_speed_of_sound.setObjectName("action_speed_of_sound")
        self.action_simple_pendulum = QtWidgets.QAction(pslab_main_window)
        self.action_simple_pendulum.setObjectName("action_simple_pendulum")
        self.action_random_sampling = QtWidgets.QAction(pslab_main_window)
        self.action_random_sampling.setObjectName("action_random_sampling")
        self.action_servo_motors = QtWidgets.QAction(pslab_main_window)
        self.action_servo_motors.setObjectName("action_servo_motors")
        self.action_stepper_motors = QtWidgets.QAction(pslab_main_window)
        self.action_stepper_motors.setObjectName("action_stepper_motors")
        self.action_ac_and_dc_concepts = QtWidgets.QAction(pslab_main_window)
        self.action_ac_and_dc_concepts.setObjectName(
            "action_ac_and_dc_concepts")
        self.action_lemon_cell_experiment = QtWidgets.QAction(
            pslab_main_window)
        self.action_lemon_cell_experiment.setObjectName(
            "action_lemon_cell_experiment")
        self.action_ac_generation = QtWidgets.QAction(pslab_main_window)
        self.action_ac_generation.setObjectName("action_ac_generation")
        self.action_resistance_basics = QtWidgets.QAction(pslab_main_window)
        self.action_resistance_basics.setObjectName("action_resistance_basics")
        self.action_body_resistance = QtWidgets.QAction(pslab_main_window)
        self.action_body_resistance.setObjectName("action_body_resistance")
        self.action_induction_basics = QtWidgets.QAction(pslab_main_window)
        self.action_induction_basics.setObjectName("action_induction_basics")
        self.action_water_resistance = QtWidgets.QAction(pslab_main_window)
        self.action_water_resistance.setObjectName("action_water_resistance")
        self.action_sound_basics = QtWidgets.QAction(pslab_main_window)
        self.action_sound_basics.setObjectName("action_sound_basics")
        self.action_sound_buzzer = QtWidgets.QAction(pslab_main_window)
        self.action_sound_buzzer.setObjectName("action_sound_buzzer")
        self.action_sound_beats = QtWidgets.QAction(pslab_main_window)
        self.action_sound_beats.setObjectName("action_sound_beats")
        self.action_capacitance_basics = QtWidgets.QAction(pslab_main_window)
        self.action_capacitance_basics.setObjectName(
            "action_capacitance_basics")
        self.action_capacitor_discharge = QtWidgets.QAction(pslab_main_window)
        self.action_capacitor_discharge.setObjectName(
            "action_capacitor_discharge")
        self.action_light_dependant_diodes = QtWidgets.QAction(
            pslab_main_window)
        self.action_light_dependant_diodes.setObjectName(
            "action_light_dependant_diodes")
        self.action_sensors = QtWidgets.QAction(pslab_main_window)
        self.action_sensors.setObjectName("action_sensors")
        self.menuDevice.addAction(self.action_reconnect)
        self.menuDevice.addAction(self.action_test_device)
        self.menuDevice.addSeparator()
        self.menuDevice.addAction(self.action_about_device)
        self.menuHelp.addAction(self.action_pin_Layout)
        self.menuHelp.addAction(self.action_datasheet)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_about_pslab)
        self.menuBJTs_and_FETs.addAction(self.action_nfet)
        self.menuBJTs_and_FETs.addAction(self.action_nfet_gs)
        self.menuBJTs_and_FETs.addSeparator()
        self.menuBJTs_and_FETs.addAction(self.action_bjt_cb_characteristics)
        self.menuBJTs_and_FETs.addAction(self.action_bjt_ce_characteristics)
        self.menuBJTs_and_FETs.addAction(self.action_bjt_input_characteristics)
        self.menuBJTs_and_FETs.addAction(
            self.action_bjt_transfer_characteristics)
        self.menuBJTs_and_FETs.addSeparator()
        self.menuBJTs_and_FETs.addAction(self.action_transistor_amplifier)
        self.menuDiodes.addAction(self.action_diode_iv_characteristics)
        self.menuDiodes.addAction(self.action_zener_iv_characteristics)
        self.menuDiodes.addSeparator()
        self.menuDiodes.addAction(self.action_diode_clamping)
        self.menuDiodes.addAction(self.action_diode_clipping)
        self.menuDiodes.addSeparator()
        self.menuDiodes.addAction(self.action_halfwave_rectifier)
        self.menuDiodes.addAction(self.action_fullwave_rectifier)
        self.menuOpAmps.addAction(self.action_inverting_opamp)
        self.menuOpAmps.addAction(self.action_non_inverting_opamp)
        self.menuOpAmps.addAction(self.action_linear_ramp_generator)
        self.menuOpAmps.addAction(self.action_precision_rectifier)
        self.menuOpAmps.addAction(self.action_opamp_summer)
        self.menuOscillators.addAction(self.action_astable_multivibrator)
        self.menuOscillators.addAction(self.action_colpitts)
        self.menuOscillators.addAction(self.action_wien_bridge)
        self.menuOscillators.addAction(self.action_monostable_amplifier)
        self.menuOscillators.addSeparator()
        self.menuOscillators.addAction(self.action_phase_shift_oscillator)
        self.menuCommunication.addAction(self.action_amplitude_modulation)
        self.menuElectronics.addAction(self.menuBJTs_and_FETs.menuAction())
        self.menuElectronics.addAction(self.menuDiodes.menuAction())
        self.menuElectronics.addAction(self.menuOpAmps.menuAction())
        self.menuElectronics.addAction(self.menuOscillators.menuAction())
        self.menuElectronics.addAction(self.menuCommunication.menuAction())
        self.menuFilters.addAction(self.action_low_pass)
        self.menuFilters.addAction(self.action_high_pass)
        self.menuElectrical.addAction(self.actionBode_Plots)
        self.menuElectrical.addSeparator()
        self.menuElectrical.addAction(self.menuFilters.menuAction())
        self.menuElectrical.addAction(self.action_transient_rlc_response)
        self.menuElectrical.addAction(self.action_capacitive_phase_shift)
        self.menuElectrical.addAction(self.action_inductive_phase_shift)
        self.menuElectrical.addAction(self.action_lcr_steady_state_response)
        self.menuElectrical.addSeparator()
        self.menuElectrical.addAction(self.action_ohms_law)
        self.menuElectrical.addAction(self.action_inductive_reactance)
        self.menuElectrical.addAction(self.action_capacitive_reactance)
        self.menuPhysics.addAction(self.action_speed_of_sound)
        self.menuPhysics.addAction(self.action_simple_pendulum)
        self.menuPhysics.addAction(self.action_random_sampling)
        self.menuRobotics.addAction(self.action_servo_motors)
        self.menuRobotics.addAction(self.action_stepper_motors)
        self.menuRobotics.addSeparator()
        self.menuRobotics.addAction(self.action_sensors)
        self.menuSchool_Experiments.addAction(self.action_ac_and_dc_concepts)
        self.menuSchool_Experiments.addAction(self.action_ac_generation)
        self.menuSchool_Experiments.addSeparator()
        self.menuSchool_Experiments.addAction(self.action_resistance_basics)
        self.menuSchool_Experiments.addAction(self.action_body_resistance)
        self.menuSchool_Experiments.addAction(self.action_water_resistance)
        self.menuSchool_Experiments.addSeparator()
        self.menuSchool_Experiments.addAction(self.action_capacitance_basics)
        self.menuSchool_Experiments.addAction(self.action_capacitor_discharge)
        self.menuSchool_Experiments.addSeparator()
        self.menuSchool_Experiments.addAction(self.action_induction_basics)
        self.menuSchool_Experiments.addSeparator()
        self.menuSchool_Experiments.addAction(self.action_sound_basics)
        self.menuSchool_Experiments.addAction(self.action_sound_beats)
        self.menuSchool_Experiments.addAction(self.action_sound_buzzer)
        self.menuSchool_Experiments.addSeparator()
        self.menuSchool_Experiments.addAction(
            self.action_lemon_cell_experiment)
        self.menuSchool_Experiments.addAction(
            self.action_light_dependant_diodes)
        self.menuExperiments.addAction(self.menuElectronics.menuAction())
        self.menuExperiments.addAction(self.menuElectrical.menuAction())
        self.menuExperiments.addAction(self.menuPhysics.menuAction())
        self.menuExperiments.addAction(
            self.menuSchool_Experiments.menuAction())
        self.menuExperiments.addSeparator()
        self.menuExperiments.addAction(self.menuRobotics.menuAction())
        self.pslab_main_menu.addAction(self.menuDevice.menuAction())
        self.pslab_main_menu.addAction(self.menuHelp.menuAction())
        self.pslab_main_menu.addAction(self.menuExperiments.menuAction())

        self.retranslateUi(pslab_main_window)
        self.app_tabs.setCurrentIndex(0)
        self.action_reconnect.triggered.connect(
            pslab_main_window.maction_reconnect_device)
        self.action_test_device.triggered.connect(
            pslab_main_window.maction_test_device)
        self.action_about_device.triggered.connect(
            pslab_main_window.maction_about_device)
        self.action_pin_Layout.triggered.connect(
            pslab_main_window.maction_pinlayout)
        self.action_datasheet.triggered.connect(
            pslab_main_window.maction_datasheet)
        self.action_about_pslab.triggered.connect(
            pslab_main_window.maction_about_pslab)
        self.action_sensors.triggered.connect(
            pslab_main_window.maction_experiments)
        self.action_ac_and_dc_concepts.triggered.connect(
            pslab_main_window.maction_experiments)
        self.action_ac_generation.triggered.connect(
            pslab_main_window.maction_experiments)
        QtCore.QMetaObject.connectSlotsByName(pslab_main_window)

    def retranslateUi(self, pslab_main_window):
        _translate = QtCore.QCoreApplication.translate
        pslab_main_window.setWindowTitle(_translate(
            "pslab_main_window", "PSLab Desktop App"))
        self.text_instrument_details.setHtml(_translate("pslab_main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_instrument_details.setPlaceholderText(_translate(
            "pslab_main_window", "Hover over an instrument to view more details about it..."))
        self.app_tabs.setTabText(self.app_tabs.indexOf(
            self.tab_instruments), _translate("pslab_main_window", "Instruments"))
        self.app_tabs.setTabToolTip(self.app_tabs.indexOf(self.tab_instruments), _translate(
            "pslab_main_window", "Instruments provided by PSLab"))
        self.text_area_guide.setHtml(_translate("pslab_main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_area_guide.setPlaceholderText(_translate(
            "pslab_main_window", "Guide for the selected instrument will be displayed here..."))
        self.app_tabs.setTabText(self.app_tabs.indexOf(
            self.tab_guide), _translate("pslab_main_window", "Guide"))
        self.app_tabs.setTabText(self.app_tabs.indexOf(
            self.tab_sensors), _translate("pslab_main_window", "Sensors"))
        self.app_tabs.setTabText(self.app_tabs.indexOf(
            self.tab_console), _translate("pslab_main_window", "Console"))
        self.menuDevice.setTitle(_translate("pslab_main_window", "Device"))
        self.menuHelp.setTitle(_translate("pslab_main_window", "Help"))
        self.menuExperiments.setTitle(
            _translate("pslab_main_window", "Experiments"))
        self.menuElectronics.setTitle(
            _translate("pslab_main_window", "Electronics"))
        self.menuBJTs_and_FETs.setTitle(
            _translate("pslab_main_window", "Transistors"))
        self.menuDiodes.setTitle(_translate("pslab_main_window", "Diodes"))
        self.menuOpAmps.setTitle(_translate("pslab_main_window", "OpAmps"))
        self.menuOscillators.setTitle(
            _translate("pslab_main_window", "Oscillators"))
        self.menuCommunication.setTitle(
            _translate("pslab_main_window", "Communication"))
        self.menuElectrical.setTitle(
            _translate("pslab_main_window", "Electrical"))
        self.menuFilters.setTitle(_translate("pslab_main_window", "Filters"))
        self.menuPhysics.setTitle(_translate("pslab_main_window", "Physics"))
        self.menuRobotics.setTitle(_translate("pslab_main_window", "Robotics"))
        self.menuSchool_Experiments.setTitle(
            _translate("pslab_main_window", "School Experiments"))
        self.action_reconnect.setText(
            _translate("pslab_main_window", "Reconnect"))
        self.action_reconnect.setToolTip(_translate(
            "pslab_main_window", "Reconnect to PSLab device"))
        self.action_reconnect.setShortcut(
            _translate("pslab_main_window", "Ctrl+Alt+R"))
        self.action_about_device.setText(
            _translate("pslab_main_window", "About..."))
        self.action_test_device.setText(_translate(
            "pslab_main_window", "Test Device..."))
        self.action_pin_Layout.setText(_translate(
            "pslab_main_window", "Pin Layout..."))
        self.action_datasheet.setText(_translate(
            "pslab_main_window", "Datasheet..."))
        self.action_about_pslab.setText(_translate(
            "pslab_main_window", "About PSLab..."))
        self.action_nfet.setText(_translate(
            "pslab_main_window", "NFET Input Characteristics"))
        self.action_nfet_gs.setText(_translate(
            "pslab_main_window", "NFET Output Characteristics"))
        self.action_bjt_cb_characteristics.setText(
            _translate("pslab_main_window", "BJT CB Characteristics"))
        self.action_bjt_ce_characteristics.setText(
            _translate("pslab_main_window", "BJT CE Characteristics"))
        self.action_bjt_input_characteristics.setText(
            _translate("pslab_main_window", "BJT Input Characteristics"))
        self.action_bjt_transfer_characteristics.setText(
            _translate("pslab_main_window", "BJT Transfer Characteristics"))
        self.action_transistor_amplifier.setText(
            _translate("pslab_main_window", "Transistor Amplifier"))
        self.action_diode_iv_characteristics.setText(
            _translate("pslab_main_window", "Diode IV Characteristics"))
        self.action_zener_iv_characteristics.setText(
            _translate("pslab_main_window", "Zener IV Characteristics"))
        self.action_diode_clamping.setText(
            _translate("pslab_main_window", "Diode Clamping"))
        self.action_diode_clipping.setText(
            _translate("pslab_main_window", "Diode Clipping"))
        self.action_halfwave_rectifier.setText(
            _translate("pslab_main_window", "Halfwave Rectifier"))
        self.action_fullwave_rectifier.setText(
            _translate("pslab_main_window", "Fullwave Rectifier"))
        self.action_inverting_opamp.setText(
            _translate("pslab_main_window", "Inverting OpAmp"))
        self.action_non_inverting_opamp.setText(
            _translate("pslab_main_window", "Non Inverting OpAmp"))
        self.action_linear_ramp_generator.setText(
            _translate("pslab_main_window", "Linear Ramp Generator"))
        self.action_precision_rectifier.setText(
            _translate("pslab_main_window", "Precision Rectifier"))
        self.action_opamp_summer.setText(
            _translate("pslab_main_window", "OpAmp Summer"))
        self.action_astable_multivibrator.setText(
            _translate("pslab_main_window", "Astable Multivibrator"))
        self.action_colpitts.setText(_translate(
            "pslab_main_window", "Colpitts Oscillator"))
        self.action_wien_bridge.setText(
            _translate("pslab_main_window", "Wien Bridge"))
        self.action_monostable_amplifier.setText(_translate(
            "pslab_main_window", "Monostable Multivibrator"))
        self.action_phase_shift_oscillator.setText(
            _translate("pslab_main_window", "Phase Shift Oscillator"))
        self.action_amplitude_modulation.setText(
            _translate("pslab_main_window", "Amplitude Modulation"))
        self.actionBode_Plots.setText(
            _translate("pslab_main_window", "Bode Plots"))
        self.action_low_pass.setText(
            _translate("pslab_main_window", "Low Pass"))
        self.action_high_pass.setText(
            _translate("pslab_main_window", "High Pass"))
        self.action_transient_rlc_response.setText(
            _translate("pslab_main_window", "Transient RLC Response"))
        self.action_capacitive_phase_shift.setText(
            _translate("pslab_main_window", "Capacitive Phase Shift"))
        self.action_inductive_phase_shift.setText(
            _translate("pslab_main_window", "Inductive Phase Shift"))
        self.action_lcr_steady_state_response.setText(
            _translate("pslab_main_window", "LCR Steady State Response"))
        self.action_ohms_law.setText(
            _translate("pslab_main_window", "Ohm\'s Law"))
        self.action_capacitive_reactance.setText(
            _translate("pslab_main_window", "Capacitive Reactance"))
        self.action_inductive_reactance.setText(
            _translate("pslab_main_window", "Inductive Reactance"))
        self.action_speed_of_sound.setText(
            _translate("pslab_main_window", "Speed of Sound"))
        self.action_simple_pendulum.setText(
            _translate("pslab_main_window", "Simple Pendulum"))
        self.action_random_sampling.setText(
            _translate("pslab_main_window", "Random Sampling"))
        self.action_servo_motors.setText(
            _translate("pslab_main_window", "Servo Motors"))
        self.action_stepper_motors.setText(
            _translate("pslab_main_window", "Stepper Motors"))
        self.action_ac_and_dc_concepts.setText(
            _translate("pslab_main_window", "AC and DC Concepts"))
        self.action_lemon_cell_experiment.setText(
            _translate("pslab_main_window", "Lemon Cell Experiment"))
        self.action_ac_generation.setText(
            _translate("pslab_main_window", "AC Generation"))
        self.action_resistance_basics.setText(
            _translate("pslab_main_window", "Resistance Basics"))
        self.action_body_resistance.setText(
            _translate("pslab_main_window", "Body Resistance"))
        self.action_induction_basics.setText(
            _translate("pslab_main_window", "Induction Basics"))
        self.action_water_resistance.setText(
            _translate("pslab_main_window", "Water Resistance"))
        self.action_sound_basics.setText(
            _translate("pslab_main_window", "Sound Basics"))
        self.action_sound_buzzer.setText(
            _translate("pslab_main_window", "Sound Buzzer"))
        self.action_sound_beats.setText(
            _translate("pslab_main_window", "Sound Beats"))
        self.action_capacitance_basics.setText(
            _translate("pslab_main_window", "Capacitance Basics"))
        self.action_capacitor_discharge.setText(
            _translate("pslab_main_window", "Capacitor Discharge"))
        self.action_light_dependant_diodes.setText(
            _translate("pslab_main_window", "Light Dependant Diodes"))
        self.action_sensors.setText(_translate(
            "pslab_main_window", "Sensors..."))

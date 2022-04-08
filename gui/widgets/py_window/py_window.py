# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.core.functions import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT STYLES
# ///////////////////////////////////////////////////////////////
from . styles import Styles
# IMPORT BUTTONS
from  .py_page_button import PyPageButton
# PY WINDOW
# ///////////////////////////////////////////////////////////////
class PyWindow(QFrame):

    clicked = Signal(object)
    released = Signal(object)

    def __init__(
        self,
        parent,
        layout = Qt.Vertical,
        margin = 0,
        spacing = 2,
        bg_color = "#2c313c",
        text_color = "#fff",
        text_font = "9pt 'Segoe UI'",
        border_radius = 10,
        border_size = 2,
        border_color = "#343b48",
        enable_shadow = True
    ):
        super().__init__()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self.parent = parent
        self.layout = layout
        self.margin = margin
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_font = text_font
        self.border_radius = border_radius
        self.border_size = border_size
        self.border_color = border_color
        self.enable_shadow = enable_shadow

        # OBJECT NAME
        # ///////////////////////////////////////////////////////////////   
        self.setObjectName("pod_bg_app")

        # APPLY STYLESHEET
        # /////////////////////////////////////////////////////////////// 
        self.set_stylesheet()

        # ADD LAYOUT
        # ///////////////////////////////////////////////////////////////
        if layout == Qt.Vertical:
            # VERTICAL LAYOUT
            self.layout = QHBoxLayout(self)
        else:
            # HORIZONTAL LAYOUT
            self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(margin, margin, margin, margin)
        self.layout.setSpacing(spacing)

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            if enable_shadow:
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(20)
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.shadow.setColor(QColor(0, 0, 0, 160))
                self.setGraphicsEffect(self.shadow)

    # APPLY AND UPDATE STYLESHEET
    # ///////////////////////////////////////////////////////////////
    def set_stylesheet(
        self,
        bg_color = None,
        border_radius = None,
        border_size = None,
        border_color = None,
        text_color = None,
        text_font = None
    ):
        # CHECK BG COLOR
        if bg_color != None: internal_bg_color = bg_color
        else: internal_bg_color = self.bg_color

        # CHECK BORDER RADIUS
        if border_radius != None: internal_border_radius = border_radius
        else: internal_border_radius = self.border_radius

        # CHECK BORDER SIZE
        if border_size != None: internal_border_size = border_size
        else: internal_border_size = self.border_size

        # CHECK BORDER COLOR
        if text_color != None: internal_text_color = text_color
        else: internal_text_color = self.text_color

        # CHECK TEXT COLOR
        if border_color != None: internal_border_color = border_color
        else: internal_border_color = self.border_color

        # CHECK TEXT COLOR
        if text_font != None: internal_text_font = text_font
        else: internal_text_font = self.text_font

        self.setStyleSheet(Styles.bg_style.format(
            _bg_color = internal_bg_color,
            _border_radius = internal_border_radius,
            _border_size = internal_border_size,
            _border_color = internal_border_color,
            _text_color = internal_text_color,
            _text_font = internal_text_font
        ))

    def add_pages(self, parameters):
        if parameters != None:
            for parameter in parameters:
                _btn_icon = parameter['btn_icon']
                _btn_id = parameter['btn_id']
                _btn_text = parameter['btn_text']
                _btn_tooltip = parameter['btn_tooltip']
                _show_top = parameter['show_top']
                _is_active = parameter['is_active']

                self.page = PyPageButton(
                    self._app_parent,
                    text=_btn_text,
                    btn_id=_btn_id,
                    tooltip_text=_btn_tooltip,
                    dark_one=self._dark_one,
                    dark_three=self._dark_three,
                    dark_four=self._dark_four,
                    bg_one=self._bg_one,
                    icon_color=self._icon_color,
                    icon_color_hover=self._icon_color_active,
                    icon_color_pressed=self._icon_color_pressed,
                    icon_color_active=self._icon_color_active,
                    context_color=self._context_color,
                    text_foreground=self._text_foreground,
                    text_active=self._text_active,
                    icon_path=_btn_icon,
                    is_active=_is_active
                )
                self.page.clicked.connect(self.btn_clicked)
                self.page.released.connect(self.btn_released)

    def btn_clicked(self):
        self.clicked.emit(self.page)

    def btn_released(self):
        self.released.emit(self.page)


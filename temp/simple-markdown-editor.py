import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, 
                              QHBoxLayout, QWidget, QPushButton, QToolBar, QComboBox,
                              QFontComboBox, QSpinBox, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QTextCursor, QTextCharFormat, QAction, QIcon
import markdown

class MarkdownEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trình chỉnh sửa Markdown WYSIWYG")
        self.setGeometry(100, 100, 800, 600)
        
        # Tạo widget chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout chính
        layout = QVBoxLayout(central_widget)
        
        # Tạo toolbar
        self.create_toolbar()
        
        # Tạo text editor
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Arial", 12))
        layout.addWidget(self.text_edit)
        
        # Kết nối signals
        self.text_edit.selectionChanged.connect(self.update_format_buttons)
        
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Combo box cho heading levels
        self.heading_combo = QComboBox()
        self.heading_combo.addItems(["Normal", "Heading 1", "Heading 2", "Heading 3", "Heading 4", "Heading 5", "Heading 6"])
        self.heading_combo.currentTextChanged.connect(self.apply_heading)
        toolbar.addWidget(QLabel("Tiêu đề: "))
        toolbar.addWidget(self.heading_combo)
        
        toolbar.addSeparator()
        
        # Nút in đậm
        self.bold_btn = QPushButton("B")
        self.bold_btn.setFont(QFont("Arial", 10, QFont.Bold))
        self.bold_btn.setCheckable(True)
        self.bold_btn.clicked.connect(self.toggle_bold)
        self.bold_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.bold_btn)
        
        # Nút in nghiêng
        self.italic_btn = QPushButton("I")
        italic_font = QFont("Arial", 10)
        italic_font.setItalic(True)
        self.italic_btn.setFont(italic_font)
        self.italic_btn.setCheckable(True)
        self.italic_btn.clicked.connect(self.toggle_italic)
        self.italic_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.italic_btn)
        
        # Nút gạch dưới
        self.underline_btn = QPushButton("U")
        underline_font = QFont("Arial", 10)
        underline_font.setUnderline(True)
        self.underline_btn.setFont(underline_font)
        self.underline_btn.setCheckable(True)
        self.underline_btn.clicked.connect(self.toggle_underline)
        self.underline_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.underline_btn)
        
        toolbar.addSeparator()
        
        # Nút bullet list
        self.bullet_btn = QPushButton("•")
        self.bullet_btn.setFont(QFont("Arial", 12))
        self.bullet_btn.clicked.connect(self.insert_bullet_list)
        self.bullet_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.bullet_btn)
        
        # Nút numbered list
        self.number_btn = QPushButton("1.")
        self.number_btn.setFont(QFont("Arial", 10))
        self.number_btn.clicked.connect(self.insert_numbered_list)
        self.number_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.number_btn)
        
        toolbar.addSeparator()
        
        # Nút code
        self.code_btn = QPushButton("< >")
        self.code_btn.setFont(QFont("Courier", 8))
        self.code_btn.clicked.connect(self.insert_code)
        self.code_btn.setFixedSize(35, 30)
        toolbar.addWidget(self.code_btn)
        
        # Nút blockquote
        self.quote_btn = QPushButton('"')
        self.quote_btn.setFont(QFont("Arial", 14))
        self.quote_btn.clicked.connect(self.insert_blockquote)
        self.quote_btn.setFixedSize(30, 30)
        toolbar.addWidget(self.quote_btn)
    
    def apply_heading(self, heading_text):
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.LineUnderCursor)
        
        format = QTextCharFormat()
        
        if heading_text == "Normal":
            format.setFontPointSize(12)
            format.setFontWeight(QFont.Normal)
        elif heading_text == "Heading 1":
            format.setFontPointSize(24)
            format.setFontWeight(QFont.Bold)
        elif heading_text == "Heading 2":
            format.setFontPointSize(20)
            format.setFontWeight(QFont.Bold)
        elif heading_text == "Heading 3":
            format.setFontPointSize(18)
            format.setFontWeight(QFont.Bold)
        elif heading_text == "Heading 4":
            format.setFontPointSize(16)
            format.setFontWeight(QFont.Bold)
        elif heading_text == "Heading 5":
            format.setFontPointSize(14)
            format.setFontWeight(QFont.Bold)
        elif heading_text == "Heading 6":
            format.setFontPointSize(13)
            format.setFontWeight(QFont.Bold)
        
        cursor.mergeCharFormat(format)
        self.text_edit.setTextCursor(cursor)
    
    def toggle_bold(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        
        if self.bold_btn.isChecked():
            format.setFontWeight(QFont.Bold)
        else:
            format.setFontWeight(QFont.Normal)
        
        cursor.mergeCharFormat(format)
        self.text_edit.setTextCursor(cursor)
    
    def toggle_italic(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setFontItalic(self.italic_btn.isChecked())
        cursor.mergeCharFormat(format)
        self.text_edit.setTextCursor(cursor)
    
    def toggle_underline(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setFontUnderline(self.underline_btn.isChecked())
        cursor.mergeCharFormat(format)
        self.text_edit.setTextCursor(cursor)
    
    def insert_bullet_list(self):
        cursor = self.text_edit.textCursor()
        cursor.insertText("• ")
        self.text_edit.setTextCursor(cursor)
    
    def insert_numbered_list(self):
        cursor = self.text_edit.textCursor()
        cursor.insertText("1. ")
        self.text_edit.setTextCursor(cursor)
    
    def insert_code(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            format = QTextCharFormat()
            format.setFontFamily("Courier New")
            format.setBackground(Qt.lightGray)
            cursor.insertText(selected_text, format)
        else:
            format = QTextCharFormat()
            format.setFontFamily("Courier New")
            format.setBackground(Qt.lightGray)
            cursor.insertText("code", format)
            # Di chuyển cursor về trước để user có thể thay thế text
            cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, 4)
            self.text_edit.setTextCursor(cursor)
    
    def insert_blockquote(self):
        cursor = self.text_edit.textCursor()
        # Chuyển đến đầu dòng
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.insertText("> ")
        self.text_edit.setTextCursor(cursor)
    
    def update_format_buttons(self):
        cursor = self.text_edit.textCursor()
        format = cursor.charFormat()
        
        # Cập nhật trạng thái các nút
        self.bold_btn.setChecked(format.fontWeight() == QFont.Bold)
        self.italic_btn.setChecked(format.fontItalic())
        self.underline_btn.setChecked(format.fontUnderline())
        
        # Cập nhật heading combo dựa trên font size
        font_size = format.fontPointSize()
        if font_size >= 24:
            self.heading_combo.setCurrentText("Heading 1")
        elif font_size >= 20:
            self.heading_combo.setCurrentText("Heading 2")
        elif font_size >= 18:
            self.heading_combo.setCurrentText("Heading 3")
        elif font_size >= 16:
            self.heading_combo.setCurrentText("Heading 4")
        elif font_size >= 14:
            self.heading_combo.setCurrentText("Heading 5")
        elif font_size >= 13:
            self.heading_combo.setCurrentText("Heading 6")
        else:
            self.heading_combo.setCurrentText("Normal")

def main():
    app = QApplication(sys.argv)
    
    # Thiết lập style cho ứng dụng
    app.setStyle('Fusion')
    
    editor = MarkdownEditor()
    editor.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

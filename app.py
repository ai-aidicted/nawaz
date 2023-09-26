import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from pytube import YouTube
import webbrowser

# Path where the video will be saved
SAVE_PATH = "./downloads"

class VideoDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('YouTube Video Downloader')
        self.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.url_entry = QLineEdit(self)
        self.url_entry.setPlaceholderText("Enter the YouTube video URL")
        self.url_entry.setStyleSheet("background-color: #333; color: white; padding: 10px;")
        layout.addWidget(self.url_entry)

        self.download_button = QPushButton("Download", self)
        self.download_button.setStyleSheet("background-color: #2ecc71; color: white; padding: 10px; border: none;")
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)

        self.result_label = QLabel("", self)
        self.result_label.setStyleSheet("color: white;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def download_video(self):
        video_url = self.url_entry.text()

        try:
            yt = YouTube(video_url)

            if yt.age_restricted:
                self.result_label.setText("This video is age-restricted.\nOpen in browser to download manually.")
                return

            video_stream = yt.streams.get_highest_resolution()
            print("Downloading the video...")
            video_stream.download(output_path=SAVE_PATH)
            self.result_label.setText("Video downloaded successfully!")
        except Exception as e:
            self.result_label.setText("An error occurred: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    downloader_app = VideoDownloaderApp()
    downloader_app.setStyleSheet("background-color: #2c3e50;")
    downloader_app.show()
    sys.exit(app.exec_())

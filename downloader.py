# https://download.sublimetext.com/Sublime%20Text%20Build%203211.zip
# import libraries
# Qt5 imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
# Normal imports
import sys
import os
import datetime
from time import sleep
from pytube import YouTube
from moviepy.editor import *
import humanize
from urllib import request

# set up ui
LOADUI, _ = loadUiType("DownloaderV2.ui")


# Make the class
class MyApp(QMainWindow, LOADUI):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        QMainWindow.__init__(self)
        LOADUI.__init__(self)  # By me
        self.setupUi(self)
        self.Handle_UiChange()
        self.Handel_Buttons()
        #self.My_Time()
        self.My_Date()
        self.hide_Default_Style_Button()
        # self.Hide_Labels()
        # self.Show_Label1()
        self.Hide_Themes_list()


    # set window change
    def Handle_UiChange(self):
        self.tabWidget.tabBar().setVisible(False)  # hide tabBar
        self.tabWidget_2.tabBar().setVisible(False)  # hide tabBar
        self.setWindowTitle("Downloader")  # set word (Downloader) window title
        self.pushButton_17.setVisible(False)  # hide this button
        self.Macos_style()                    # set MacOs Style

    # connect buttons
    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.Download)
        self.pushButton.clicked.connect(self.Handel_Browse)

        self.pushButton_20.clicked.connect(self.Youtube_Download)
        self.pushButton_21.clicked.connect(self.Handel_youtube_Browse)
        self.pushButton_22.clicked.connect(self.Get_Video_Quality)

        self.pushButton_30.clicked.connect(self.Handel_Audio_Browse)
        self.pushButton_31.clicked.connect(self.Audio_Download)


        self.checkBox.stateChanged.connect(self.Edit_Default_Style)

        self.pushButton_12.clicked.connect(self.Open_Home_Tap)
        self.pushButton_3.clicked.connect(self.Open_Download_Files)
        self.pushButton_7.clicked.connect(self.Open_Download_Videos_Audios)
        self.pushButton_6.clicked.connect(self.Open_Themes)
        self.pushButton_23.clicked.connect(self.Open_Vid_Audio)
        self.pushButton_24.clicked.connect(self.Open_Videos)

        self.pushButton_10.clicked.connect(self.Default_style)
        self.pushButton_16.clicked.connect(self.Default_style)
        self.pushButton_4.clicked.connect(self.Macos_style)
        self.pushButton_11.clicked.connect(self.Macos_style)
        self.pushButton_8.clicked.connect(self.Dark_Orange_style)
        self.pushButton_14.clicked.connect(self.Dark_Orange_style)
        self.pushButton_9.clicked.connect(self.Dark_Blue_style)
        self.pushButton_15.clicked.connect(self.Dark_Blue_style)
        self.pushButton_5.clicked.connect(self.Breeze_Dark_style)
        self.pushButton_13.clicked.connect(self.Breeze_Dark_style)

        self.pushButton_18.clicked.connect(self.Show_Themes_list)
        self.pushButton_17.clicked.connect(self.Hide_Themes_list)

    ####################################################################################################################
    ####################################################################################################################
    # show the present time
    def My_Time(self):
        timer = QTimer(self)
        timer.timeout.connect(self.My_Time)
        timer.start(1000)

        current_time = QTime.currentTime()
        Timer_time = current_time.toString('hh:mm:ss')

        self.textBrowser_2.setText(Timer_time)
        self.textBrowser_8.setText(Timer_time)
        self.textBrowser_3.setText(Timer_time)
        self.textBrowser_6.setText(Timer_time)
        self.textBrowser_10.setText(Timer_time)

    # show the Current date
    def My_Date(self):
        Date = datetime.datetime.now()
        self.textBrowser.setText("%s/%s/%s" % (Date.day, Date.month, Date.year))
        self.textBrowser_9.setText("%s/%s/%s" % (Date.day, Date.month, Date.year))
        self.textBrowser_4.setText("%s/%s/%s" % (Date.day, Date.month, Date.year))
        self.textBrowser_11.setText("%s/%s/%s" % (Date.day, Date.month, Date.year))

    # Hide Labels
    def Hide_Labels(self):
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        self.label_9.setVisible(False)
        self.label_10.setVisible(False)

    # Show Labels   -----------------------------------------
    def Show_Labels(self):
        sleep(.2)
        self.label_5.setVisible(True)
        sleep(.1)
        self.label_6.setVisible(True)
        sleep(.4)
        self.label_7.setVisible(True)
        sleep(.1)
        self.label_8.setVisible(True)
        sleep(.4)
        self.label_9.setVisible(True)
        sleep(.1)
        self.label_10.setVisible(True)

    # show themes list
    def Show_Themes_list(self):
        self.tabWidget.setVisible(False)
        self.groupBox_3.setVisible(True)
        self.pushButton_18.setVisible(False)
        self.pushButton_17.setVisible(True)
        self.pushButton_3.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        self.pushButton_12.setVisible(False)

    # hide themes list
    def Hide_Themes_list(self):
        self.tabWidget.setVisible(True)
        self.groupBox_3.setVisible(False)
        self.pushButton_17.setVisible(False)
        self.pushButton_18.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton_6.setVisible(True)
        self.pushButton_7.setVisible(True)
        self.pushButton_12.setVisible(True)

    ####################################################################################################################
    ####################################################################################################################
    # open Home tap
    def Open_Home_Tap(self):
        self.tabWidget.setCurrentIndex(0)
 
    # open Download Files tap
    def Open_Download_Files(self):
        self.tabWidget.setCurrentIndex(1)

    # open Download Videos tap
    def Open_Download_Videos_Audios(self):
        self.tabWidget.setCurrentIndex(2)

    # open Themes tap
    def Open_Themes(self):
        self.tabWidget.setCurrentIndex(3)

    # open Audio tab in Download Videos Audio tap
    def Open_Vid_Audio(self):

        self.tabWidget_2.setCurrentIndex(1)

    # open Videos tab in Download Videos Audio tap
    def Open_Videos(self):
        self.tabWidget_2.setCurrentIndex(0)

    # hide the button
    def hide_Default_Style_Button(self):
        self.pushButton_10.setVisible(False)

    # Edit button (show/hide)
    def Edit_Default_Style(self, state):
        if state == Qt.Checked:
            self.pushButton_10.setVisible(True)
        else:
            self.pushButton_10.setVisible(False)

    ####################################################################################################################
    ####################################################################################################################
    # percentage for progressbar
    def Handel_progress(self, block_num, block_size, total_size):
        read = block_num * block_size

        if total_size > 0:
            percent = read * 100 / total_size
            self.progressBar.setValue(percent)
            QApplication.processEvents()

    # programming Browse button
    def Handel_Browse(self):
        text = self.lineEdit_3.text()
        p1 = self.lineEdit_3.text().split("/")[0]
        p2 = self.lineEdit_3.text().split("/")[-1]

        label = self.label_15

        if text == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe url")
        elif "http:" in text:
            if p1 == "http:":
                QMessageBox.critical(self, "Be careful !!!",
                                     "The site you want to download the file from \nis not safe, try not to use it again")
        elif "https:" in text:
            if p1 == "https:":
                if "." in p2:
                    save_place = QFileDialog.getExistingDirectory(self, "Select Download Directory")
                    str_save_place = str(save_place)
                    self.lineEdit_2.setText(str_save_place)
                    if str_save_place != "":
                        File_Name = self.lineEdit_3.text().split("/")[-1]
                        str_File_Name = str(File_Name)
                        self.lineEdit_2.setText(self.lineEdit_2.text() + "/")
                        self.lineEdit_2.setText(self.lineEdit_2.text() + str_File_Name)
                else:
                    label.setStyleSheet("color:red")
                    label.setText("The url does not contain \nthe file type (.exe\.png\.zip)")
                    self.lineEdit_3.setText("")
                    self.lineEdit_2.setText("")
            else:
                label.setStyleSheet("color:red")
                label.setText("The url is invalid")
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("")
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_3.setText("")
            self.lineEdit_2.setText("")

    # programming Download button
    def Download(self):
        url = self.lineEdit_3.text()
        save_location = self.lineEdit_2.text()


        p1 = self.lineEdit_3.text().split("/")[0]
        p2 = self.lineEdit_3.text().split("/")[-1]

        label = self.label_15

        if url == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe url")
        elif save_location == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe file path")
        elif "http:" in url:
            if p1 == "http:":
                QMessageBox.critical(self, "Be careful !!!",
                                     "The site you want to download the file from \nis not safe, try not to use it again")
        elif p1 == "https:":
            if "." in p2:
                try:
                    request.urlretrieve(url, save_location, self.Handel_progress)
                except Exception:
                    label.setStyleSheet("color:blue")
                    label.setText("Unknown error, The Download Failed")
                    self.lineEdit_3.setText("")
                    self.lineEdit_2.setText("")
                    self.progressBar.setValue(0)
                    return
                else:
                    label.setStyleSheet("color:blue")
                    label.setText("Download Completed")
                    self.lineEdit_3.setText("")
                    self.lineEdit_2.setText("")
                    self.progressBar.setValue(0)
            else:
                label.setStyleSheet("color:red")
                label.setText("The url does not contain \nthe file type (.exe\.png\.zip)")
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("")
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_3.setText("")
            self.lineEdit_2.setText("")

    ####################################################################################################################
    ####################################################################################################################
    # set world Download completed in label
    def Download_Completed(self):
        self.label_22.setStyleSheet("color:blue")
        self.label_22.setText("Download Completed")

    # handling browse button
    def Handel_youtube_Browse(self):
        text = self.lineEdit_4.text()
        loc = self.lineEdit_3.text()

        label = self.label_22

        if loc != "":   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            label.setStyleSheet("color:red")
            label.setText("Make sure you have not entered \the path ")
        elif "http:" in text:
            QMessageBox.critical(self, "Be careful !!!",
                                 "The site you want to download the file from \nis not safe, try not to use it again")
            self.lineEdit_4.setText("")
        elif "https:" in text:
            try:
                YouTube(text)
            except Exception:
                label.setStyleSheet("color:red")
                label.setText("The url is invalid")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
            else:
                save_place = QFileDialog.getExistingDirectory(self, "Select Download Directory")
                str_save_place = str(save_place)
                self.lineEdit_5.setText(str_save_place)
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")

    # get Quality and set its in comboBox
    def Get_Video_Quality(self):
        video_link = self.lineEdit_4.text()
        chek_pass = self.comboBox.currentIndex()
        print(chek_pass)
        label = self.label_22

        if chek_pass > 0:
            pass
        elif video_link == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe url")

        elif "https:" in video_link:
            try:
                video = YouTube(video_link)
            except Exception:
                label.setStyleSheet("color:red")
                label.setText("The url is invalid")
                self.lineEdit_4.setText("")
            else:
                try:
                    for streams in video.streams.filter(progressive=True, subtype="mp4"):
                        str_streams = str(streams)
                        Quality = str_streams.split('"')
                        show_resolution = Quality[5]
                        size = str(round(streams.filesize/(1024*1024))).split(".")[0]
                        really_size = humanize.naturalsize(size)
                        data = "{} {} {} {}".format("Quality: ",show_resolution, " / Size: ", really_size)
                        self.comboBox.addItem(data)
                        QApplication.processEvents()
                        label.setStyleSheet("color:blue")
                        label.setText("Check Combo Box")
                except Exception:
                    label.setStyleSheet("color:red")
                    label.setText("Unknown Error")
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_4.setText("")

    # programing download button
    def Youtube_Download(self):
        Url = self.lineEdit_4.text()
        location = self.lineEdit_5.text()

        label = self.label_22

        if Url == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe url")
        elif location == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe file path")
        elif "https:" in Url:
            if self.comboBox.currentIndex() > 0:
                try:
                    video = YouTube(Url)
                except Exception:
                    label.setStyleSheet("color:red")
                    label.setText("The url is invalid")
                    self.lineEdit_4.setText("")
                else:
                    try:
                        Quality = self.comboBox.currentIndex() - 1
                        streams = video.streams.filter(progressive=True, subtype="mp4")[Quality]
                        download = streams.download(location)
                        QApplication.processEvents()
                        video.register_on_complete_callback(self.Download_Completed())
                    except Exception:
                        label.setStyleSheet("color:red")
                        label.setText("Unknown Error")
            else:
                label.setStyleSheet("color:red")
                label.setText("Make sure you are press \nthe search quality button \nand choose \nthe video quality from combo box")
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_4.setText("")
    '''
    def on_progress(self, total, received, ratio):
        read_data = received
        if total > 0 :
            download_percentage = read_data * 100 / total
            self.progressBar_2.setValue(download_percentage)
            remaining_time = round(time/60, 2)

            self.label_22.setText(str('{} minutes remaining'.format(remaining_time)))
            QApplication.processEvents()
    '''
    ####################################################################################################################

    # set world Download completed in label
    def Download_Completed_2(self):
        self.label_22.setStyleSheet("color:blue")
        self.label_22.setText("Download Completed")

    # handling browse button
    def Handel_Audio_Browse(self):
        text = self.lineEdit_9.text()
        loc = self.lineEdit_8.text()

        label = self.label_28

        if loc != "":  # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            label.setStyleSheet("color:red")
            label.setText("Make sure you have not entered \the path ")
        elif "http:" in text:
            QMessageBox.critical(self, "Be careful !!!",
                                 "The site you want to download the file from \nis not safe, try not to use it again")
            self.lineEdit_4.setText("")
        elif "https:" in text:
            try:
                YouTube(text)
            except Exception:
                label.setStyleSheet("color:red")
                label.setText("The url is invalid")
                self.lineEdit_9.setText("")
                self.lineEdit_8.setText("")
            else:
                save_place = QFileDialog.getExistingDirectory(self, "Select Download Directory")
                str_save_place = str(save_place)
                self.lineEdit_8.setText(str_save_place)
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_9.setText("")
            self.lineEdit_8.setText("")

    # programing download button
    def Audio_Download(self):
        Url = self.lineEdit_9.text()
        location = self.lineEdit_8.text()
        label = self.label_28
        if Url == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe url")
        elif location == "":
            label.setStyleSheet("color:red")
            label.setText("Make sure you are entered \nthe file path")
        elif "https:" in Url:
            try:
                video = YouTube(Url)
            except Exception:
                label.setStyleSheet("color:red")
                label.setText("The url is invalid")
                self.lineEdit_9.setText("")
            else:
                try:
                    streams = video.streams.filter(mime_type="audio/mp4", subtype='mp4')[0]
                    download = streams.download(location)
                    os.chdir(location)
                    title = video.title
                    filename1 = "{}.mp4".format(title)
                    filename2 = title[:-3] + ".mp3"
                    os.rename(filename1, filename2)
                    video.register_on_complete_callback(self.Download_Completed_2())
                except Exception:
                    label.setStyleSheet("color:red")
                    label.setText("Unknown Error")
        else:
            label.setStyleSheet("color:red")
            label.setText("The url is invalid")
            self.lineEdit_9.setText("")

    ####################################################################################################################
    ########Styles######################################################################################################
    def Default_style(self):
        style = open("themes/Default style.qcc", "r")
        style = style.read()
        self.setStyleSheet(style)

    def Macos_style(self):
        style = open("themes/MacOS Style Sheet.qcc", "r")
        style = style.read()
        self.setStyleSheet(style)

    def Breeze_Dark_style(self):
        style = open("themes/Breeze_Dark_style.qcc", "r")
        style = style.read()
        self.setStyleSheet(style)
        pass

    def Dark_Orange_style(self):
        style = open("themes/Dark_Orange_Style.qcc", "r")
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Blue_style(self):
        style = open("themes/Dark_Blue_Style.qcc", "r")
        style = style.read()
        self.setStyleSheet(style)

    def closeEvent(self, event):
        mbox = QMessageBox.question(self, "Close program", "Are you sure you want close the program?",
                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            event.accept()
        elif mbox == QMessageBox.No:
            event.ignore()



def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

'''

FROM_CLASS,_=loadUiType(path.join(path.dirname(__file__,"download.ui")))
def Handel_Buttons():
    ui.pushButton_2.click.connect(Handel_Download)

        uic.loadUi("download.ui", self)


'''



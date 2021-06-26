# модуль os для манипуляций с фалйами и директориями(создание и удаление)
from datetime import date
import subprocess
import os
import shutil  # shutil для копирования и перемещения файлов
import sys  # sys для корректной работы приложения
from midiutil.MidiFile import MIDIFile
import moviepy.editor as mp  # moviepy для отделения звука от видео
from pytube import YouTube  # pytube для загрузки виедоматериала с YouTube
# виджеты (кнопки, надписи) для пользовательского интерфейса
from PyQt5.QtWidgets import *
# для работы с аппаратной частью мультимедиа(проинрывании музыки, пауза и т.п. )
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *  # для работы с аппаратной частью
# для настройки иконок и интерфейса приложения и всплывающих окон
from PyQt5.QtGui import *
# виджеты для мультимедиа(плеер, модель плейлиста)
from PyQt5.QtMultimediaWidgets import *
# импорт пользовательского интерфейса приложения
from interface.main_interface import Ui_MainWindow
from piano import create_question, create_warning, PianoWindow, Worker
from modules.db_helper import DB_helper
import datetime


class PlaylistModel(QAbstractListModel):
    '''Модель плейлиста. Позволяет получать индекс и название текущего трека,
    изменять путь к треку(необходимо для переименовывания), а также в принципе работать
    с аппартным представлением плейлиста'''

    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def setData(self, index, value, role):
        if role == Qt.DisplayRole:
            self.playlist.removeMedia(index)
            self.playlist.insertMedia(
                index, QMediaContent(QUrl.fromLocalFile(value)))

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


class Main(QMainWindow, Ui_MainWindow):
    '''Главное окно приложения'''
    def __init__(self):
        super().__init__()
        self.con = DB_helper('db/project.db')
        self.file_path = ''  # в этой переменной будет храниться файловый путь до трека
        self.video = ''  # для загрузки видео с YouTube
        self.video_path = ''  # для файлового пути до видео
        self.setupUi(self)  # инициализируем интерфейс
        now = datetime.datetime.now()
        if 21 >= int(now.strftime('%H')) >= 8:
            self.dark_theme_off()
        else:
            self.dark_theme_on()  # включаем обычную(светлую) тему
        
        self.setWindowIcon(QIcon('images/main_icon.png')) # настройка название и иконки главного окна
        self.setWindowTitle('M&S(music and sounds)')
        self.con.create('mp3_playlist', ['track_title', 'way']) # создание необходимых таблиц
        self.con.create('will_remove', ['way_to_track'])
        self.con.create('melody_playlist', ['title', 'way_to_melody'])
        self.player = QMediaPlayer()
        self.threadpool = QThreadPool()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.play()
        self.playlist = QMediaPlaylist()
        self.model = PlaylistModel(self.playlist)
        self.player.setPlaylist(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(
            self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(
            self.playlist_selection_changed)  # инициализация плеера и плейлиста
        self.delete_need()
        self.set_mp3_playlist()
        self.set_melody_playlist()# вставляем треки в плейлист, если есть таковые
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.timeSlider.valueChanged.connect(self.player.setPosition)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.player.durationChanged.connect(self.update_duration)
        # соединяем функции плеера с их виджетами
        self.player.positionChanged.connect(self.update_position)
        self.setAcceptDrops(False)
        # делаем место для навзания трека неизменяемым
        self.lineEdit.setReadOnly(True)
        # инициализация функции выключения темной темы
        self.off_dark.triggered.connect(self.dark_theme_off)
        # инициализация функции включения темной темы
        self.on_dark.triggered.connect(self.dark_theme_on)
        # для красивого оформления(без белой полоски)
        self.tabWidget.setDocumentMode(True)
        self.tab.setAutoFillBackground(True)
        self.tab_2.setAutoFillBackground(True)
        self.changeButton.clicked.connect(self.change)
        self.linkButton.clicked.connect(self.download_from_yt)
        self.openButton_2.clicked.connect(self.open_video)
        self.deleteButton.clicked.connect(self.delete)
        self.openButton.clicked.connect(self.open_file)
        self.playButton_2.clicked.connect(self.watch)
        self.startButton.clicked.connect(self.sound_of_clip)
        self.pianoButton.clicked.connect(self.open_piano)
        self.playButton_3.clicked.connect(self.play_melody)
        self.changeButton_2.clicked.connect(self.change_melody)
        self.deleteButton_2.clicked.connect(self.delete_melody)
        self.openButton_3.clicked.connect(self.add_melody)
        self.piano = PianoWindow(self)
        if 'videos' not in os.listdir():
            os.mkdir('videos')
        if 'music' not in os.listdir():
            os.mkdir('music')

    def open_piano(self):
        '''Метод для открытия пианино'''
        self.piano.show()
        self.set_melody_playlist()

    def delete_need(self):
        '''При запуске удаляем необходимые
        элементы'''
        removing_items = self.con.select('will_remove')
        if removing_items:
            for i in removing_items:
                if i:
                    os.remove(i[0])
                    self.con.delete('will_remove', f"way_to_track='{i[0]}'")
    
    def set_mp3_playlist(self):
        '''При запуске приложения настравиваем основной плейлист'''
        all_mp3 = self.con.select('mp3_playlist')
        all_mp3 = list(set(all_mp3))
        if all_mp3:
            for item in all_mp3:
                if item and os.path.exists(item[1]):
                    if not item[1].endswith('.wav'):
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(item[1])))
                    else:
                        subprocess.call(f'ffmpeg -i {item[1]}  -vn -ar 44100 -ac 2 -b:a 192k music\\{item[0]}.mp3 -y',
                                        shell=True)
                        self.con.update('mp3_playlist', f'way=music/{item[0]}.mp3', f'track_title={item[0]}')
                        self.playlist.addMedia(
                            QMediaContent(QUrl.fromLocalFile(f'music/{item[0]}.mp3')))
                elif not os.path.exists(item[1]):
                    print(self.con.select('mp3_playlist'))
                    self.con.delete('mp3_playlist', f"way='{item[1]}'")
    
    def set_melody_playlist(self):
        '''Настраиваем плейлист с мелодиями пользователя'''
        all_melodies = self.con.select('melody_playlist')
        all_melodies = list(set(all_melodies))
        if all_melodies:
            for melody in all_melodies:
                if melody and os.path.exists(melody[1]):
                    self.listWidget.addItem(f'{melody[0]} (Путь: {melody[1]})')

    def open_file(self):
        '''Открытие музыкального файла в формате mp3, wav и добавление
        его в плейлист на вкладке "Прослушивание музыки"'''
        self.file_path = QFileDialog.getOpenFileName(
            self, 'Выберите .mp3', '', '.MP3(*.mp3);;.WAV(*.wav);;Все файлы(*.*)',
            options=QFileDialog.DontUseNativeDialog)[0]
        if self.file_path and self.file_path.endswith('.mp3') or self.file_path.endswith('.wav'):
            if self.file_path.endswith('.wav'):
                name = self.file_path.split('/')[-1].split('.')[0]
                subprocess.call(f'ffmpeg -i {self.file_path}  -vn -ar 44100 -ac 2 -b:a 192k music\\{name}.mp3 -y',
                                shell=True)
                self.con.insert('mp3_playlist', 2, (f'music/{name}.mp3', name))
                self.file_path = f'music/{name}.mp3'
            else:
                try:
                    shutil.copy(self.file_path, 'music')
                except shutil.Error as se:
                    pass
                self.file_path = 'music/' + self.file_path.split('/')[-1]
                self.con.insert('mp3_playlist', 2,
                     (self.file_path.split('/')[-1].split('.')[0], self.file_path))
            self.playlist.addMedia(QMediaContent(
                QUrl.fromLocalFile(self.file_path)))
            self.lineEdit.setText(
                self.file_path.split('/')[-1].split('.')[0])
            self.model.layoutChanged.emit()
        else:
            create_warning('Выберите MP3 или WAV файлы!')

    def delete(self):
        '''Удаление трека из плейлиста'''
        int_track_index = self.playlist.currentIndex()
        all_tracks = self.con.select('mp3_playlist')
        if int_track_index >= 0:
            remove_or_not = create_question('Вопрос', "Действительно удалить трек с названием: " +
                                            all_tracks[int_track_index][0])
            if remove_or_not:
                self.playlist.removeMedia(int_track_index)
                self.con.delete('mp3_playlist', f"track_title='{all_tracks[int_track_index][0]}'")
                self.con.insert('will_remove', 1, (all_tracks[int_track_index][1], ))
            else:
                create_warning('Отмена операции.')
        else:
            create_warning('Выберите ОДИН любой трек, чтобы удалить!')

    def change(self):
        '''Изменение трека в плейлисте'''
        int_track_index = self.playlist.currentIndex()
        if int_track_index >= 0:
            all_tracks = self.con.select('mp3_playlist')
            if all_tracks:
                if int_track_index <= len(all_tracks) - 1:
                    new_name, ok = QInputDialog.getText(
                        self, 'Изменение', 'Введите нужное название:')
                    if ok:
                        change_or_not = create_question('Изменить название',
                        "Действительно изменить трек с названием: " + all_tracks[int_track_index][0])
                        if change_or_not:
                            try:
                                shutil.copy(
                                    all_tracks[int_track_index][1], f"music/{new_name}.mp3")
                                self.file_path = f"music/{new_name}.mp3"
                                self.con.update('mp3_playlist', f"track_title='{new_name}', way='{self.file_path}'",
                                                f"track_title='{all_tracks[int_track_index][0]}'")
                                self.model.setData(int_track_index, self.file_path, Qt.DisplayRole)
                                self.con.insert('will_remove', 1, (all_tracks[int_track_index][1], ))
                            except Exception as e:
                                if 'are the same file' in str(e):
                                    create_warning(
                                       'Имя файла должно быть отличным от предыдущего!')
                            else:
                                create_warning(
                                    'Имя файла должно включать только буквы и цифры!')
        else:
            create_warning(
                'Выберите из плейлиста ОДИН любой файл, чтобы изменить его название!')

    def download_from_yt(self):
        '''Метод для закачки видео с YouTube.
        Позволяет сохранить видео под любым названием.
        '''
        if not self.video_path:
            if self.linkEdit.text():
                try:
                    video = YouTube(self.linkEdit.text(),
                                    on_progress_callback=self.progress_func)
                    if video.title not in os.listdir('videos'):
                        self.video = video.streams.first()
                        self.video.download('videos')
                        print('успешно')
                        self.progressBar.setValue(0)
                        try:
                            shutil.copy(f"videos/{video.title}.mp4",
                                f'videos/{"".join([i for i in video.title.split(" ")])}.mp4')
                        except Exception:
                            pass
                        self.linkEdit.setText(
                            f'videos/{"".join([i for i in video.title.split(" ")])}.mp4')
                        self.video_path = f'videos/{"".join([i for i in video.title.split(" ")])}.mp4'
                        self.linkEdit.setReadOnly(True)
                    else:
                        create_warning('Видео уже скачано!')
                except Exception as e:
                    print(e)
                    create_warning('Ссылка введена неправильно!')
            if not self.linkEdit.text():
                create_warning('Введите ссылку!')
        else:
            create_warning('Вы уже выбрали видеофайл!')

    def progress_func(self, stream, chunk, bytes_remaining):
        '''Для заполнения полосы загрузки, когда
        скачиваем видел с YouTube'''
        size = self.video.filesize
        progress = (float(abs(bytes_remaining - size) / size)) * float(100)
        self.progressBar.setValue(progress)

    def open_video(self):
        '''Открытие видеофайла'''
        self.video_dialog()
    
    def video_dialog(self):
        '''Диалог для выбора видео'''
        self.video_path = QFileDialog.getOpenFileName(
        self, 'Выберите .mp4', '', '.MP4(*.mp4);;AVI(*.avi)',
        options=QFileDialog.DontUseNativeDialog)[0]
        if self.video_path and self.video_path.endswith('.mp4') or\
                self.video_path.endswith('.avi'):
            norm_path = "".join(self.video_path.split('/')[-1].split('.')[0].split(" "))
            try:
                shutil.copy(self.video_path, f'videos/{norm_path}')
            except shutil.Error:
                pass
            self.video_path = f'videos/{norm_path}'
            self.linkEdit.setText(
                f'videos/{self.video_path.split("/")[-1]}')
        else:
            create_warning('Выберите один видеофайл!')
                    
    def sound_of_clip(self):
        '''Для отделения звука от видеофайла.'''
        if self.video_path:
            clip = mp.VideoFileClip(self.video_path).subclip()
            audio = self.video_path.split('/')[-1]
            save_path = QFileDialog.getSaveFileName(self, 'Сохранить звук', '', '.MP3(*.mp3)',
                                    options=QFileDialog.DontUseNativeDialog)[0]
            if save_path:
                if save_path.endswith('.mp3'):
                    clip.audio.write_audiofile(save_path)
                    question = create_question('Добавить', 'Добавить звук в плейлист?')
                    print(question)
                    if question:
                        try:
                            shutil.copy(
                                save_path, f'music/{save_path.split("/")[-1]}')
                        except Exception as e:
                            pass
                        save_path = 'music/' + save_path.split('/')[-1]
                        save_name = save_path.split('/')[-1].split('.')[0]
                        self.con.insert('mp3_playlist', 2, (save_name, save_path))
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(save_path)))
                        self.playlist.setCurrentIndex(-1)
                        self.set_mp3_playlist()
                    self.linkEdit.setReadOnly(False)
                    self.linkEdit.clear()
                    self.video_path = ''
                else:
                    create_warning('Сохраните как mp3 файл!')
            else:
                create_warning('Введите путь для сохранения!')
        else:
            create_warning('Сначала выберите видео!')

    def watch(self):
        '''Открывает окно предварительного просмотра видео.
        Реализуется с помощью файла "play_clip.py"
        и вызова его с помощью подпроцесса'''
        if self.video_path:
            w = Worker(self.call, 'play_clip', way=self.video_path)
            self.threadpool.start(w)
        else:
            create_warning('Сначала загрузите видео или вставьте ссылку!')

    def play_melody(self):
        '''Проигрывает MID-файл в фоновом режимк с помощью потока'''
        need_melody = self.listWidget.currentItem()
        if need_melody:
            name = need_melody.text()
            way = name.split(' (Путь: ')[1][:-1]
            w = Worker(self.call, 'play_melody', way=way)
            self.threadpool.start(w) 
        else:
            create_warning('Выберите одну мелодию из списка!')

    def delete_melody(self):
        '''Для удаления файла из плейлиста на вкалдке "инструенты".
        Также позволяет удалить файл полностью.'''
        index = self.listWidget.selectedIndexes()
        melody = self.listWidget.currentItem()
        if melody:
            melody= melody.text()
            if len(index) == 1:
                if create_question('Удаление', 'Удалить файл полностью?'):
                    way_to_melody = melody.split('Путь: ')[-1][:-1]
                    self.listWidget.takeItem(index[0].row())
                    os.remove(way_to_melody)
                    self.con.delete('melody_playlist', f"way_to_melody='{way_to_melody}'")
                if create_question('Удаление', 'Удалить элемент из плейлиста?'):
                    self.listWidget.takeItem(index[0].row())
                    way_to_melody = melody.split('Путь: ')[-1][:-1]
                    self.con.delete('melody_playlist', f"way_to_melody='{way_to_melody}'")  
            else:
                create_warning('Выберите только один элемент!')
        else:
            create_warning('Выберите один элемент плейлиста!')

    def change_melody(self):
        '''Для изменения любого предмета в списке на вкладке
        "инструменты". Позволяет изменить имя файла, название в плейлисте,
        расположение файла.'''
        if self.listWidget.currentItem():
            melody = self.listWidget.currentItem()
            way = melody.text().split('(Путь: ')[1][:-1]
            name = melody.text().split(' (Путь:')[0]
            if create_question('Изменение', 'Изменить название трека в плейлисте?'):
                new_name, ok = QInputDialog.getText(self, 'Изменение в плейлисте',
                'Введите новое название в плейлисте:')
                if ok:
                    melody.setText(f'{new_name} (Путь: {way})')
                    self.con.update('melody_playlist', f"title='{new_name}'",
                                    f"way_to_melody='{way}'")
            if create_question('Изменение', 'Изменить имя файла?'):
                new_way, ok = QInputDialog.getText(self, 'Изменение в плейлисте',
                'Введите новое имя файла(без формата):')
                if ok:
                    if '.mid' not in new_way:
                        old_way = way
                        way = '/'.join(way.split('/')[:-1]) + '/' + new_way + '.mid'
                        melody.setText(f'{name} (Путь: {way})')
                        self.con.update('melody_playlist', f"way_to_melody='{way}",
                                        f"title='{name}''")
                        os.rename(old_way, way)
                    else:
                        create_warning('Не надо указывать расширение!')
            if create_question('Изменение', 'Изменить расположение файла?'):
                new_way = QFileDialog.getSaveFileName(self, 'Перемещение', '', '.MID(*.mid)',
                                    options=QFileDialog.DontUseNativeDialog)[0]
                try:
                    shutil.move(way, new_way)
                    self.con.update('melody_playlist', f"way_to_melody='{new_way}'",
                            f"title='{name}'")
                    melody.setText(f'{name} (Путь: {new_way})')
                except shutil.Error:
                    create_warning('Операция прошла неудачно!')
        else:
            create_warning('Сначала выберите мелодию!')
    
    def add_melody(self):
        '''Добавить готовый MIDI-файл в плейлист на вкладке "инструменты"'''
        way = QFileDialog.getOpenFileName(self, 'Добавить в мелодию', '', '.MIDI(*.mid)',
                                          options=QFileDialog.DontUseNativeDialog)[0]
        if way:
            name = way.split('/')[-1].split('.')[0]
            self.listWidget.addItem(f'{name} (Путь: {way})')
            self.con.insert('melody_playlist', 2, (name, way))
        else:
            create_warning('Выберите файл!')
    
    
    def dark_theme_on(self):
        '''включаем темную тему'''
        self.tabWidget.setStyleSheet('background-color: black')
        self.setStyleSheet('''QInputDialog {background-color: black; width: 700px; height: 400px}
                              QPushButton {color: white; border: 2px solid #9a9a9a; border-radius: 7px;}
                              QLabel {color: white}
                              QLineEdit{background-color: black; color: white; border-radius: 7px; border: 2px solid #9a9a9a;}
                              QListView {border: 2px solid #9a9a9a; border-radius: 5px;}
                              QMenuBar{background-color: #000080; color: white; border: 1px solid #990066; border-radius: 7px}
                              QMenuBar::item:selected {background: #0095b6;} 
                              QMenuBar::item:pressed {background: #0095b6;}
                              QTabBar {background-color: #000080;}
                              QTabBar::tab {background-color: black; color: rgb(255, 255, 255); border: 2px solid yellow; border-radius: 3px; width: 190px; height: 25px;}
                              QTabBar::tab:selected, QTabBar::tab:hover {background-color: #0095b6;}
                              QListView {show-decoration-selected: 1;}
                              QListView::item {color: #f0f0f0}
                              QListView::item:selected:active {background: #2f4f4f;}
                              QListView::item:hover {background: #0a5f38; color: yellow} 
                              QSlider::handle {background: #997a8d;border-radius: 5px;}
                              QFileDialog {background-color: black; color: white}
                              QListView {background-color:black}
                              QComboBox{background-color: black; color: white}
                              QProgressBar {color: white;}''')

    def dark_theme_off(self):
        '''выключаем темную тему'''
        self.tabWidget.setStyleSheet('background-color: #5b92e5')
        self.setStyleSheet('''QMessageBox {background-color: #5b92e5; width: 700px; height: 400px}
                              QInputDialog {background-color: #5b92e5; width: 700px}
                              QPushButton {color: #f0f0f0; border: 2px solid #f0f0f0;}
                              QLabel {color: #f0f0f0}
                              QLineEdit{background-color: #5b92e5; color: #f0f0f0; border-radius: 7px; border: 2px solid #f0f0f0;}
                              QListView {border: 1px solid #f0f0f0; border-radius: 5px; color: f0f0f0;}
                              QMenuBar{background-color: #5b92e5; color: #f0f0f0}
                              QMenuBar::item:selected {background: #4040ff;}
                              QMenuBar::item:pressed {background: #4040ff;}
                              QTabBar {background-color: #5b92e5;}
                              QTabBar::tab {background-color: #5b92e5; color: rgb(255, 255, 255); border: 2px solid white; border-radius: 7px; width: 190px; height: 25px;}
                              QTabBar::tab:selected, QTabBar::tab:hover {background-color: #4040ff;}
                              QToolTip{ border: 1px solid white }
                              QListView {show-decoration-selected: 1; background-color: #5b92e5;}
                              QListView::item {color: #f0f0f0}
                              QListView::item:selected {border: 1px solid #6495ed;}
                              QListView::item:selected:active {background: #00a86b;}
                              QListView::item:hover {background: #c9eef6; color: black}
                              QListWidget::item {color: white}
                              QComboBox {color: black; border: 2px solid #c0c0c0; border-radius: 5px; background-color: white;}
                              QComboBox::drop-down {color: black; border: 2px solid black; border-radius: 5px;}
                              QComboBox::down-arrow {color: white; image: url(images/arrow.jpg);}
                              QFileDialog {background-color: #5b92e5;}''')
        
    def hhmmss(self, ms):
        '''Вычисляем длительность трека/аудиофайла'''
        h, r = divmod(ms, 36000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%d:%02d" % (h, s))

    def update_duration(self, duration):
        '''Для того, чтобы узнать продолжительность трека'''
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(self.hhmmss(duration))

    def update_position(self, position):
        '''Для обработки перемотки трека по времени'''
        if position >= 0:
            self.currentTimeLabel.setText(self.hhmmss(position))
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        '''Если в плейлисте выбран какой-то объект'''
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        '''Если в плейлисте по объекту кликнули два раза,
        начинает играть выбранный объект'''
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)
            now_track = str(self.model.data(self.playlistView.currentIndex(), Qt.DisplayRole)).split('.')[0]
            self.lineEdit.setText(now_track)

    def call(self, file, way=''):
        '''Функция для создания подпроцесса.
        Необходима для облегчения создания потокаю'''
        subprocess.call(f'python modules/{file}.py {way}')


if __name__ == '__main__':
    try:
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        app = QApplication(sys.argv)
        m = Main()
        m.show()
        app.exec()
    except OverflowError:
        pass

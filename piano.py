import subprocess
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from interface.piano_interface import Ui_Form
from midiutil.MidiFile import MIDIFile
import sqlite3



def create_warning(text, icon='images/warning.png', title='Внимание!'):
    '''Метод для создания всплывающего
    окна предупреждения, чтобы упростить понимание кода'''
    dialog = QMessageBox()
    dialog.setWindowIcon(QIcon(icon))
    dialog.setWindowTitle(title)
    dialog.setText(text)
    return dialog.exec()


def create_question(title, text):
    '''Метод для создания стандратного(кнопки 'ok', 'cancel')
    всплывающего окна, которое будет что-то спрашивать у пользователя'''
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setWindowIcon(QIcon('question.png'))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    yes_or_no = msg.exec_()
    if yes_or_no == QMessageBox.Ok:
        return True
    return False


class PianoWindow(QWidget, Ui_Form):
    '''Виджет, созданный для того, чтобы имитировать работу
    пианино.'''

    def __init__(self, parent=None):
        super(PianoWindow, self).__init__(parent, Qt.Window)
        self.setupUi(self)
        self.mf = MIDIFile(1)
        self.mf.addTrackName(0, 0, "Piano Track")
        self.mf.addTempo(0, 0, 120)
        self.setWindowIcon(QIcon('images/piano_icon.png'))
        self.volumeSlider.setRange(1, 126)
        self.durationlSlider.setRange(1, 120)
        self.volumeSlider.valueChanged.connect(self.volume_changed)
        self.durationlSlider.valueChanged.connect(self.duration_changed)
        self.comboBox.currentIndexChanged.connect(self.octave_changed)
        self.keyboard.buttonClicked.connect(self.select_note)
        self.addButton.clicked.connect(self.add_note)
        self.playButton.clicked.connect(self.play_melody)
        self.octave = '1'
        self.selected_note = ()
        self.time = 0
        self.duration = 1
        self.volume = 1
        self.isSelected = False
        self.threadpool = QThreadPool()
        self.note_numbers = {'C': [24, 36, 48, 60, 72, 84, 96, 108, 120],  # номера нот, необходимые
                             # для создания MIDI-файла,
                             'C#': [25, 37, 49, 61, 73, 85, 97, 109, 121],
                             # то есть имитации игры какого-то инструмента,
                             'D': [26, 38, 50, 62, 74, 86, 98, 110, 122],
                             # в нашем случае, инструмент - пианино
                             'D#': [27, 39, 51, 63, 75, 87, 99, 111, 123],
                             'E': [28, 40, 52, 64, 76, 88, 100, 112, 124],
                             'F': [29, 41, 53, 65, 77, 89, 101, 113, 125],
                             'F#': [30, 42, 54, 66, 78, 90, 102, 114, 126],
                             'G': [31, 43, 55, 67, 79, 91, 103, 115, 127],
                             'G#': [32, 44, 56, 68, 80, 92, 104, 116],
                             'A': [33, 45, 57, 69, 81, 93, 105, 117],
                             'A#': [34, 46, 58, 70, 82, 94, 106, 118],
                             'B': [35, 47, 59, 71, 83, 95, 107, 119]}

    def octave_changed(self):
        '''Метод, позволяющий пользователю
        выбрать нужную октаву. Октавы от 1 до 8,
        из-за чего присвоение такое громоздкое'''
        self.octave = self.comboBox.currentText()
        keys = self.keyboard.buttons()
        for i in range(len(keys)):
            if self.octave < '7':
                if i <= 11:
                    if i < 5:
                        if i % 2 == 0:
                            keys[i].setText(keys[i].text()[0] + self.octave)
                        else:
                            keys[i].setText(keys[i].text()[0] +
                                            keys[i].text()[1] + self.octave)
                    else:
                        if i % 2 != 0:
                            keys[i].setText(keys[i].text()[0] + self.octave)
                        else:
                            keys[i].setText(keys[i].text()[0] +
                                            keys[i].text()[1] + self.octave)
                elif i <= 23:
                    if i < 17:
                        if i % 2 == 0:
                            keys[i].setText(keys[i].text()[0] +
                                            str(int(self.octave) + 1))
                        else:
                            keys[i].setText(
                                keys[i].text()[0] + keys[i].text()[1] + str(int(self.octave) + 1))
                    else:
                        if i % 2 != 0:
                            keys[i].setText(keys[i].text()[0] +
                                            str(int(self.octave) + 1))
                        else:
                            keys[i].setText(keys[i].text()[0] +
                                            keys[i].text()[1] + str(int(self.octave) + 1))
                elif i == 24:
                    keys[i].setText(keys[i].text()[0] +
                                    str(int(self.octave) + 2))
            else:
                if i <= 11:
                    if i < 5:
                        if i % 2 == 0:
                            keys[i].setText(keys[i].text()[0] + self.octave)
                        else:
                            keys[i].setText(keys[i].text()[0] +
                                            keys[i].text()[1] + self.octave)
                    else:
                        if i % 2 != 0:
                            keys[i].setText(keys[i].text()[0] + self.octave)
                        else:
                            keys[i].setText(keys[i].text()[0] +
                                            keys[i].text()[1] + self.octave)
                elif i <= 23:
                    if self.octave == '8':
                        if i < 17:
                            if i % 2 == 0:
                                keys[i].setText(
                                    keys[i].text()[0] + self.octave)
                            else:
                                keys[i].setText(keys[i].text()[0] +
                                                keys[i].text()[1] + self.octave)
                        else:
                            if i % 2 != 0:
                                keys[i].setText(
                                    keys[i].text()[0] + self.octave)
                            else:
                                keys[i].setText(keys[i].text()[0] +
                                                keys[i].text()[1] + self.octave)
                elif i == 24:
                    if self.octave == 7:
                        keys[i].setText(keys[i].text()[0] +
                                        str(int(self.octave) + 2))
                    else:
                        keys[-1].setText('C9')

    def duration_changed(self):
        '''Считывает с ползунка продолжительность ноты(в четвертях, от 1 до 120)'''
        self.durationLevel.setText(str(self.durationlSlider.value()))
        self.duration = self.durationlSlider.value()

    def volume_changed(self):
        '''Считывает с ползунка громкость одной ноты(от 1 до 126)'''
        self.volumeLevel.setText(str(self.volumeSlider.value()))
        self.volume = self.volumeSlider.value()

    def select_note(self, button):
        '''обрабатывает нажатие на "клавишу" пианино'''
        note = button.text()[:-1]
        octave = button.text()[-1]
        self.isSelected = True
        self.selected.setText(note + ', ' + octave + ', ' +
                              str(self.duration) + ', ' + str(self.volume))
        self.selected_note = (note, int(octave), self.duration, self.volume)

    def add_note(self):
        '''Добавляет ноту в будущую мелодию'''
        if self.isSelected:
            note = self.selected_note[0]
            octave = self.selected_note[1]
            self.mf.addNote(0, 0, self.note_numbers[note][octave - 1], self.time,
                            self.duration, self.volume)
            self.time += self.duration
        else:
            create_warning(
                'Сначала выберите октаву, ноту, громкость и длительность!')

    def play_melody(self):
        '''Самый интересный метод в этом классе.
        С помощью подпроцесса вызываем файл play_melody, который проиграет нам мелодию
        Я бы хотел реализовать
        '''
        old_melody = self.mf
        with open("output.mid", 'wb') as outf:
            self.mf.writeFile(outf)
        w = Worker(self.call_melody, 'play_melody', way='output.mid')
        self.threadpool.start(w)
        saving_or_not = create_question(
            'Сохранение',  "Сохранить трек или перезаписать его?(создать полностью заново)")
        if saving_or_not:
            save_path = QFileDialog.getSaveFileName(
                self, 'Сохранить мелодию', '', '.mid(*.mid)')[0]
            if save_path:
                with open(save_path, 'wb') as melody_file:
                    self.mf.writeFile(melody_file)
                if save_path.split('/')[-1] != 'output.mid':
                    os.remove('output.mid')
                add_playlist = create_question('Добавить в плейлист?',
                "Добавить мелодию в Ваш плейлист на вкладке 'создание музыки'?(при следующем запуске)")
                if add_playlist:
                    con = sqlite3.connect('project.db')
                    cur = con.cursor()
                    all_melodies = cur.execute(
                        'SELECT way_to_melody FROM melody_playlist').fetchall()
                    cur.execute('INSERT INTO melody_playlist VALUES(?, ?)',
                            (save_path.split('/')[-1].split('.')[0], save_path)).fetchall()
                    con.commit()
                    cur.close()
            else:
                create_warning('Выберите путь для сохранения!')
        else:
            edit_or_remove = create_question('Изменить', 'Удалить мелодию или дополнить её?')
            if edit_or_remove:
                self.mf = old_melody
            else:
                os.remove('output.mid')
                create_warning('''Файл для предварительной прослушки удалён.
                           Удачи в написании новой мелодии!''')
                self.mf = MIDIFile(1)

    def call_melody(self, file, way):
        subprocess.call(f'python {file}.py {way}')

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs['way']

    @pyqtSlot()
    def run(self):
        if self.args and self.kwargs:
            self.fn(*self.args, self.kwargs)
        else:
            self.fn()

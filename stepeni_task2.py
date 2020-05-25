#!/usr/bin/env python
# Version 1.1.0
# 05/2020

# Изменить путь к файлу логов
global path
path = '/home/kirill/python_work/log.txt'
from tkinter import *
from datetime import datetime

temp = 0
after_id = ''



def Root():
    root = Tk()
    root.title('Степень боевой готовности')
    root['bg'] = 'Gray'
    root.attributes('-zoomed', True)
    root.resizable(False, False)
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    
    def o_prog():
        prog = Tk()
        prog.title('О программе')
        prog['bg'] = 'Gainsboro'
        prog.geometry('600x350')
        prog.resizable(False, False)
        
        info = Label(prog,
                     text='''
                \"Степень боевой готовности\"
                
                Язык разработки:    Python 3.6
                Используемые модули и библиотеки:
                - tkinter
                - datetime

                Дата выхода:
                Version_1.0.0:     02. 2020 (Не исп)
                Version_1.1.0:     05. 2020

                Автор: @ivg97
                © 2020 Все права защищены
                     ''',
                     font='Cambria 14',
                     bg='Gainsboro',
                     foreground='Black'
                     )
        info.place(x=10, y=10)
        prog.mainloop()
    
    def help_prog():
        help = Tk()
        help.title('Справка')
        help['bg'] = 'Gainsboro'
        help.geometry('700x300')
        help.resizable(False, False)
        info = Label(help, text='''Информационная справка!(EXAMPLE)
        После запуска программы, открытия окна программы необходимо 
        запустить ее с помощью нажатия кнопки "Постоянная". \n
        Для правильной работы программы и записи соощений в файл о 
        включении одной из степеней боевой готовности необходимо   
        прописать путь к файлу записи в переменной "path" в файле   
        основного кода "stepeni_task2.py"
        ''',
        
                     font='Cambria 12',
                     bg='Gainsboro',
                     foreground='Black',
                     # width = 65,
                     # yustify = 'CENTER',
                     )
        info.place(x=1, y=5)
        help.mainloop()
    
    mainmenu.add_command(label='Справка', command=help_prog)
    mainmenu.add_command(label='О программе', command=o_prog)
    
    # Label
    astr_time = Label(root, text='Астрономическое время',
                      font='Cambria 50',
                      bg='Gray',
                      foreground='White'
                      )
    astr_time.place(x=50, y=50)
    
    oper_time = Label(root, text='Оперативное время',
                      font='Cambria 50',
                      bg='Gray',
                      foreground='White'
                      )
    oper_time.place(x=1100, y=50)
    
    # Data and time
    
    data = Label(root,
                 font='Cambria 30',
                 bg='Gray',
                 foreground='Blue'
                 )
    data.place(x=1450, y=5)
    time_asrt = Label(root,
                      font='Cambria 100',
                      bg='Gray',
                      foreground='Lime'
                      )
    time_asrt.place(x=150, y=150)


 
 
    #  Label степени
    # ========================================================================= #
    
    post_on = Label(root, text='Постоянная',
                    background='Blue',
                    foreground='OrangeRed',
                    font='Cambria 180',
                    )
    post_first = Label(root, text='          Отдел приведен        ',
                       background='Blue',
                       foreground='OrangeRed',
                       font='Cambria 80',
                       )
    
    povish_on = Label(root, text='Повышенная',
                      background='LimeGreen',
                      foreground='OrangeRed',
                      font='Cambria 180',
                      )
    povish_first = Label(root, text='          Отдел приведен            ',
                         background='LimeGreen',
                         foreground='OrangeRed',
                         font='Cambria 80',
                         )
    
    voen_opas_on = Label(root, text='Военная опасность',
                         background='Yellow',
                         foreground='OrangeRed',
                         font='Cambria 130',
                         )
    voen_opas_first = Label(root, text='            Отдел приведен             ',
                            background='Yellow',
                            foreground='OrangeRed',
                            font='Cambria 80',
                            )
    
    poln_on = Label(root, text='Полная',
                    background='Red',
                    foreground='Maroon',
                    font='Cambria 180',
                    )
    poln_BG_first = Label(root, text='          Отдел приведен         ',
                          background='Red',
                          foreground='Maroon',
                          font='Cambria 80',
                          )
    sec = Label(root, font='Cambria 100', text='00:00:00',
                background='Gray',
                foreground='Red')
    
    def oper_times():
        global temp, after_id
        after_id = root.after(1000, oper_times)
        f_temp = datetime.utcfromtimestamp(temp).strftime("%H:%M:%S")
        sec.configure(text=str(f_temp))
        temp += 1
    
    def reset_oper_time():
        global temp
        temp = 0
        sec.grid_forget()
    
    # logs write
    # ===================================================================== #
    '''Запись логов'''
    
    def file_Post():
        try:
            '''Запись лога ПОСТОЯННАЯ'''
            file = open(path, 'a')
            log_time_data = datetime.datetime.today()
            log_t_d = log_time_data.strftime(' %H:%M:%S | %d:%m:%Y ')
            log_print = 'App_Python: ' + log_t_d + ' # ON Postoyannay\n'
            file.write(str(log_print))
            file.close()
        except FileNotFoundError:
            error = Label(root,
                          text='Путь к файлу для записи '
                               'логов указан неверно',
                          foreground='Red',
                          font='Cambria 50'
                          )
            error.pack()
    
    def file_Pov():
        '''Запись лога ПОВЫШЕННАЯ'''
        try:
            file = open(path, 'a')
            log_time_data = datetime.datetime.today()
            log_t_d = log_time_data.strftime(' %H:%M:%S | %d:%m:%Y ')
            log_print = 'App_Python: ' + log_t_d + ' # ON Povishennay\n'
            file.write(str(log_print))
            file.close()
        except FileNotFoundError:
            error = Label(root,
                          text='Путь к файлу для записи '
                               'логов указан неверно',
                          foreground='Red',
                          font='Cambria 50'
                          )
            error.pack()
    
    def file_VO():
        '''Запись лога ВОЕННАЯ ОПАСНОСТЬ'''
        try:
            file = open(path, 'a')
            log_time_data = datetime.datetime.today()
            log_t_d = log_time_data.strftime(' %H:%M:%S | %d:%m:%Y ')
            log_print = 'App_Python: ' + log_t_d + ' # ON Voennay Opasnost\n'
            file.write(str(log_print))
            file.close()
        except FileNotFoundError:
            error = Label(root,
                          text='Путь к файлу для записи '
                               'логов указан неверно',
                          foreground='Red',
                          font='Cambria 50'
                          )
            error.pack()
    
    def file_P_BG():
        '''Запись лога ПОЛНАЯ'''
        try:
            file = open(path, 'a')
            log_time_data = datetime.datetime.today()
            log_t_d = log_time_data.strftime(' %H:%M:%S | %d:%m:%Y ')
            log_print = 'App_Python: ' + log_t_d + ' # ON Polnay BG\n'
            file.write(str(log_print))
            file.close()
        except FileNotFoundError:
            error = Label(root,
                          text='Путь к файлу для записи '
                               'логов указан неверно',
                          foreground='Red',
                          font='Cambria 50'
                          )
            error.pack()


   
    
    # функции включения и отключения степеней
    # ========================================================================== #
 
 
    def post_ON():
        '''Включает постоянную степень готовности'''
        post_on.place(x=140, y=620)
        post_first.place(x=142, y=470)
        sec.place(x=1150, y=150)
        reset_oper_time()
        file_Post()
        povish_on.place_forget()
        povish_first.place_forget()
        voen_opas_on.place_forget()
        voen_opas_first.place_forget()
        poln_on.place_forget()
        poln_BG_first.place_forget()
    
    def povish_ON():
        '''Включает повышенную степень готовности'''
        povish_on.place(x=90, y=620)
        povish_first.place(x=90, y=470)
        file_Pov()
        post_on.place_forget()
        post_first.place_forget()
        # sec.place_forget()
        oper_times()
        voen_opas_on.place_forget()
        voen_opas_first.place_forget()
        poln_on.place_forget()
        poln_BG_first.place_forget()
    
    def voen_op_ON():
        '''Включает военную опасность'''
        voen_opas_on.place(x=30, y=620)
        voen_opas_first.place(x=32, y=470)
        file_VO()
        post_on.place_forget()
        post_first.place_forget()
        sec.place_forget()
        povish_on.place_forget()
        povish_first.place_forget()
        poln_on.place_forget()
        poln_BG_first.place_forget()
    
    def poln_ON():
        '''Включает полную БГ'''
        poln_on.place(x=450, y=620)
        poln_BG_first.place(x=110, y=470)
        file_P_BG()
        post_on.place_forget()
        post_first.place_forget()
        sec.place_forget()
        povish_on.place_forget()
        povish_first.place_forget()
        voen_opas_on.place_forget()
        voen_opas_first.place_forget()
        
        # Button for select_stepen
        '''Кнопки для выбора степени в окне выбора'''
    
    postoyannaya = Button(root,
                          text='Постоянная',
                          font='Cambria 14',
                          bg='Gainsboro',
                          foreground='Black',
                          command=post_ON
                          )
    postoyannaya.place(x=10, y=950)
    
    povishennay = Button(root,
                         text='Повышенная',
                         font='Cambria 14',
                         bg='Gainsboro',
                         foreground='Black',
                         command=povish_ON
                         )
    povishennay.place(x=160, y=950)
    
    voen_opasn = Button(root,
                        text='Военая опасность',
                        font='Cambria 14',
                        bg='Gainsboro',
                        foreground='Black',
                        command=voen_op_ON
                        )
    voen_opasn.place(x=320, y=950)
    
    polnay = Button(root,
                    text='Полная',
                    font='Cambria 14',
                    bg='Gainsboro',
                    foreground='Black',
                    command=poln_ON
                    )
    polnay.place(x=527, y=950)

 
 
    
    def clock():
        '''Вывод даты и астрономического времени '''
        data_p = datetime.datetime.now().strftime("%B   %x")
        time_p = datetime.datetime.now().strftime(" %H:%M:%S ")
        data.config(text=data_p)
        time_asrt.config(text=time_p)
        
        root.after(1000, clock)
    
    clock()
    
    # Button
    stepen = Label(root, text='Степень боевой готовности:',
                   font='Cambria 50',
                   bg='Gray',
                   foreground='White',
                   )
    stepen.place(x=450, y=350)
    
    root.mainloop()




Root()

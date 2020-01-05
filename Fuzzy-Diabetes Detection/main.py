#! /usr/bin/env python

import sys
import matlab.engine
eng = matlab.engine.start_matlab()

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import matlab.engine
import main_support
from PIL import Image, ImageTk
import threading

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family Arial -size 19 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family Arial -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family Arial -size 15 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font15 = "-family Arial -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("968x493+919+245")
        top.title("Diabetes Detection Fuzzy System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#b9b9b9")
        top.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.01, rely=0.02, relheight=0.94, relwidth=0.48)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=465)

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.3, rely=0.04, height=32, width=350)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font11)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Enter Patient's data ''')

#----------------------------pregnant times----------------------------------
        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.02, rely=0.15, height=39, width=120)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font12)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Pregnant Times''')

        self.TEntry_Preg = ttk.Entry(self.TFrame1)
        self.TEntry_Preg.place(relx=0.24, rely=0.17, relheight=0.05
                , relwidth=0.53)
        self.TEntry_Preg.configure(width=246)
        self.TEntry_Preg.configure(takefocus="")
        self.TEntry_Preg.configure(cursor="ibeam")

#-----------------------------------plas----------------------------------------
        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.02, rely=0.24, height=39, width=120)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=font12)
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Plasma Glucose Level''')

        self.TEntry_Plas = ttk.Entry(self.TFrame1)
        self.TEntry_Plas.place(relx=0.24, rely=0.26, relheight=0.05
                , relwidth=0.53)
        self.TEntry_Plas.configure(width=246)
        self.TEntry_Plas.configure(takefocus="")
        self.TEntry_Plas.configure(cursor="ibeam")

#---------------------------------Diastolic bp-------------------------------

        self.TLabel4 = ttk.Label(self.TFrame1)
        self.TLabel4.place(relx=0.02, rely=0.33, height=39, width=120)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font=font12)
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Diastolic BP''')

        self.TEntry_Dias = ttk.Entry(self.TFrame1)
        self.TEntry_Dias.place(relx=0.24, rely=0.35, relheight=0.05
                , relwidth=0.53)
        self.TEntry_Dias.configure(width=246)
        self.TEntry_Dias.configure(takefocus="")
        self.TEntry_Dias.configure(cursor="ibeam")

#----------------------------------------Tric----------------------------------

        self.TLabel5 = ttk.Label(self.TFrame1)
        self.TLabel5.place(relx=0.02, rely=0.41, height=39, width=120)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font=font12)
        self.TLabel5.configure(relief=FLAT)
        self.TLabel5.configure(text='''Skin thickness''')

        self.TEntry_Tric = ttk.Entry(self.TFrame1)
        self.TEntry_Tric.place(relx=0.24, rely=0.43, relheight=0.05
                , relwidth=0.53)
        self.TEntry_Tric.configure(width=246)
        self.TEntry_Tric.configure(takefocus="")
        self.TEntry_Tric.configure(cursor="ibeam")

#-----------------------------Insulin-----------------------------------------

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.02, rely=0.5, height=39, width=120)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font12)
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Serum insulin''')

        self.TEntry_Ins = ttk.Entry(self.TFrame1)
        self.TEntry_Ins.place(relx=0.24, rely=0.52, relheight=0.05
                , relwidth=0.53)
        self.TEntry_Ins.configure(width=246)
        self.TEntry_Ins.configure(takefocus="")
        self.TEntry_Ins.configure(cursor="ibeam")

#-----------------------------BMI Value--------------------------------------

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.02, rely=0.61, height=39, width=120)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font12)
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''BMI Value''')

        self.TEntry_bmi = ttk.Entry(self.TFrame1)
        self.TEntry_bmi.place(relx=0.24, rely=0.63, relheight=0.05
                , relwidth=0.53)
        self.TEntry_bmi.configure(width=246)
        self.TEntry_bmi.configure(takefocus="")
        self.TEntry_bmi.configure(cursor="ibeam")

#-----------------------------Pedigree------------------------------------

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.02, rely=0.70, height=39, width=120)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font12)
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Pedigree''')

        self.TEntry_Pedigree = ttk.Entry(self.TFrame1)
        self.TEntry_Pedigree.place(relx=0.24, rely=0.72, relheight=0.05
                              , relwidth=0.53)
        self.TEntry_Pedigree.configure(width=246)
        self.TEntry_Pedigree.configure(takefocus="")
        self.TEntry_Pedigree.configure(cursor="ibeam")

#-----------------------------Age-----------------------------------------

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.02, rely=0.79, height=39, width=120)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font12)
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Age''')

        self.TEntry_Age = ttk.Entry(self.TFrame1)
        self.TEntry_Age.place(relx=0.24, rely=0.81, relheight=0.05
                              , relwidth=0.53)
        self.TEntry_Age.configure(width=246)
        self.TEntry_Age.configure(takefocus="")
        self.TEntry_Age.configure(cursor="ibeam")
# -----------------------------------------------------------------------

        self.TButton_eval = ttk.Button(self.TFrame1)
        self.TButton_eval.place(relx=0.34, rely=0.93, height=35, width=126)
        self.TButton_eval.configure(takefocus="")
        self.TButton_eval.configure(text='''Evaluate''')
        self.TButton_eval.bind('<Button-1>',lambda e:main_support.TButton_eval_onClick(e))


        self.TLabel_Indicator = ttk.Label(self.TFrame1)
        self.TLabel_Indicator.place(relx=0.29, rely=0.88, height=19, width=184)
        self.TLabel_Indicator.configure(background="#d9d9d9")
        self.TLabel_Indicator.configure(foreground="#000000")
        self.TLabel_Indicator.configure(relief=FLAT)
        self.TLabel_Indicator.configure(anchor=CENTER)

        self.TLabel7 = ttk.Label(self.TFrame1)
        self.TLabel7.place(relx=0.8, rely=0.18, height=19, width=36)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font=font15)
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(anchor=W)
        self.TLabel7.configure(text='''0-17''')
        self.TLabel7.configure(width=36)

        self.TLabel8 = ttk.Label(self.TFrame1)
        self.TLabel8.place(relx=0.8, rely=0.26, height=19, width=46)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font=font15)
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(anchor=W)
        self.TLabel8.configure(text='''0-199''')
        self.TLabel8.configure(width=46)

        self.TLabel9 = ttk.Label(self.TFrame1)
        self.TLabel9.place(relx=0.8, rely=0.35, height=19, width=66)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font=font15)
        self.TLabel9.configure(relief=FLAT)
        self.TLabel9.configure(anchor=W)
        self.TLabel9.configure(text='''0-122''')
        self.TLabel9.configure(width=66)

        self.TLabel11 = ttk.Label(self.TFrame1)
        self.TLabel11.place(relx=0.8, rely=0.43, height=19, width=76)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font=font15)
        self.TLabel11.configure(relief=FLAT)
        self.TLabel11.configure(anchor=W)
        self.TLabel11.configure(text='''0 - 99''')
        self.TLabel11.configure(width=76)

        self.TLabel10 = ttk.Label(self.TFrame1)
        self.TLabel10.place(relx=0.8, rely=0.52, height=19, width=56)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font15)
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(anchor=W)
        self.TLabel10.configure(text='''0-846''')
        self.TLabel10.configure(width=56)

        self.TLabel10 = ttk.Label(self.TFrame1)
        self.TLabel10.place(relx=0.8, rely=0.63, height=19, width=56)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font15)
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(anchor=W)
        self.TLabel10.configure(text='''0-67''')
        self.TLabel10.configure(width=56)

        self.TLabel10 = ttk.Label(self.TFrame1)
        self.TLabel10.place(relx=0.8, rely=0.72, height=19, width=56)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font15)
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(anchor=W)
        self.TLabel10.configure(text='''0-2.42''')
        self.TLabel10.configure(width=56)


        self.TLabel10 = ttk.Label(self.TFrame1)
        self.TLabel10.place(relx=0.8, rely=0.82, height=19, width=56)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font15)
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(anchor=W)
        self.TLabel10.configure(text='''21-81''')
        self.TLabel10.configure(width=56)

        self.TLabel_Output = ttk.Label(top)
        self.TLabel_Output.place(relx=0.52, rely=0.06, height=29, width=436)
        self.TLabel_Output.configure(background="#d9d9d9")
        self.TLabel_Output.configure(foreground="#000000")
        self.TLabel_Output.configure(font=font11)
        self.TLabel_Output.configure(relief=FLAT)
        self.TLabel_Output.configure(anchor=CENTER)
        self.TLabel_Output.configure(text='''Diabetes Stage :''')
        self.TLabel_Output.configure(width=436)

        self.Canvas_Graph = Canvas(top)
        self.Canvas_Graph.place(relx=0.51, rely=0.16, relheight=0.66
                , relwidth=0.47)
        self.Canvas_Graph.configure(background="white")
        self.Canvas_Graph.configure(borderwidth="2")
        self.Canvas_Graph.configure(highlightbackground="#e0ded1")
        self.Canvas_Graph.configure(highlightcolor="black")
        self.Canvas_Graph.configure(insertbackground="black")
        self.Canvas_Graph.configure(relief=RIDGE)
        self.Canvas_Graph.configure(selectbackground="#cac8bc")
        self.Canvas_Graph.configure(selectforeground="black")
        self.Canvas_Graph.configure(width=456)

        self.TLabel_OutputText = ttk.Label(top)
        self.TLabel_OutputText.place(relx=0.52, rely=0.87, height=29, width=500)
        self.TLabel_OutputText.configure(background="#d9d9d9")
        self.TLabel_OutputText.configure(foreground="#000000")
        self.TLabel_OutputText.configure(font=font14)
        self.TLabel_OutputText.configure(relief=FLAT)
        self.TLabel_OutputText.configure(anchor=CENTER)
        self.TLabel_OutputText.configure(width=500)

        widgets = [self.TEntry_Preg, self.TEntry_Plas, self.TEntry_Dias, self.TEntry_Tric, self.TEntry_Ins, self.TEntry_bmi,self.TEntry_Pedigree,self.TEntry_Age]
        self.TButton_eval.bind('<Button-1>',lambda e:self.TButton_eval_onClick(e, widgets))

        self.TEntry_Preg.insert(END, '7')
        self.TEntry_Plas.insert(END, '140')
        self.TEntry_Dias.insert(END, '80')
        self.TEntry_Tric.insert(END, '50')
        self.TEntry_Ins.insert(END, '500')
        self.TEntry_bmi.insert(END, '40')
        self.TEntry_Pedigree.insert(END, '1.40')
        self.TEntry_Age.insert(END, '50')

        # start matlab engine
        self.matlabeng = matlab.engine.start_matlab()


    def TButton_eval_onClick(self, p1, widgets):

        self.TLabel_Indicator['text'] = "Processing from MATLAB..."
        self.TButton_eval.state(['disabled'])

        # run in multithread so our UI won't freeze
        args = [float(x.get()) for x in widgets]
        t = threading.Thread(target=self.doMATLABProcessing, args=[args])
        t.daemon = True
        t.start()

    def doMATLABProcessing(self, data):

        # contacting MATLAB using its API
        val = self.matlabeng.evalFuzzy(*data, nargout=1)
        self.matlabeng.createOutputGraph(val, nargout=0)
        self.tk_img = ImageTk.PhotoImage(file='output.jpg')

        # displaying MATLAB output to the interface
        self.Canvas_Graph.create_image(250, 150, image=self.tk_img)
        self.TLabel_Output['text'] = "Output : %.5f" % val
        self.TLabel_Indicator['text'] = "Done!"
        self.outputOutputMsg(val)

        # enable the button back
        self.TButton_eval.state(['!disabled'])

    def outputOutputMsg(self, val):
        cond = []
        if val >= 0.1 and val <= 0.9: cond += ['medium']
        if val >= 0 and val <= 0.4: cond += ['dangerous']
        if val >= 0.6 and val <= 1.0: cond += ['safe']
        if len(cond) == 1:
            if val <= 0.1:
                self.TLabel_OutputText['text'] = "You're in Dangerous stage of Diabetes.".format(*cond)
            if val >= 0.4 and val <= 0.6:
                self.TLabel_OutputText['text'] = "You're in Medium stage of Diabetes.".format(*cond)
            if val >= 0.7:
                self.TLabel_OutputText['text'] = "You're in Safe stage of Diabetes.".format(*cond)

        else:
            if val >= 0.1 and val <= 0.4:
                self.TLabel_OutputText['text'] = "You're in Medium and Dangerous stage of Diabetes.".format(*cond)
            if val >= 0.6 and val <= 0.7:
                self.TLabel_OutputText['text'] = "You're in Medium and Safe stage of Diabetes.".format(*cond)


if __name__ == '__main__':
    vp_start_gui()




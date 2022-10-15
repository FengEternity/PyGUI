from tkinter import *
from tkinter import ttk, filedialog, messagebox # 实现打开文件、保存文件的操作

'''
GUI 设计的一般流程：
    1.创建一个窗体
    2.把需要的控件放到窗体上，并告诉它们当有预期的事件发生时就执行预设的动作
    3.启动循环监听事件
'''

'''
root = Tk() # 1. 创建一个窗体
Label(root, text='Hello World').pack() # 2. 添加Label控件
root.mainloop() # 3. 启动循环监听事件
'''
'''
from tkinter import *

root = Tk()
root.title('最简单的桌面应用程序') # 设置窗口标题
root.geometry('480x200') # 设置窗口大小
# root.iconbitmap('res/Tk.ico') # 设置窗口图标 # 需使用本地文件自定义

label = Label(root, text='Hello World', font=("Arial Bold", 50))
label.pack(side='top', expand='yes', fill='both') # 使用全部可用空间，水平和垂直两个方向填充
btn = Button(root, text='关闭窗口', bg='#C0C0C0') # 按钮背景深灰色
btn.pack(side='top', fill='x', padx=5, pady=5) # 水平方向填充，水平垂直两个方向留白5个像素

root.mainloop()
'''

# 事件函数
'''
from tkinter import *

def click_button():
    """点击按钮的事件函数"""
    
    root.destroy() # 调用root的析构函数

root = Tk()
root.title('最简单的桌面应用程序')
root.geometry('640x320')
# root.iconbitmap('res/Tk.ico')

label = Label(root, text='Hello World', font=("Arial Bold", 50))
label.pack(side='top', expand='yes', fill='both')
btn = Button(root, text='关闭窗口', bg='#C0C0C0', command=click_button) # 用command参数绑定事件函数
btn.pack(side='top', fill='x', padx=5, pady=5)

root.mainloop()
'''

# 面向对象使用Tkinter
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('按钮点击计数器')
        self.geometry('320x160')
        # self.iconbitmap('res/Tk.ico')
        
        self.counter = IntVar() # 创建一个整型变量对象
        self.counter.set(0) # 置其初值为0
        
        label = Label(self, textvariable=self.counter, font=("Arial Bold", 50)) # 将Label和整型变量对象关联
        label.pack(side='left', expand='yes', fill='both', padx=5, pady=5)
        
        btn = Button(self, text='点我试试看', bg='#90F0F0')
        btn.pack(side='right', anchor='center', fill='y', padx=5, pady=5)
        
        btn.bind(sequence='<Button-1>', func=self.on_button) # 绑定事件和事件函数
    
    def on_button(self, evt):
        """点击按钮事件的响应函数, evt是事件对象"""
        
        self.counter.set(self.counter.get()+1)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

'''
Tkinter支持的鼠标事件如下所列:

<Return> - 回车
<Cancel> - Break键
<BackSpace> - BackSpace键
<Tab> - Tab键
<Shift_L> - Shift键
<Alt_R> - Alt键
<Control_L> - Control键
<Pause> - Pause键
<Caps_Lock> - Caps_Lock键
<Escape> - Escapel键
<Prior> - PageUp键
<Next> - PageDown键
<End> - End键
<Home> - Home键
<Left> - 左箭头
<Up> - 上箭头
<Right> - 右箭头
<Down> - 下箭头
<Print> - Print Screen键
<Insert> - Insert键
<Delete> - Delete键
<F1> - F1键
<Num_Lock> - Num_Lock键
<Scroll_Lock> - Scroll_Lock键
<Key> - 任意键
'''
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('键盘事件演示程序')
        self.geometry('480x200')
        # self.iconbitmap('res/Tk.ico')
        
        self.info = StringVar()
        self.info.set('')

        self.info = StringVar()
        self.info.set('')

        self.lab = Label(self, textvariable=self.info, font=("Arial Bold", 18))
        self.lab.pack(side='top', expand='yes', fill='both')
        self.lab.focus_set()
        self.lab.bind('<Key>', self.on_key)
        
        self.btn = Button(self, text='切换焦点', bg='#C0C0C0', command=self.set_label_focus)
        self.btn.pack(side='top', fill='x', padx=5, pady=5)
    
    def on_key(self, evt):
        """响应所有键盘事件的函数"""
        
        self.info.set('evt.char = %s\nevt.keycode = %s\nevt.keysym = %s'%(evt.char, evt.keycode, evt.keysym))
    
    def set_label_focus(self):
        """在Label和Button之间切换焦点"""
            
        self.info.set('')
        
        if isinstance(self.lab.focus_get(), Label):
            self.btn.focus_set()
        else:
            self.lab.focus_set()

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 窗格 Frame
'''
from tkinter import *

def befor_quit(evt):
    """关闭之前清理现场"""
    
    print('关闭之前，可以做点什么')

root = Tk()
Label(root, text='Hello World').pack()

root.bind('<Destroy>', befor_quit)

root.mainloop()
'''
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('窗格：Frame')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        frame1 = Frame(self, bg='#90c0c0') 
        frame1.pack(padx=5, pady=5)

        # Label是frame1的第1个子控件，从左向右布局
        Label(frame1, bg='#f0f0f0', width=25).pack(side=LEFT, fill=BOTH, padx=5, pady=5)

        # frame2是frame1的第2个子控件，从左向右布局
        frame2 = Frame(frame1, bg='#f0f0f0')
        frame2.pack(side=LEFT, padx=5, pady=5)

        # 3个Button是frame2的子控件，自上而下布局
        Button(frame2, text='按钮1', width=10).pack(padx=5, pady=5)
        Button(frame2, text='按钮2', width=10).pack(padx=5, pady=5)
        Button(frame2, text='按钮3', width=10).pack(padx=5, pady=5)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''


# 输入框
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('输入框：Entry')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        account, passwd = StringVar(), StringVar()
        account.set('')
        passwd.set('')

        group = LabelFrame(self, text="登录", padx=5, pady=5)
        group.pack(padx=20, pady=10)

        f1 = Frame(group)
        f1.pack(padx=5, pady=5)
        Label(f1, text='账号：').pack(side=LEFT, pady=5)
        Entry(f1, textvariable=account, width=15, justify=CENTER).pack(side=LEFT, pady=5)

        f2 = Frame(group)
        f2.pack(padx=5, pady=5) 
        Label(f2, text='密码：').pack(side=LEFT, pady=5)
        Entry(f2, textvariable=passwd, width=15, show='*', justify=CENTER).pack(side=LEFT, pady=5)

        btn = Button(self, text='确定', bg='#90c0c0', command=lambda : print(account.get(), passwd.get()))
        btn.pack(fill=X, padx=20, pady=10)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 单选框
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('单选框：Radiobutton')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        f0 = Frame(self)
        f0.pack(padx=5, pady=5)
         
        f1 = Frame(f0) 
        f1.pack(side=LEFT, padx=5, pady=5)

        g1 = LabelFrame(f1, text="你最擅长哪一个？", padx=5, pady=5)
        g1.pack(padx=5, pady=5)

        self.rb_v1 = IntVar()
        self.rb_v1.set(0)
        rb_11 = Radiobutton(g1, variable=self.rb_v1, text='Tkinter', value=0, command=self.on_radio_1)
        rb_12 = Radiobutton(g1, variable=self.rb_v1, text='wxPython', value=1, command=self.on_radio_1)
        rb_13 = Radiobutton(g1, variable=self.rb_v1, text='PyQt5', value=2, command=self.on_radio_1)
        rb_11.pack(ancho='w', padx=5, pady=5)
        rb_12.pack(ancho='w', padx=5, pady=5)
        rb_13.pack(ancho='w', padx=5, pady=5)

        f2 = Frame(f0) 
        f2.pack(side=LEFT, padx=5, pady=5)

        g2 = LabelFrame(f2, text="你最擅长哪一个？", padx=5, pady=5)
        g2.pack(padx=5, pady=5)

        self.rb_v2 = IntVar()
        self.rb_v2.set(0)
        rb_21 = Radiobutton(g2, variable=self.rb_v2, text='Tkinter', value=0, indicatoron=False, command=self.on_radio_2)
        rb_22 = Radiobutton(g2, variable=self.rb_v2, text='wxPython', value=1, indicatoron=False, command=self.on_radio_2)
        rb_23 = Radiobutton(g2, variable=self.rb_v2, text='PyQt5', value=2, indicatoron=False, command=self.on_radio_2)
        rb_21.pack(fill=X, padx=5, pady=5)
        rb_22.pack(fill=X, padx=5, pady=5)
        rb_23.pack(fill=X, padx=5, pady=5)

        self.info = StringVar()
        self.info.set('')
        label = Label(self, textvariable=self.info, bg='#ffffff')
        label.pack(expand='yes', fill='x', padx=5, pady=10)
    
    def on_radio_1(self):
        """响应第1组单选框事件的函数"""
        
        selected = ['Tkinter', 'wxPython', 'PyQt5'][self.rb_v1.get()]
        self.info.set('你选择了第1组的%s'%selected)

    def on_radio_2(self):
        """响应第2组单选框事件的函数"""
        
        selected = ['Tkinter', 'wxPython', 'PyQt5'][self.rb_v2.get()]
        self.info.set('你选择了第2组的%s'%selected)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 复选框
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('复选框：Checkbox')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        group = LabelFrame(self, text="你擅长哪个？", padx=20, pady=5)
        group.pack(padx=30, pady=5)

        self.cb_v1 = IntVar()
        self.cb_v2 = IntVar()
        self.cb_v3 = IntVar()
        self.cb_v1.set(0)
        self.cb_v2.set(0)
        self.cb_v3.set(0)

        cb_1 = Checkbutton(group, variable=self.cb_v1, text='Tkinter', onvalue=1, offvalue=0, command=self.on_cb).pack(ancho='w', padx=5, pady=5)
        cb_2 = Checkbutton(group, variable=self.cb_v2, text='wxPython', onvalue=1, offvalue=0, command=self.on_cb).pack(ancho='w', padx=5, pady=5)
        cb_3 = Checkbutton(group, variable=self.cb_v3, text='PyQt5', onvalue=1, offvalue=0, command=self.on_cb).pack(ancho='w', padx=5, pady=5)

        self.info = StringVar()
        self.info.set('')
        label = Label(self, textvariable=self.info, bg='#ffffff')
        label.pack(expand='yes', fill='x', padx=5, pady=5)
    
    def on_cb(self):
        """响应复选框事件的函数"""
        
        selected = list()
        if self.cb_v1.get():
           selected.append('Tkinter') 
        if self.cb_v2.get():
           selected.append('wxPython') 
        if self.cb_v3.get():
           selected.append('PyQt5') 
        
        self.info.set(', '.join(selected))

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 计数器
'''
from tkinter import *

def on_spin():
    """响应可调输入框事件的函数"""
    
    info.set(str(spin_v.get()))

root = Tk()
root.title('可调输入框：Spinbox')

spin_v = IntVar()
spin_v.set(5)
entry = Spinbox(root, textvariable=spin_v, from_=0, to=9, bg='#ffffff', command=on_spin).pack(fill=X, padx=5, pady=5)

info = StringVar()
info.set(str(spin_v.get()))
label = Label(root, textvariable=info, bg='#ffffff')
label.pack(expand=YES, fill=X, padx=5, pady=5)

root.mainloop()
'''

# 滑块
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('滑块：Scale')
        self.geometry('240x100')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        self.scale_v = DoubleVar()
        self.scale_v.set(50)
        scale = Scale(self, variable=self.scale_v, from_=0, to=100, orient=HORIZONTAL, command=self.on_scale)
        scale.pack(fill=X, padx=5, pady=5)

        self.info = StringVar()
        self.info.set(str(self.scale_v.get()))
        label = Label(self, textvariable=self.info, bg='#ffffff')
        label.pack(expand=YES, fill=X, padx=5, pady=5)
    
    def on_scale(self, evt):
        """响应滑块事件的函数"""
        
        self.info.set(str(self.scale_v.get()))

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 菜单
'''
class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('菜单按钮：Menubutton')
        self.geometry('300x100')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        frame_menu = Frame(self)
        frame_menu.pack(anchor=NW) # 菜单位于窗口左上角（North_West）

        mb_file = Menubutton(frame_menu, text='文件', relief=RAISED)
        mb_file.pack(side='left')
        file_menu = Menu(mb_file, tearoff=False)
        file_menu.add_command(label='打开', command=lambda :print('打开文件'))
        file_menu.add_command(label='保存', command=lambda :print('保存文件'))
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=self.destroy)
        mb_file.config(menu=file_menu)

        mb_help = Menubutton(frame_menu, text='帮助', relief=RAISED)
        mb_help.pack(side='left')
        help_menu = Menu(mb_help, tearoff=False)
        help_menu.add_command(label='关于...', command=lambda :print('帮助文档'))
        mb_help.config(menu=help_menu)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''   

# 消息对话框
'''
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title('消息对话框')

info = StringVar()
info.set('')

f = Frame(root)
f.pack(padx=5, pady=10)

Button(f, text='提示信息', command=lambda :info.set(mb.showinfo(title='提示信息', message='对手认负，比赛结束。'))).pack(side=LEFT, padx=5)
Button(f, text='警告信息', command=lambda :info.set(mb.showwarning(title='警告信息', message='不能连续提和！'))).pack(side=LEFT, padx=5)
Button(f, text='错误信息', command=lambda :info.set(mb.showerror(title='错误信息', message='着法错误！'))).pack(side=LEFT, padx=5)
Button(f, text='Yes/No', command=lambda :info.set(mb.askyesno(title='操作提示', message='对手提和，接受吗？'))).pack(side=LEFT, padx=5)
Button(f, text='Ok/Cancel', command=lambda :info.set(mb.askokcancel(title='操作提示', message='再来一局？'))).pack(side=LEFT, padx=5)
Button(f, text='Retry/Cancel', command=lambda :info.set(mb.askretrycancel(title='操作提示', message='消息发送失败！'))).pack(side=LEFT, padx=5)
Button(f, text='Yes/No/Cancel', command=lambda :info.set(mb.askyesnocancel(title='操作提示', message='是否保存对局记录？'))).pack(side=LEFT, padx=5)

label = Label(root, textvariable=info, bg='#ffffff')
label.pack(expand='yes', fill='x', padx=5, pady=20)

root.mainloop()
'''

# 文件对话框
'''
from tkinter import *
from tkinter import filedialog as fd

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('文件对话框')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        info = StringVar()
        info.set('')

        f = Frame(self)
        f.pack(padx=20, pady=10)

        Button(f, text='选择文件', command=lambda :info.set(fd.askopenfilename(title='选择文件'))).pack(side=LEFT, padx=10)
        Button(f, text='选择目录', command=lambda :info.set(fd.askdirectory(title='选择目录'))).pack(side=LEFT, padx=10)
        Button(f, text='保存文件', command=lambda :info.set(fd.asksaveasfilename(title='保存文件', defaultextension='.png'))).pack(side=LEFT, padx=10)

        label = Label(self, textvariable=info, bg='#ffffff')
        label.pack(expand='yes', fill='x', padx=5, pady=20)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 主题选择
'''
from tkinter import *
from tkinter import ttk

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('主题控件')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        self.style = ttk.Style()
        
        self.theme = StringVar() 
        self.theme.set(self.style.theme_use())
        
        ttk.Button(self, text='切换主题按钮', command=self.on_style).pack(padx=30, pady=20)
        ttk.Entry(self, textvariable=self.theme, justify=CENTER, width=20).pack(padx=30, pady=0)
        ttk.Combobox(self, value=('Tkinter', 'wxPython', 'PyQt5')).pack(padx=30, pady=20)
    
    def on_style(self):
        """更换主题"""
        
        items = self.style.theme_names()
        new_theme = items[(items.index(self.theme.get())+1)%len(items)]
        self.theme.set(new_theme)
        self.style.theme_use(new_theme)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 窗口居中
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('窗口居中')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
        self.center()
    
    def init_ui(self):
        """初始化界面"""
        
        Label(self, text='Hello World', font=("Arial Bold", 50)).pack(expand=YES, fill='both')
    
    def center(self):
        """窗口居中"""
        
        self.update() # 更新显示以获取最新的窗口尺寸
        scr_w = self.winfo_screenwidth() # 获取屏幕宽度
        scr_h = self.winfo_screenheight() # 获取屏幕宽度
        w = self.winfo_width() # 窗口宽度
        h = self.winfo_height() # 窗口高度
        x = (scr_w-w)//2 # 窗口左上角x坐标
        y = (scr_h-h)//2 # 窗口左上角y坐标

        self.geometry('%dx%d+%d+%d'%(w,h,x,y)) # 设置窗口大小和位置

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 图库
'''
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('相册')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
        self.center()
    
    def init_ui(self):
        """初始化界面"""
        
        self.curr = 0
        self.photos = ('DSC00485.jpg', 'DSC00450.jpg', 'DJI_0106.jpg') # 图像显示有问题，应该是图片的像素与代码中设计的像素相冲突
        self.img = ImageTk.PhotoImage(Image.open(self.photos[self.curr]))

        self.album = Label(self, image=self.img)
        self.album.pack(expand=YES, fill='both', padx=5, pady=5)

        f = Frame(self)
        f.pack(padx=10, pady=20)

        style = ttk.Style()
        style.theme_use('vista')

        ttk.Button(f, text='<', width=10, command=self.on_prev).pack(side=LEFT, padx=10)
        ttk.Button(f, text='>', width=10, command=self.on_next).pack(side=LEFT, padx=10)
    
    def center(self):
        """窗口居中"""
        
        self.update() # 更新显示以获取最新的窗口尺寸
        scr_w = self.winfo_screenwidth() # 获取屏幕宽度
        scr_h = self.winfo_screenheight() # 获取屏幕宽度
        w = self.winfo_width() # 窗口宽度
        h = self.winfo_height() # 窗口高度
        x = (scr_w-w)//2 # 窗口左上角x坐标
        y = (scr_h-h)//2 # 窗口左上角y坐标

        self.geometry('%dx%d+%d+%d'%(w,h,x,y)) # 设置窗口大小和位置
    
    def on_prev(self):
        """前一张照片"""
        
        self.curr = (self.curr-1)%3
        img = ImageTk.PhotoImage(Image.open(self.photos[self.curr]))
        self.album.configure(image=img)
        self.album.image = img

    def on_next(self):
        """后一张照片"""
        
        self.curr = (self.curr+1)%3
        img = ImageTk.PhotoImage(Image.open(self.photos[self.curr]))
        self.album.configure(image=img)
        self.album.image = img

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 计算机
'''
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('计算器')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
        self.center()
    
    def init_ui(self):
        """初始化界面"""
        
        self.screen = StringVar()
        self.screen.set('')
        Label(self, textvariable=self.screen, anchor=E, bg='#000030', fg='#30ff30', font=("Arial Bold", 16)).pack(fill=X, padx=10, pady=10)

        keys = [
            ['(', ')', 'Back', 'Clear'],
            ['7',  '8',  '9',  '/'], 
            ['4',  '5',  '6',  '*'], 
            ['1',  '2',  '3',  '-'], 
            ['0',  '.',  '=',  '+']
        ]

        f = Frame(self)
        f.pack(padx=10, pady=10)

        for i in range(5):
            for j in range(4):
                if i == 0 or j == 3:
                    Button(f, text=keys[i][j], width=8, bg='#f0e0d0', fg='red').grid(row=i, column=j, padx=3, pady=3)
                elif i == 4 and j == 2:
                    Button(f, text=keys[i][j], width=8, bg='#f0e0a0').grid(row=i, column=j, padx=3, pady=3)
                else:
                    Button(f, text=keys[i][j], width=8, bg='#d9e4f1').grid(row=i, column=j, padx=3, pady=3)

        self.bind_class("Button", "<ButtonRelease-1>", self.on_button)
    
    def center(self):
        """窗口居中"""
        
        self.update() # 更新显示以获取最新的窗口尺寸
        scr_w = self.winfo_screenwidth() # 获取屏幕宽度
        scr_h = self.winfo_screenheight() # 获取屏幕宽度
        
        w = self.winfo_width() # 窗口宽度
        h = self.winfo_height() # 窗口高度
        x = (scr_w-w)//2 # 窗口左上角x坐标
        y = (scr_h-h)//2 # 窗口左上角y坐标

        self.geometry('%dx%d+%d+%d'%(w,h,x,y)) # 设置窗口大小和位置
    
    def on_button(self, evt):
        """响应按键"""
        
        if self.screen.get() == 'Error':
            self.screen.set('')
        
        ch = evt.widget.cget('text')
        if ch == 'Clear':
            self.screen.set('')
        elif ch == 'Back':
            self.screen.set(self.screen.get()[:-1])
        elif ch == '=':
            try:
                result = str(eval(self.screen.get()))
            except:
                result = 'Error'
            self.screen.set(result)
        else:
            self.screen.set(self.screen.get() + ch)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()

'''

# 秒表
'''
import time
import threading
from tkinter import *

def on_btn():
    """点击按钮"""
    
    global t0
    
    if btn_name.get() == '开始':
        lcd.set('0.00')
        t0 = time.time()
        btn_name.set('停止')
    else:
        btn_name.set('开始')

def watch():
    """秒表计时线程函数"""
    
    while True:
        if btn_name.get() == '停止':
            lcd.set('%.2f'%(time.time()-t0))
        else:
            time.sleep(0.01)

root = Tk()
root.title('秒表')

btn_name = StringVar() # 按钮名
btn_name.set('开始')

t0 = 0 # 计时开始的时间戳
lcd = StringVar() # 液晶显示值
lcd.set('0:00')

f = Frame(root)
f.pack(padx=20, pady=10)

Label(f, textvariable=lcd, width=10, bg='#000030', fg='#30ff30', font=("Arial Bold", 24)).pack(pady=10)
Button(f, textvariable=btn_name, bg='#f0e0d0', command=on_btn).pack(fill=X, pady=10)

threading.Thread(target=watch).start()

root.mainloop()

'''

# 画板
# 主要利用 canvas 组件
'''
from tkinter import *
import tkinter.colorchooser as tc

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('画板')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        
        self.color = '#90f010' # 当前颜色
        self.pen = 3 # 当前画笔
        self.pos = None # 鼠标当前位置
        
        self.rbv = IntVar() # 当前画笔
        self.rbv.set(self.pen)
        
        self.cav = Canvas(self, bg='#ffffff', width=480, height=320)
        self.cav.pack(side=LEFT, padx=5, pady=5)
        
        self.cav.bind('<Button-1>', self.on_down)
        self.cav.bind('<ButtonRelease-1>', self.on_up)
        self.cav.bind('<B1-Motion>', self.on_motion)
        
        frame = Frame(self)
        frame.pack(side=LEFT, anchor=N, padx=5, pady=20)
        
        Radiobutton(frame, variable=self.rbv, text='1pix', value=1, command=self.on_radio).pack(ancho='w', padx=5, pady=5)
        Radiobutton(frame, variable=self.rbv, text='3pix', value=3, command=self.on_radio).pack(ancho='w', padx=5, pady=5)
        Radiobutton(frame, variable=self.rbv, text='5pix', value=5, command=self.on_radio).pack(ancho='w', padx=5, pady=5)
        Radiobutton(frame, variable=self.rbv, text='7pix', value=7, command=self.on_radio).pack(ancho='w', padx=5, pady=5)
        Radiobutton(frame, variable=self.rbv, text='9pix', value=9, command=self.on_radio).pack(ancho='w', padx=5, pady=5)
        
        self.btn = Button(frame, text='', width=6, bg=self.color, command=self.on_btn)
        self.btn.pack(padx=5, pady=10)
    
    def on_radio(self):
        """选择画笔"""
        
        self.pen = self.rbv.get()
    
    def on_btn(self):
        """选择颜色"""
        
        color = tc.askcolor()[1]
        if color:
            self.color = color
            self.btn.configure(bg=self.color)
    
    def on_down(self, evt):
        """左键按下"""
        
        self.pos = evt.x, evt.y
    
    def on_up(self, evt):
        """左键弹起"""
        
        self.pos = None
    
    def on_motion(self, evt):
        """鼠标移动"""
        
        if not self.pos is None:
            line = (*self.pos, evt.x, evt.y)
            self.pos = evt.x, evt.y
            self.cav.create_line(line, fill=self.color, width=self.pen)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
'''

# 集成matplotlib
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['FangSong']
matplotlib.rcParams['axes.unicode_minus'] = False

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        Tk.__init__(self)
        
        self.title('集成Matplotlib')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
        self.center()
    
    def init_ui(self):
        """初始化界面"""
        
        self.fig = Figure(dpi=150)
        self.cv = FigureCanvasTkAgg(self.fig, self)
        self.cv.get_tk_widget().pack(fill=BOTH, expand=1, padx=5, pady=5)
        
        f = Frame(self)
        f.pack(pady=10)
        Button(f, text='散点图', width=12, bg='#f0e0d0', command=self.on_scatter).pack(side=LEFT, padx=20)
        Button(f, text='等值线图', width=12, bg='#f0e0d0', command=self.on_contour).pack(side=LEFT, padx=20)
    
    def center(self):
        """窗口居中"""
        
        self.update() # 更新显示以获取最新的窗口尺寸
        scr_w = self.winfo_screenwidth() # 获取屏幕宽度
        scr_h = self.winfo_screenheight() # 获取屏幕宽度
        
        w = self.winfo_width() # 窗口宽度
        h = self.winfo_height() # 窗口高度
        x = (scr_w-w)//2 # 窗口左上角x坐标
        y = (scr_h-h)//2 # 窗口左上角y坐标

        self.geometry('%dx%d+%d+%d'%(w,h,x,y)) # 设置窗口大小和位置
    
    def on_scatter(self):
        """散点图"""
        
        x = np.random.randn(50) # 随机生成50个符合标准正态分布的点（x坐标）
        y = np.random.randn(50) # 随机生成50个符合标准正态分布的点（y坐标）
        color = 10 * np.random.rand(50) # 随即数，用于映射颜色
        area = np.square(30*np.random.rand(50)) # 随机数表示点的面积
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.scatter(x, y, c=color, s=area, cmap='hsv', marker='o', edgecolor='r', alpha=0.5)
        self.cv.draw()
    
    def on_contour(self):
        """等值线图"""
        
        y, x = np.mgrid[-3:3:60j, -4:4:80j]
        z = (1-y**5+x**5)*np.exp(-x**2-y**2)
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_title('有填充的等值线图')
        c = ax.contourf(x, y, z, levels=8, cmap='jet')
        self.fig.colorbar(c, ax=ax)
        self.cv.draw()

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()

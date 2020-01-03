# coding=utf-8

"""
@author:songmengyun
@file: android_keycode.py
@time: 2020/01/03

"""

from enum import unique, Enum


@unique
class KEYCODE(Enum):

    KEYCODE_CALL = 5  # 拨号键
    KEYCODE_ENDCALL = 6  # 挂机键
    KEYCODE_HOME = 3  # 按键Home
    KEYCODE_MENU = 82  # 菜单键
    KEYCODE_BACK = 4  # 返回键
    KEYCODE_SEARCH = 84  # 搜索键
    KEYCODE_CAMERA = 27  # 拍照键
    KEYCODE_FOCUS = 80  # 拍照对焦键
    KEYCODE_POWER = 26  # 电源键
    KEYCODE_NOTIFICATION = 83  # 通知键
    KEYCODE_MUTE = 91  # 话筒静音键
    KEYCODE_VOLUME_MUTE = 164  # 扬声器静音键
    KEYCODE_VOLUME_UP = 24  # 音量增加键
    KEYCODE_VOLUME_DOWN = 25  # 音量减小键
    KEYCODE_ENTER = 66  # 回车键
    KEYCODE_ESCAPE = 111  # ESC键
    KEYCODE_DPAD_CENTER = 23  # 导航键 确定键
    KEYCODE_DPAD_UP = 19  # 导航键 向上
    KEYCODE_DPAD_DOWN = 20  # 导航键 向下
    KEYCODE_DPAD_LEFT = 21  # 导航键 向左
    KEYCODE_DPAD_RIGHT = 22  # 导航键 向右
    KEYCODE_MOVE_HOME = 122  # 光标移动到开始键
    KEYCODE_MOVE_END = 123  # 光标移动到末尾键
    KEYCODE_PAGE_UP = 92  # 向上翻页键
    KEYCODE_PAGE_DOWN = 93  # 向下翻页键
    KEYCODE_DEL = 67  # 退格键
    KEYCODE_FORWARD_DEL = 112  # 删除键
    KEYCODE_INSERT = 124  # 插入键
    KEYCODE_TAB = 61  # Tab键
    KEYCODE_NUM_LOCK = 143  # 小键盘锁
    KEYCODE_CAPS_LOCK = 115  # 大写锁定键
    KEYCODE_BREAK = 121  # Break/Pause键
    KEYCODE_SCROLL_LOCK = 116  # 滚动锁定键
    KEYCODE_ZOOM_IN = 168  # 放大键
    KEYCODE_ZOOM_OUT = 169  # 缩小键

    KEYCODE_0 = 7  # 按键'0'
    KEYCODE_1 = 8  # 按键'1'
    KEYCODE_2 = 9  # 按键'2'
    KEYCODE_3 = 10  # 按键'3'
    KEYCODE_4 = 11  # 按键'4'
    KEYCODE_5 = 12  # 按键'5'
    KEYCODE_6 = 13  # 按键'6'
    KEYCODE_7 = 14  # 按键'7'
    KEYCODE_8 = 15  # 按键'8'
    KEYCODE_9 = 16  # 按键'9'
    KEYCODE_A = 29  # 按键'A'
    KEYCODE_B = 30  # 按键'B'
    KEYCODE_C = 31  # 按键'C'
    KEYCODE_D = 32  # 按键'D'
    KEYCODE_E = 33  # 按键'E'
    KEYCODE_F = 34  # 按键'F'
    KEYCODE_G = 35  # 按键'G'
    KEYCODE_H = 36  # 按键'H'
    KEYCODE_I = 37  # 按键'I'
    KEYCODE_J = 38  # 按键'J'
    KEYCODE_K = 39  # 按键'K'
    KEYCODE_L = 40  # 按键'L'
    KEYCODE_M = 41  # 按键'M'
    KEYCODE_N = 42  # 按键'N'
    KEYCODE_O = 43  # 按键'O'
    KEYCODE_P = 44  # 按键'P'
    KEYCODE_Q = 45  # 按键'Q'
    KEYCODE_R = 46  # 按键'R'
    KEYCODE_S = 47  # 按键'S'
    KEYCODE_T = 48  # 按键'T'
    KEYCODE_U = 49  # 按键'U'
    KEYCODE_V = 50  # 按键'V'
    KEYCODE_W = 51  # 按键'W'
    KEYCODE_X = 52  # 按键'X'
    KEYCODE_Y = 53  # 按键'Y'
    KEYCODE_Z = 54  # 按键'Z'

    KEYCODE_SPACE = 62          # 按键空格
    KEYCODE_GRAVE = 68          # '`'
    KEYCODE_MINUS = 69          # '-'
    KEYCODE_EQUALS = 70         # '='
    KEYCODE_LEFT_BRACKET = 71   # '['
    KEYCODE_RIGHT_BRACKET = 72  # ']'
    KEYCODE_BACKSLASH = 73      # '\'
    KEYCODE_SEMICOLON = 74      # ';'
    KEYCODE_APOSTROPHE = 75     # ''' (apostrophe)
    KEYCODE_SLASH = 76          # '/'
    KEYCODE_AT = 77             # '@'



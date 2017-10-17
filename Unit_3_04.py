# Created by: Khoa Le
# Created on October 13 2017
# Created for ICS3U
# This program tells you what year was a leap year.

import ui

def enter_touch_up_inside(sender):
    year = int(view['year_textfield'].text)
    if ((year % 100) == 0):
       if ((year % 400) == 0):
       	view['year_label'].text = ("Leap year")
       else:
       	view['year_label'].text = ("Not a leap year")
    else:
      if ((year % 4) == 0):
      	 view['year_label'].text = ("Leap year")
      else:
      	view['year_label'].text = ("Not a leap year")

view = ui.load_view()
view.present('sheet')

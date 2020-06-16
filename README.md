# Saver
A plugin for Blender to bypass the save dialog for saving renders.

Type ctrl + shift + cmd + s and your latest render will be saved with a date/time stamp to a folder named exports in your current directory.

Success and warning messages will be shown in the Blender footer status bar.

Current messages:
* Image Saved: given for successful image output
* You must render an image before saving: given if no render data exists yet

Date format:
YearMonthDay-HoursMinSec
200616-082103
This format was chosen because it is short, gives a unique id to the file name, allows file to be easily sorted by date without relying on metadata.
import os

def get_masks():
   os.chdir('C:\\mysite1\\twapp\\static\\masks\\')
   return os.listdir(os.getcwd())



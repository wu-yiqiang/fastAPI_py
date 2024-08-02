import sys
import os

def picture_path():
    project_dir = os.path.dirname(sys.argv[0])
    return  project_dir+'/statics/pictures/'
    print(project_dir)

def facedata_path():
    project_dir = os.path.dirname(sys.argv[0])
    return  project_dir+'/statics/trainer/'

def temps_path():
    project_dir = os.path.dirname(sys.argv[0])
    return  project_dir+'/statics/temps/'

def classifiers_path():
    project_dir = os.path.dirname(sys.argv[0])
    return project_dir + '/statics/classifiers/haarcascade_frontalface_default.xml'
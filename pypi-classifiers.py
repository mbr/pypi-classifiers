#!/usr/bin/env python
# coding=utf8

import gtk
import os

import urllib2

def reset_model():
    model = builder.get_object('classifiers_store')

    model.clear()

    # load data
    url = r'http://pypi.python.org/pypi?%3Aaction=list_classifiers'
    data = urllib2.urlopen(url)

    for line in data:
        model.append((False, line.strip()))


def on_cell_toggle(renderer, path):
    model = builder.get_object('classifiers_store')
    i = model.get_iter(path)

    # flip column 0, the "active" column
    model.set_value(i, 0, not model.get_value(i, 0))

    # update tree view
    chunks = ['classifiers=[']
    i = model.get_iter_first()
    while None != i:
        if True == model.get_value(i, 0):
            chunks.append("    '%s'," % model.get_value(i, 1))
        i = model.iter_next(i)
    chunks.append(']')

    builder.get_object('output').get_buffer().set_text('\n'.join(chunks))

builder = gtk.Builder()
builder.add_from_file(os.path.join(os.path.dirname(__file__), 'ui.xml'))

# load data
reset_model()

# set up GUI
mw = builder.get_object('main_window')
mw.connect('delete-event', lambda a, b: gtk.main_quit())
builder.get_object('renderer_active').connect('toggled', on_cell_toggle)



if '__main__' == __name__:
    import glib
    glib.set_application_name('PyPI classifiers selector 0.1')
    mw.show()
    gtk.main()

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 export2kmlDialog
                                 A QGIS plugin
 This plugin export point shapefile with timestamp field to kml
                             -------------------
        begin                : 2015-03-06
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Leonidas Liakos
        email                : leonidas_liakos@yahoo.gr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import time
import kmlgenerator
from qgis.core import *
from PyQt4 import QtGui, uic


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'export_2kml_dialog_base.ui'))


class export2kmlDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self,iface, parent=None):
        """Constructor."""
        super(export2kmlDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        
        self.iface = iface
        self.vlayer= self.iface.activeLayer() 
        fields = self.vlayer.pendingFields()
        for i in fields:
            self.comboBox_timestamp.addItem(i.name())
            self.comboBox_altitude.addItem(i.name())
        
        
        #Signals and slots
        self.button_box.accepted.connect(self.verify)
        
    
    def verify(self):
        
        fileName = QtGui.QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'), u"Αρχεία kml (*.kml)")
             
        if not fileName:
           return
      
      
       
        if not fileName.endswith('.kml'):
             fileName = fileName + '.kml'        
        
        

        iter = self.vlayer.getFeatures()
        
        positions=[] #list with all the positions        
        
        for feature in iter:
                # retrieve every feature with its geometry and attributes
                # fetch geometry
            geom = feature.geometry()
                #print "Feature ID %d: " % feature.id()
                #print "geometry", geom.type()
            
                # show some information about the feature
            
            
            
            if geom.type() == QGis.Point:
                 pnt = geom.asPoint()
                  
                 time_fld = self.vlayer.fieldNameIndex(self.comboBox_timestamp.currentText()) #get qgsfield by name
                 altitude_fld=self.vlayer.fieldNameIndex(self.comboBox_altitude.currentText()) #get qgsfield by name
                 
                 mytime = feature.attributes()[time_fld] #get feature attribute of field
                 
                 ttuple=time.strptime(mytime,'%Y-%m-%d %H:%M:%S')
                 
                 time_xml = time.strftime('%Y-%m-%dT%H:%M:%SZ', ttuple)
                 
                 altitude = feature.attributes()[altitude_fld] #get feature attribute of field

                 kmlposition = kmlgenerator.Position(u"Σημείο %s" %feature.id(),pnt.x(),pnt.y(),altitude,time_xml)
                 positions.append(kmlposition)
                 
        mykml =kmlgenerator.kmlobj(positions)
        mykml.writekml2disk(fileName)
        QMessageBox.information(None, u"Ενημέρωση!", u"Η εξαγωγή σε kml ολοκληρώθηκε!")
                          
        
        

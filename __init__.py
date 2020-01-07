# -*- coding: utf-8 -*-
"""
/***************************************************************************
 export2kml
                                 A QGIS plugin
 This plugin export point shapefile with timestamp field to kml
                             -------------------
        begin                : 2015-03-06
        copyright            : (C) 2015 by Leonidas Liakos
        email                : leonidas_liakos@yahoo.gr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load export2kml class from file export2kml.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from export_2kml import export2kml
    return export2kml(iface)

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OsmToFrench
                                 A QGIS plugin
 Ce plugin vise à récupérer les données osm en anglais et les traitées pour le mettre en français
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-09-08
        copyright            : (C) 2023 by SOUFOU Abdel Hafidhou
        email                : abdelhafidhou@live.fr
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
    """Load OsmToFrench class from file OsmToFrench.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from osmtofrench.OsmToFrench import OsmToFrench
    return OsmToFrench(iface)

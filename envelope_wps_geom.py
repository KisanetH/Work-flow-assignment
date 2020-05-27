# ---------------------
# Envelope Calculation function using WPS specification
# ---------------------
from osgeo import ogr
from osgeo import osr

def title():
    return "Envelope of a Geometry" # title of the function

def abstract():
    return "A function that calculates the envelope of a geometry." # short description of the function

def inputs():
    return [
        ['geom', 'Input geometry','The geometry of which envelope is to be calculated.','application/wkt', True]
    ]

def outputs():
    return [['env', 'Calculated Envelope','The calculated value of envelope of the given geometry.','application/json']]

def execute(parameters):

    geom = parameters.get('geom')

    if (geom is not None):
        geom = geom['value']

    geom1 = ogr.CreateGeometryFromWkt(geom)
    Envelope = geom1.GetEnvelope()
    print()
    print(Envelope)
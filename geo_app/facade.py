from geo_app.models import MunicipiosIBGE


def get_coords(ibge_id):

    try:
        city = MunicipiosIBGE.objects.using('geo_db').get(ibge_id=ibge_id)
    except MunicipiosIBGE.DoesNotExist:
        return None

    return [
        city.geom.point_on_surface.coords[1],
        city.geom.point_on_surface.coords[0]]

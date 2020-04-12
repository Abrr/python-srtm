from srtm.base_coordinates import RasterBaseCoordinates
from srtm.height_map_collection import HeightMapCollection


def test_height_map_collection_build_file_index():
    collection = HeightMapCollection()
    collection.build_file_index()
    assert len(collection.height_maps) == 13967


def test_height_map_collection_get_height_for_latitude_and_longitude():
    collection = HeightMapCollection()
    collection.build_file_index()
    assert (
        collection.get_height_for_latitude_and_longitude(latitude=40, longitude=-7)
        == 390
    )


def test_height_map_collection_load_area():
    collection = HeightMapCollection()
    collection.build_file_index()
    collection.load_area(
        RasterBaseCoordinates.from_file_name("N38W006"),
        RasterBaseCoordinates.from_file_name("N40W008"),
    )
    loaded_height_maps = [hm for hm in collection.height_maps.values() if hm.raster]
    assert len(loaded_height_maps) == 9


def test_height_map_collection_get_elevation_profile():
    collection = HeightMapCollection()
    collection.build_file_index()
    profile = collection.get_elevation_profile(
        start_latitude=40.103284,
        start_longitude=-7.453766,
        end_latitude=40.073772,
        end_longitude=-7.432998,
    )
    assert profile[0] == 566
    assert profile[-1] == 424
    assert len(profile) == 36

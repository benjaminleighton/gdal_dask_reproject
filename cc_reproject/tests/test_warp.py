from cc_reproject.warp import reproject
from rasterio.warp import Affine as A
# from rasterio.warp import Resampling
import numpy as np
import xarray as xr
# from xarray.testing import assert_equal
from pyproj.crs import CRS

from cc_reproject.tools import _add_coords_crs_tr_da

dem_asia_data = np.array([[[32, 30, 50, 50, 35, 9, 9, 227, 40, 250, 16, 41,
                            22, 254, 23],
                           [21, 17, 24, 45, 15, 50, 32, 24, 47, 13, 25, 22,
                            24, 13, 26],
                           [33, 38, 49, 49, 32, 53, 37, 39, 24, 40, 6, 30,
                            3, 16, 10],
                           [44, 60, 39, 26, 16, 51, 224, 41, 41, 39, 47, 238,
                            22, 11, 235],
                           [55, 54, 41, 50, 48, 55, 47, 41, 28, 33, 214, 218,
                            13, 255, 32],
                           [47, 50, 14, 50, 23, 47, 23, 13, 47, 29, 235, 10,
                            20, 199, 7],
                           [56, 26, 40, 39, 37, 28, 255, 63, 44, 238, 45, 27,
                            18, 0, 245],
                           [4, 44, 16, 10, 241, 45, 49, 236, 9, 58, 180, 225,
                            249, 246, 250],
                           [249, 37, 46, 33, 55, 10, 51, 219, 44, 200, 244,
                            246,
                            248, 249, 245],
                           [59, 68, 26, 42, 220, 66, 18, 45, 42, 238, 250, 245,
                            248, 244, 240],
                           [16, 58, 194, 4, 55, 26, 18, 57, 245, 200, 245, 0,
                            242, 244, 239],
                           [200, 182, 55, 225, 237, 60, 45, 51, 45, 226, 207,
                            249,
                            241, 243, 250],
                           [183, 37, 226, 47, 241, 251, 47, 41, 38, 234, 240,
                            15,
                            1, 33, 24],
                           [153, 214, 36, 215, 15, 45, 5, 255, 55, 192, 7, 3,
                            1, 16, 16],
                           [12, 242, 195, 47, 41, 246, 13, 238, 22, 35, 42, 29,
                            18, 253, 247]],

                          [[2, 0, 20, 20, 5, 235, 235, 197, 10, 220, 242, 11,
                            248, 224, 249],
                           [247, 243, 250, 15, 241, 20, 2, 250, 17, 239, 251,
                            248,
                            250, 239, 252],
                           [3, 8, 19, 19, 2, 23, 7, 9, 250, 10, 232, 0,
                            229, 242, 236],
                           [14, 30, 9, 252, 242, 21, 194, 11, 11, 9, 17, 208,
                            248, 237, 205],
                           [25, 24, 11, 20, 18, 25, 17, 11, 254, 3, 184, 188,
                            239, 225, 2],
                           [17, 20, 240, 20, 249, 17, 249, 239, 17, 255, 205,
                            236,
                            246, 169, 233],
                           [26, 252, 10, 9, 7, 254, 225, 33, 14, 208, 15, 253,
                            244, 226, 215],
                           [230, 14, 242, 236, 211, 15, 19, 206, 235, 28, 150,
                            195,
                            219, 216, 220],
                           [219, 7, 16, 3, 25, 236, 21, 189, 14, 170, 214, 216,
                            218, 219, 215],
                           [29, 38, 252, 12, 190, 36, 244, 15, 12, 208, 220,
                            215,
                            218, 214, 210],
                           [242, 28, 164, 230, 25, 252, 244, 27, 215, 170, 215,
                            226,
                            212, 214, 209],
                           [170, 152, 25, 195, 207, 30, 15, 21, 15, 196, 177,
                            219,
                            211, 213, 220],
                           [153, 7, 196, 17, 211, 221, 17, 11, 8, 204, 210,
                            241,
                            227, 3, 250],
                           [123, 184, 6, 185, 241, 15, 231, 225, 25, 162, 233,
                            229,
                            227, 242, 242],
                           [238, 212, 165, 17, 11, 216, 239, 208, 248, 5, 12,
                            255,
                            244, 223, 217]],

                          [[158, 156, 176, 176, 161, 135, 135, 97, 166, 120,
                            142, 167,
                            148, 124, 149],
                           [147, 143, 150, 171, 141, 176, 158, 150, 173, 139,
                            151, 148,
                            150, 139, 152],
                           [159, 164, 175, 175, 158, 179, 163, 165, 150, 166,
                            132, 156,
                            129, 142, 136],
                           [170, 186, 165, 152, 142, 177, 94, 167, 167, 165,
                            173, 108,
                            148, 137, 105],
                           [181, 180, 167, 176, 174, 181, 173, 167, 154, 159,
                            84, 88,
                            139, 125, 158],
                           [173, 176, 140, 176, 149, 173, 149, 139, 173, 155,
                            105, 136,
                            146, 69, 133],
                           [182, 152, 166, 165, 163, 154, 125, 189, 170, 108,
                            171, 153,
                            144, 126, 115],
                           [130, 170, 142, 136, 111, 171, 175, 106, 135, 184,
                            50, 95,
                            119, 116, 120],
                           [119, 163, 172, 159, 181, 136, 177, 89, 170, 70,
                            114, 116,
                            118, 119, 115],
                           [185, 194, 152, 168, 90, 192, 144, 171, 168, 108,
                            120, 115,
                            118, 114, 110],
                           [142, 184, 64, 130, 181, 152, 144, 183, 115, 70,
                            115, 126,
                            112, 114, 109],
                           [70, 52, 181, 95, 107, 186, 171, 177, 171, 96, 77,
                            119,
                            111, 113, 120],
                           [53, 163, 96, 173, 111, 121, 173, 167, 164, 104,
                            110, 141,
                            127, 159, 150],
                           [23, 84, 162, 85, 141, 171, 131, 125, 181, 62, 133,
                            129,
                            127, 142, 142],
                           [138, 112, 65, 173, 167, 116, 139, 108, 148, 161,
                            168, 155,
                            144, 123, 117]]], dtype=np.uint16)

bounds = (
 96.66666666666661, 26.666666666666668, 106.66666666666659, 36.66666666666667)

input_crs = 'EPSG:4326'

transform = A(0.6666666666666653, 0.0, 96.66666666666661,
              0.0, -0.6666666666666669, 36.66666666666667)

dem_asia = _add_coords_crs_tr_da(dem_asia_data, bounds, input_crs, transform)

dem_asia_wm_data = np.array([[[32, 30, 50, 35, 9, 9, 227, 40, 250, 16, 22, 254,
                               23],
                              [21, 17, 24, 15, 50, 32, 24, 47, 13, 25, 24, 13,
                               26],
                              [33, 38, 49, 32, 53, 37, 39, 24, 40, 6, 3, 16,
                               10],
                              [44, 60, 39, 16, 51, 224, 41, 41, 39, 47, 22, 11,
                               235],
                              [55, 54, 41, 48, 55, 47, 41, 28, 33, 214, 13,
                               255,
                               32],
                              [55, 54, 41, 48, 55, 47, 41, 28, 33, 214, 13,
                               255,
                               32],
                              [47, 50, 14, 23, 47, 23, 13, 47, 29, 235, 20,
                               199,
                               7],
                              [56, 26, 40, 37, 28, 255, 63, 44, 238, 45, 18, 0,
                               245],
                              [4, 44, 16, 241, 45, 49, 236, 9, 58, 180, 249,
                               246,
                               250],
                              [249, 37, 46, 55, 10, 51, 219, 44, 200, 244, 248,
                               249,
                               245],
                              [59, 68, 26, 220, 66, 18, 45, 42, 238, 250, 248,
                               244,
                               240],
                              [16, 58, 194, 55, 26, 18, 57, 245, 200, 245, 242,
                               244,
                               239],
                              [200, 182, 55, 237, 60, 45, 51, 45, 226, 207,
                               241, 243,
                               250],
                              [183, 37, 226, 241, 251, 47, 41, 38, 234, 240, 1,
                               33,
                               24],
                              [153, 214, 36, 15, 45, 5, 255, 55, 192, 7, 1, 16,
                               16],
                              [12, 242, 195, 41, 246, 13, 238, 22, 35, 42, 18,
                               253,
                               247]],

                             [[2, 0, 20, 5, 235, 235, 197, 10, 220, 242, 248,
                               224,
                               249],
                              [247, 243, 250, 241, 20, 2, 250, 17, 239, 251,
                               250, 239,
                               252],
                              [3, 8, 19, 2, 23, 7, 9, 250, 10, 232, 229, 242,
                               236],
                              [14, 30, 9, 242, 21, 194, 11, 11, 9, 17, 248,
                               237,
                               205],
                              [25, 24, 11, 18, 25, 17, 11, 254, 3, 184, 239,
                               225,
                               2],
                              [25, 24, 11, 18, 25, 17, 11, 254, 3, 184, 239,
                               225,
                               2],
                              [17, 20, 240, 249, 17, 249, 239, 17, 255, 205,
                               246, 169,
                               233],
                              [26, 252, 10, 7, 254, 225, 33, 14, 208, 15, 244,
                               226,
                               215],
                              [230, 14, 242, 211, 15, 19, 206, 235, 28, 150,
                               219, 216,
                               220],
                              [219, 7, 16, 25, 236, 21, 189, 14, 170, 214, 218,
                               219,
                               215],
                              [29, 38, 252, 190, 36, 244, 15, 12, 208, 220,
                               218, 214,
                               210],
                              [242, 28, 164, 25, 252, 244, 27, 215, 170, 215,
                               212, 214,
                               209],
                              [170, 152, 25, 207, 30, 15, 21, 15, 196, 177,
                               211, 213,
                               220],
                              [153, 7, 196, 211, 221, 17, 11, 8, 204, 210, 227,
                               3,
                               250],
                              [123, 184, 6, 241, 15, 231, 225, 25, 162, 233,
                               227, 242,
                               242],
                              [238, 212, 165, 11, 216, 239, 208, 248, 5, 12,
                               244, 223,
                               217]],

                             [[158, 156, 176, 161, 135, 135, 97, 166, 120, 142,
                               148, 124,
                               149],
                              [147, 143, 150, 141, 176, 158, 150, 173, 139,
                               151, 150, 139,
                               152],
                              [159, 164, 175, 158, 179, 163, 165, 150, 166,
                               132, 129, 142,
                               136],
                              [170, 186, 165, 142, 177, 94, 167, 167, 165, 173,
                               148, 137,
                               105],
                              [181, 180, 167, 174, 181, 173, 167, 154, 159, 84,
                               139, 125,
                               158],
                              [181, 180, 167, 174, 181, 173, 167, 154, 159, 84,
                               139, 125,
                               158],
                              [173, 176, 140, 149, 173, 149, 139, 173, 155,
                               105, 146, 69,
                               133],
                              [182, 152, 166, 163, 154, 125, 189, 170, 108,
                               171, 144, 126,
                               115],
                              [130, 170, 142, 111, 171, 175, 106, 135, 184, 50,
                               119, 116,
                               120],
                              [119, 163, 172, 181, 136, 177, 89, 170, 70, 114,
                               118, 119,
                               115],
                              [185, 194, 152, 90, 192, 144, 171, 168, 108, 120,
                               118, 114,
                               110],
                              [142, 184, 64, 181, 152, 144, 183, 115, 70, 115,
                               112, 114,
                               109],
                              [70, 52, 181, 107, 186, 171, 177, 171, 96, 77,
                               111, 113,
                               120],
                              [53, 163, 96, 111, 121, 173, 167, 164, 104, 110,
                               127, 159,
                               150],
                              [23, 84, 162, 141, 171, 131, 125, 181, 62, 133,
                               127, 142,
                               142],
                              [138, 112, 65, 167, 116, 139, 108, 148, 161, 168,
                               144, 123,
                               117]]], dtype=np.uint16)

dst_crs = 'EPSG:3857'

wm_bounds = (
 10760884.11001644, 4392745.707443533, 11874079.017949173, 3081887.523237937)

wm_transform = A(85630.37753328725, 0.0, 10760884.11001644,
                 0.0, -81928.63651284989, 4392745.707443535)

dem_asia_wm = _add_coords_crs_tr_da(dem_asia_wm_data, wm_bounds, dst_crs,
                                    wm_transform)
dem_asia_dsk = dem_asia.chunk(((1, 2), (5, 5, 5), (5, 5, 5)))

dem_asia_wm_20x10_data = np.array([[[32, 50, 50, 9, 9, 40, 250, 41, 22, 23],
                                    [21, 24, 45, 50, 32, 47, 13, 22, 24, 26],
                                    [21, 24, 45, 50, 32, 47, 13, 22, 24, 26],
                                    [33, 49, 49, 53, 37, 24, 40, 30, 3, 10],
                                    [44, 39, 26, 51, 224, 41, 39, 238, 22,
                                     235],
                                    [44, 39, 26, 51, 224, 41, 39, 238, 22,
                                     235],
                                    [55, 41, 50, 55, 47, 28, 33, 218, 13, 32],
                                    [47, 14, 50, 47, 23, 47, 29, 10, 20, 7],
                                    [56, 40, 39, 28, 255, 44, 238, 27, 18,
                                     245],
                                    [56, 40, 39, 28, 255, 44, 238, 27, 18,
                                     245],
                                    [4, 16, 10, 45, 49, 9, 58, 225, 249, 250],
                                    [249, 46, 33, 10, 51, 44, 200, 246, 248,
                                     245],
                                    [59, 26, 42, 66, 18, 42, 238, 245, 248,
                                     240],
                                    [59, 26, 42, 66, 18, 42, 238, 245, 248,
                                     240],
                                    [16, 194, 4, 26, 18, 245, 200, 0, 242,
                                     239],
                                    [200, 55, 225, 60, 45, 45, 226, 249, 241,
                                     250],
                                    [183, 226, 47, 251, 47, 38, 234, 15, 1,
                                     24],
                                    [153, 36, 215, 45, 5, 55, 192, 3, 1, 16],
                                    [153, 36, 215, 45, 5, 55, 192, 3, 1, 16],
                                    [12, 195, 47, 246, 13, 22, 35, 29, 18,
                                     247]],

                                   [[2, 20, 20, 235, 235, 10, 220, 11, 248,
                                     249],
                                    [247, 250, 15, 20, 2, 17, 239, 248, 250,
                                     252],
                                    [247, 250, 15, 20, 2, 17, 239, 248, 250,
                                     252],
                                    [3, 19, 19, 23, 7, 250, 10, 0, 229, 236],
                                    [14, 9, 252, 21, 194, 11, 9, 208, 248,
                                     205],
                                    [14, 9, 252, 21, 194, 11, 9, 208, 248,
                                     205],
                                    [25, 11, 20, 25, 17, 254, 3, 188, 239, 2],
                                    [17, 240, 20, 17, 249, 17, 255, 236, 246,
                                     233],
                                    [26, 10, 9, 254, 225, 14, 208, 253, 244,
                                     215],
                                    [26, 10, 9, 254, 225, 14, 208, 253, 244,
                                     215],
                                    [230, 242, 236, 15, 19, 235, 28, 195, 219,
                                     220],
                                    [219, 16, 3, 236, 21, 14, 170, 216, 218,
                                     215],
                                    [29, 252, 12, 36, 244, 12, 208, 215, 218,
                                     210],
                                    [29, 252, 12, 36, 244, 12, 208, 215, 218,
                                     210],
                                    [242, 164, 230, 252, 244, 215, 170, 226,
                                     212, 209],
                                    [170, 25, 195, 30, 15, 15, 196, 219, 211,
                                     220],
                                    [153, 196, 17, 221, 17, 8, 204, 241, 227,
                                     250],
                                    [123, 6, 185, 15, 231, 25, 162, 229, 227,
                                     242],
                                    [123, 6, 185, 15, 231, 25, 162, 229, 227,
                                     242],
                                    [238, 165, 17, 216, 239, 248, 5, 255, 244,
                                     217]],

                                   [[158, 176, 176, 135, 135, 166, 120, 167,
                                     148, 149],
                                    [147, 150, 171, 176, 158, 173, 139, 148,
                                     150, 152],
                                    [147, 150, 171, 176, 158, 173, 139, 148,
                                     150, 152],
                                    [159, 175, 175, 179, 163, 150, 166, 156,
                                     129, 136],
                                    [170, 165, 152, 177, 94, 167, 165, 108,
                                     148, 105],
                                    [170, 165, 152, 177, 94, 167, 165, 108,
                                     148, 105],
                                    [181, 167, 176, 181, 173, 154, 159, 88,
                                     139, 158],
                                    [173, 140, 176, 173, 149, 173, 155, 136,
                                     146, 133],
                                    [182, 166, 165, 154, 125, 170, 108, 153,
                                     144, 115],
                                    [182, 166, 165, 154, 125, 170, 108, 153,
                                     144, 115],
                                    [130, 142, 136, 171, 175, 135, 184, 95,
                                     119, 120],
                                    [119, 172, 159, 136, 177, 170, 70, 116,
                                     118, 115],
                                    [185, 152, 168, 192, 144, 168, 108, 115,
                                     118, 110],
                                    [185, 152, 168, 192, 144, 168, 108, 115,
                                     118, 110],
                                    [142, 64, 130, 152, 144, 115, 70, 126, 112,
                                     109],
                                    [70, 181, 95, 186, 171, 171, 96, 119, 111,
                                     120],
                                    [53, 96, 173, 121, 173, 164, 104, 141, 127,
                                     150],
                                    [23, 162, 85, 171, 131, 181, 62, 129, 127,
                                     142],
                                    [23, 162, 85, 171, 131, 181, 62, 129, 127,
                                     142],
                                    [138, 65, 173, 116, 139, 148, 161, 155,
                                     144, 117]]], dtype=np.uint16)

wm_20x10_bounds = (
 10760884.11001644, -5758266661736.368, 11874079.017949173, 4392745.707443535)

wm_20x10_transform = A(111319.4907932734, 0.0, 10760884.11001644,
                       0.0, -65542.9092102799, 4392745.707443535)

wm_20x10 = _add_coords_crs_tr_da(dem_asia_wm_20x10_data, wm_20x10_bounds,
                                 dst_crs, wm_20x10_transform)


def test_np_reproject():
    reprojected = reproject(dem_asia, dst_crs)

    assert isinstance(reprojected, xr.DataArray)
    assert isinstance(reprojected.data, np.ndarray)
    assert reprojected.data.shape == dem_asia_wm.data.shape

    sp_ref = reprojected.spatial_ref
    assert CRS(sp_ref.crs_wkt).to_string() == dst_crs

    GeoTransform = sp_ref.GeoTransform
    repr_transform = A.from_gdal(*[float(num) for num in
                                   GeoTransform.split(' ')])
    assert repr_transform == wm_transform
    for coord in dem_asia_wm.coords:
        assert np.all(dem_asia_wm[coord] == reprojected.coords[coord])

    assert np.all(reprojected.data == dem_asia_wm.data)
    # final global test with xarray's assert equal
    # does not work yet
    # assert_equal(reprojected_np, dem_asia_wm)


def test_uint8_dtype():
    dem_asia_8 = dem_asia.copy()
    dem_asia_8.data = dem_asia_8.data.astype(np.uint8)
    reprojected = reproject(dem_asia_8, dst_crs)
    # test reprojection works and results same as for uint16
    assert np.all(reprojected.data == dem_asia_wm.data)
    # test dtype conversion
    assert reprojected.data.dtype == np.uint8


def test_np_dst_shape():
    dst_shape = (3, 20, 10)
    reprojected = reproject(dem_asia, dst_crs, dst_shape=dst_shape)

    assert isinstance(reprojected, xr.DataArray)
    assert isinstance(reprojected.data, np.ndarray)

    sp_ref = reprojected.spatial_ref
    assert CRS(sp_ref.crs_wkt).to_string() == dst_crs

    GeoTransform = sp_ref.GeoTransform
    repr_transform = A.from_gdal(*[float(num) for num in
                                   GeoTransform.split(' ')])
    assert repr_transform == wm_20x10_transform

    for coord in wm_20x10.coords:
        assert np.all(wm_20x10[coord] == reprojected.coords[coord])

    assert np.all(reprojected.data == wm_20x10.data)

    # finally test shape matches input
    assert reprojected.shape == dst_shape

# def test_np_reproject_kwargs():
#     reprojected = reproject(dem_asia, dst_crs, resampling=Resampling.min)
#     assert reprojected.data.shape == None
#     assert isinstance(repr_np_kwargs.data, np.ndarray)
#     assert CRS(repr_np_kwargs.spatial_ref.crs_wkt).to_string() == dst_crs
#     assert isinstance(repr_np_kwargs, xr.DataArray)


# def test_np_to_dsk():
#     repr_np_dsk = reproject(elev_ll, dst_crs, chunks=((1, 2), (169, 169), (206, 205))) # noqa: E501
#     repr_np_dsk_2 = reproject(elev_ll, dst_crs, numblocks=(2, 2, 2))
#     assert repr_np_dsk.data.shape == (3, 338, 411)
#     assert repr_np_dsk_2.data.shape == (3, 338, 411)
#     assert isinstance(repr_np_dsk.data, da.Array)
#     assert isinstance(repr_np_dsk_2.data, da.Array)


# def test_reproject_dsk():
#     reprojected_dsk = reproject(elev_ll_dsk, dst_crs)
#     assert isinstance(reprojected_dsk.data, da.Array)
#     assert isinstance(reprojected_dsk, xr.DataArray)
#     assert reprojected_dsk.data.shape == (3, 338, 411)


# def test_repr_dsk_kwargs():
#     repr_dsk_kwargs = reproject(elev_ll_dsk, dst_crs, resmapling=Resampling.min) # noqa: E501
#     repr_dsk_bnd_kwargs = reproject(elev_ll_dsk, dst_crs, band_kwargs={0: {'resampling': Resampling.min}}, resampling=Resampling.bilinear) # noqa: E501

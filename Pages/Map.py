# ------------------------------------------------------------------------------
# This code is licensed under the Attribution-NonCommercial-ShareAlike 4.0
# International (CC BY-NC-SA 4.0) License.
#
# You are free to:
# - Share: Copy and redistribute the material in any medium or format
# - Adapt: Remix, transform, and build upon the material
#
# Under the following terms:
# - Attribution: You must give appropriate credit, provide a link to the license,
#   and indicate if changes were made. You may do so in any reasonable manner,
#   but not in any way that suggests the licensor endorses you or your use.
# - NonCommercial: You may not use the material for commercial purposes.
# - ShareAlike: If you remix, transform, or build upon the material, you must
#   distribute your contributions under the same license as the original.
#
# For more details, see https://creativecommons.org/licenses/by-nc-sa/4.0/
# ------------------------------------------------------------------------------

"""InstaGeo Serve Module.

InstaGeo Serve is a web application that enables the visualisation of GeoTIFF files in an
interactive map.
"""

import glob
import json
import os
from pathlib import Path
import re

import streamlit as st
from viz import create_map_with_geotiff_tiles



def generate_map(
    directory: str, year: int, month: int, country_tiles: list[str]
) -> None:
    """Generate the plotly map.

    Arguments:
        directory (str): Directory containing GeoTiff files.
        year (int): Selected year.
        month (int): Selected month formatted as an integer in the range 1-12.
        country_tiles (list[str]): List of MGRS tiles for the selected country.

    Returns:
        None.
    """
    try:
        root_path = os.path.abspath(os.getcwd())
        directory = root_path + '/' + directory
        if not directory or not Path(directory).is_dir():
            raise ValueError("Invalid directory path.")
        prediction_tiles = glob.glob(os.path.join(directory, f"{year}/{month}/*.tif"))
        # print(prediction_tiles[0].split("_")[3].strip("T").strip('.tif'))
        # tiles_to_consider = [
        #     tile
        #     for tile in prediction_tiles
        #     if os.path.basename(tile).split("_")[3].strip("T").strip('.tif') in country_tiles
        # ]
        print(extract_code(prediction_tiles[0]))
        tiles_to_consider = [
            tile
            for tile in prediction_tiles
            if extract_code(os.path.basename(tile)) in country_tiles
        ]
        print(tiles_to_consider)
        if not tiles_to_consider:
            raise FileNotFoundError(
                "No GeoTIFF files found for the given year, month, and country."
            )

        fig = create_map_with_geotiff_tiles(tiles_to_consider)
        st.plotly_chart(fig, use_container_width=True)
    except (ValueError, FileNotFoundError, Exception) as e:
        st.error(f"An error occurred: {str(e)}")


def extract_code(filename):
    """
    Code to extract the es435435 code from the filename so that we can match it to the country code and make it appear on the map
    """
    match = re.search(r'_T(.*?)_', filename)
    return match.group(1) if match else None

def main() -> None:
    """Instageo Serve Main Entry Point."""
    st.set_page_config(layout="wide")
    st.title("🌍 Locus Breeding Hotspots Map")

    st.sidebar.subheader(
        "This application provides an interactive mapping solution for visualizing GeoTIFF data, enabling strategic insights into locust breeding hotspots",
        divider="rainbow",
    )
    st.sidebar.header("Settings")
    with open(
        "./utils/country_code_to_mgrs_tiles.json"
    ) as json_file:
        countries_to_tiles_map = json.load(json_file)

    with st.sidebar.container():
        directory = st.sidebar.text_input(
            "GeoTiff Directory:",
            help="Write the path to the directory containing your GeoTIFF files",
        )
        country_code = st.sidebar.selectbox(
            "ISO 3166-1 Alpha-2 Country Code:",
            options=list(countries_to_tiles_map.keys()),
        )
        year = st.sidebar.number_input("Select Year", 2020, 2024)
        month = st.sidebar.number_input("Select Month", 1, 12)

    if st.sidebar.button("Generate Map"):
        country_tiles = countries_to_tiles_map[country_code]
        print(country_tiles)
        generate_map(directory, year, month, country_tiles)
    else:
        st.plotly_chart(
            create_map_with_geotiff_tiles(tiles_to_overlay=[]), use_container_width=True
        )


if __name__ == "__main__":
    main()

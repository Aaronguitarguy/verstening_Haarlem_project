def compress_raster(input_path, output_path):
    import rasterio
    
    with rasterio.open(input_path) as src:
        data = src.read()
        profile = src.profile.copy()

    profile.update({
        "compress": "lzw",
        "tiled": True
    })

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(data)

    print(f"Gecomprimeerde raster opgeslagen naar: {output_path}")

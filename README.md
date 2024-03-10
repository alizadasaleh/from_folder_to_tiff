## Requirements

- Python 3.6 or newer
- Pillow (PIL Fork)

Before running the script, ensure you have Python 3 installed on your system and the Pillow library, which can be installed using pip:

```bash
pip install Pillow
```
## Installation

1. Download `create_grid.py` to your local machine.
2. Make the script executable (Unix-like systems):
   ```bash
   chmod +x create_grid.py
   ```

## Usage

### Basic Command

```bash
./create_grid.py output_filename 1369_12_Наклейки\ 3-D_3/ [1388_2_Наклейки\ 3-D_1/ ...] [options]
```

- `output_filename`: The name of the output TIFF file.
- `1369_12_Наклейки\ 3-D_3/ [1388_2_Наклейки\ 3-D_1/ ...]`: One or more folders containing the images to be included in the grid.

### Options

- `--grid_size ROWS,COLUMNS`: Specify the grid size as rows and columns. For example, `3,3` for a 3x3 grid. If not specified, the script arranges all images in a single row.
- `--image_size WIDTH,HEIGHT`: Specify the size of each image in the grid. For example, `800,600` for images of 800x600 pixels. If not specified, the script uses the size of the first image.
- `--border_size SIZE`: The size of the border between images in pixels. Defaults to 10 pixels if not specified.

### Examples

1. Create a TIFF grid using all images from `1369_12_Наклейки\ 3-D_3/`, with default settings:

   ```bash
   ./create_grid.py output.tif 1369_12_Наклейки\ 3-D_3/
   ```

2. Create a TIFF grid using images from `1369_12_Наклейки\ 3-D_3/` and `1388_2_Наклейки\ 3-D_1/`, arranged in a 2x2 grid, with each image resized to 500x500 pixels and a border size of 20 pixels:

   ```bash
   ./create_grid.py output.tif 1369_12_Наклейки\ 3-D_3/ 1388_2_Наклейки\ 3-D_1/ --grid_size 2,2 --image_size 500,500 --border_size 20
   ```

### Windows Users

If you're using Windows, you may need to run the script through Python directly:

```bash
python create_grid.py output.tif 1369_12_Наклейки\ 3-D_3/ --grid_size 3,3 --image_size 800,800 --border_size 20
```

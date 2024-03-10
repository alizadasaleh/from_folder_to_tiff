#!/usr/bin/env python3

from PIL import Image
import os
import argparse

def parse_arguments():
    """Parse command line arguments for creating a grid of images."""
    parser = argparse.ArgumentParser(description="Create a grid of images with borders and save it as a TIFF file.")
    parser.add_argument("output_filename", help="The filename for the output TIFF image.")
    parser.add_argument("folders", nargs='+', help="Folder paths containing the images.")
    parser.add_argument("--grid_size", type=lambda s: [int(item) for item in s.split(',')], help="Grid size as rows,columns, e.g., 2,3")
    parser.add_argument("--image_size", type=lambda s: [int(item) for item in s.split(',')], help="Image size as width,height, e.g., 800,600")
    parser.add_argument("--border_size", type=int, default=10, help="Border size between images.")
    return parser.parse_args()

def load_images(folders, image_size=None):
    """Load and optionally resize images from given folders."""
    images = []
    for folder in folders:
        for image_file in filter(lambda f: f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')), os.listdir(folder)):
            try:
                img_path = os.path.join(folder, image_file)
                with Image.open(img_path) as img:
                    if image_size:
                        images.append(img.resize(image_size, Image.ANTIALIAS))
                    else:
                        images.append(img.copy())
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
    return images

def create_tiff_grid(output_filename, images, grid_size=None, border_size=10):
    """Create a grid of images with specified border size and save as a TIFF."""
    if not images:
        print("No images found.")
        return

    image_size = images[0].size
    grid_size = grid_size or (1, len(images))
    canvas_width = grid_size[1] * image_size[0] + (grid_size[1] + 1) * border_size
    canvas_height = grid_size[0] * image_size[1] + (grid_size[0] + 1) * border_size
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')

    for i, img in enumerate(images):
        row, col = divmod(i, grid_size[1])
        x_position = col * image_size[0] + (col + 1) * border_size
        y_position = row * image_size[1] + (row + 1) * border_size
        canvas.paste(img, (x_position, y_position))

    canvas.save(output_filename, format='TIFF')

if __name__ == "__main__":
    args = parse_arguments()
    images = load_images(args.folders, tuple(args.image_size) if args.image_size else None)
    create_tiff_grid(args.output_filename, images, tuple(args.grid_size) if args.grid_size else None, args.border_size)

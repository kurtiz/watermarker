# Watermarker
## Image Processing Tools

This repository contains two Python scripts designed to automate the process of watermarking images (`watermark.py`) and converting CR2 (Canon Raw version 2) files to JPEG format (`c2j.py`). These tools are ideal for photographers or digital artists who frequently need to watermark their work and convert raw images to a more accessible format.

## Installation

Before using the scripts, you must install the required Python packages. These dependencies are listed in the `requirements.txt` file included in this repository.

To install the dependencies, run:

```sh
pip install -r requirements.txt
```

## watermark.py

`watermark.py` is a command-line tool that applies a watermark to a batch of images. It supports JPEG, PNG, and CR2 image formats.

### Features

- Batch watermarking for image directories
- Adjustable watermark opacity
- Customizable watermark position
- Watermark sizing based on image percentage

### Usage

To use `watermark.py`, specify the path to your watermark image, the directory of images to watermark, and the output directory for the watermarked images. Options for watermark opacity, position, and size are also available.

```sh
python watermark.py <watermark_path> <input_dir> <output_dir> --opacity <opacity> --position <position> --size <size_percentage>
```

Arguments:
- `<watermark_path>`: Path to the watermark image (transparent PNG recommended).
- `<input_dir>`: Directory of images to be watermarked.
- `<output_dir>`: Directory for saving watermarked images.
- `--opacity` (optional): Watermark opacity from 0 (transparent) to 1 (opaque).
- `--position` (optional): Watermark position (`topleft`, `topright`, `bottomleft`, `bottomright`, `bottomcenter`).
- `--size` (optional): Watermark size as a percentage of the image size.

Example:

```sh
python watermark.py watermark.png ./images ./watermarked --opacity 0.7 --position bottomcenter --size 20
```

## c2j.py

`c2j.py` converts CR2 raw images to high-quality JPEG images in a batch process.

### Usage

Run `c2j.py` with the directory of CR2 files and the desired output directory for the JPEGs. The JPEG quality can also be specified.

```sh
python c2j.py <input_dir> <output_dir> --quality <quality>
```

Arguments:
- `<input_dir>`: Directory containing CR2 files.
- `<output_dir>`: Directory for saving converted JPEGs.
- `--quality` (optional): Quality of JPEG images, default is 95.

Example:

```sh
python c2j.py ./raw_images ./converted_images --quality 90
```

## Motivation

With a high volume of images requiring watermarking and format conversion, I developed these scripts to automate what was once a tedious manual process. The motivation was to save time and ensure consistency in the watermarking process, as well as to facilitate the easy conversion of raw files to a more shareable format. These tools were crafted to be a part of an efficient digital workflow, empowering users to focus more on creative aspects rather than repetitive tasks.

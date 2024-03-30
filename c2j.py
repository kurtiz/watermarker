import os
import argparse
import rawpy
import imageio


def convert_cr2_to_jpg(input_dir, output_dir, quality=95):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.cr2'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.jpg")

            with rawpy.imread(input_path) as raw:
                rgb = raw.postprocess()
            imageio.imsave(output_path, rgb, quality=quality)

            print(f"Converted {filename} to JPG.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CR2 images to high quality JPG images.")
    parser.add_argument('input_dir', type=str, help="Directory containing CR2 files.")
    parser.add_argument('output_dir', type=str, help="Directory to save converted JPG files.")
    parser.add_argument('--quality', type=int, default=95, help="Quality of the output JPG images (default is 95).")

    args = parser.parse_args()

    convert_cr2_to_jpg(args.input_dir, args.output_dir, args.quality)

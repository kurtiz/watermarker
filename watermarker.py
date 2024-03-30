import argparse
import os

import rawpy
from PIL import Image, ImageEnhance


def apply_watermark_to_image(base_image, watermark, opacity, position, size_percentage):
    # Calculate the new size of the watermark

    if base_image.width < base_image.height:
        watermark_height = int(base_image.height * size_percentage / 100)
        watermark_width = int(watermark_height * watermark.width / watermark.height)
        watermark = watermark.resize((int(watermark_width * 1.5), int(watermark_height * 1.5)), Image.Resampling.LANCZOS)
    else:
        watermark_width = int(base_image.width * size_percentage / 100)
        watermark_height = int(watermark_width * watermark.height / watermark.width)
        watermark = watermark.resize((watermark_width, watermark_height), Image.Resampling.LANCZOS)

    # Set watermark transparency
    if opacity < 1:
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)

    # Position the watermark
    watermark_position = {
        "bottomright": (base_image.width - watermark.width, base_image.height - watermark.height),
        "bottomleft": (0, base_image.height - watermark.height),
        "topright": (base_image.width - watermark.width, 0),
        "topleft": (0, 0),
        "bottomcenter": ((base_image.width - watermark.width) // 2, base_image.height - watermark.height + 50)
    }.get(position, (0, 0))

    # Apply watermark
    transparent = Image.new("RGBA", base_image.size)
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, watermark_position, mask=watermark)
    return transparent.convert("RGB")  # Convert back to RGB


def batch_watermark(watermark_path, input_dir, output_dir, opacity, position, size_percentage):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    watermark = Image.open(watermark_path).convert("RGBA")

    for image_file in os.listdir(input_dir):
        image_path = os.path.join(input_dir, image_file)
        output_image_path = os.path.join(output_dir, image_file)

        # Check for CR2 files and handle them accordingly
        if image_file.lower().endswith('.cr2'):
            with rawpy.imread(image_path) as raw:
                rgb = raw.postprocess()
            base_image = Image.fromarray(rgb)
            output_image_path = output_image_path.rsplit('.', 1)[0] + '.jpg'
        elif image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            base_image = Image.open(image_path).convert("RGBA")
        else:
            print(f"Skipping unsupported image format: {image_file}")
            continue

        watermarked_image = apply_watermark_to_image(base_image, watermark, opacity, position, size_percentage)
        watermarked_image.save(output_image_path)
        print(f"Watermarked {image_file}")


def main():
    parser = argparse.ArgumentParser(description="Apply a watermark to a batch of images, including CR2 raw images.")
    parser.add_argument("watermark", help="The watermark image file")
    parser.add_argument("input_dir", help="The directory of images to watermark")
    parser.add_argument("output_dir", help="The directory where watermarked images will be saved")
    parser.add_argument("--opacity", type=float, default=0.5, help="The opacity of the watermark")
    parser.add_argument(
        "--position",
        type=str,
        default="bottomright",
        choices=["topleft", "topright", "bottomleft", "bottomright", "bottomcenter"],
        help="The position of the watermark"
    )
    parser.add_argument(
        "--size",
        type=float,
        default=10.0,
        help="The size of the watermark as a percentage of the base image size"
    )

    args = parser.parse_args()

    batch_watermark(args.watermark, args.input_dir, args.output_dir, args.opacity, args.position, args.size)


if __name__ == "__main__":
    main()

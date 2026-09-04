import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF decoder with Pillow
register_heif_opener()

def main():
    input_dir = "images"
    output_dir = "outputs"
    
    for infile in os.listdir(input_dir):
        # Join folder path with filename
        in_path = os.path.join(input_dir, infile)
        
        # Skip if it's a directory
        if not os.path.isfile(in_path):
            continue

        f, e = os.path.splitext(infile)
        outfile = os.path.join(output_dir, f + ".jpg")

        if infile != f + ".jpg":
            try:
                with Image.open(in_path) as im:
                    # Convert to RGB since JPEG doesn't support RGBA/alpha channels
                    im.convert("RGB").save(outfile, "JPEG")
                print(f"Converted {infile} -> {f}.jpg")
            except OSError as err:
                print("Cannot convert", infile, "-", err)

if __name__ == '__main__':
    main()
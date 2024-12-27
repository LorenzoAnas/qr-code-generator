import csv
import qrcode
from PIL import Image

def generate_qr_codes(data_list):
    for item in data_list:
        url = item.get("data")
        name = item.get("name")
        
        if not url or not name:
            print(f"Skipping invalid entry: {item}")
            continue
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Save the QR code image with the given name
        filename = f"{name}.png"
        img.save(filename)
        print(f"QR code generated for {url} and saved as '{filename}'")

# Read data from a CSV file
data_list = []
with open(r"data\ips_to_convert.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data_list.append({"data": row["data"], "name": row["name"]})

generate_qr_codes(data_list)
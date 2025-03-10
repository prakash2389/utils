import os
import zipfile
from PIL import Image
extract_path = r"D:\PRAJ Industries\PRAJ_toRAI_READY"
file_list = os.listdir(extract_path)

def unzip_folder(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

for file_name in file_list:
    if os.path.join(extract_path, file_name).endswith(".zip"):
        unzip_folder(os.path.join(extract_path, file_name), extract_path)
        new_path = os.path.join(extract_path, file_name.replace(".zip", ""))
        new_file_list = os.listdir(new_path)
        for new_file_name in new_file_list:
            if new_file_name.lower().endswith(".scn"):
                print(new_file_name)
                with open(os.path.join(new_path, new_file_name), 'r') as file:
                    m = file.read()
                    print(len(m))
                    k = m.split("\n")
                    dcn = [i for i in k if i[:4] == "DCN="]
                    print(dcn[0][4:])
                    OriginalImage = [i for i in k if "PDF" in i]
                    if len(OriginalImage)!=0:
                        new_pdf_path = os.path.join(extract_path, file_name.replace(".zip", ""), "OrgFiles")
                        if os.path.exists(new_pdf_path):
                            new_pdf_file = os.listdir(new_pdf_path)
                            final = os.path.join(new_pdf_path, new_pdf_file[0])
                            print(final)
                    else:
                        tifs = [i for i in new_file_list if i.lower().endswith(".tif")]
                        # Open the first image and convert it to RGB
                        images = [Image.open(os.path.join(new_path, file)).convert("RGB") for file in tifs]
                        # Save as PDF
                        output_pdf = os.path.join(new_path, "merged_output.pdf")
                        images[0].save(output_pdf, save_all=True, append_images=images[1:])
                        print(f"PDF saved successfully as {output_pdf}")
                        final = os.path.join(new_path, "merged_output.pdf")
                        print(final)

import os
import time
from PIL import Image

ATTRIBUTES_IMAGE_PATH = 'attribute_frames.PNG'
NO_ATTRIBUTES_IMAGE_PATH = 'no_attribute_frames.PNG'
TEST_IMAGE_PATH = 'test_images/test.PNG'
BASE_DIR_PATH = '../images'
MONSTER_PAGE_DIR = 'monster_images/'

def get_frame(att_num: int, ind: int):
    attributes_img = Image.open(os.path.join(BASE_DIR_PATH,ATTRIBUTES_IMAGE_PATH))
    no_attributes_img = Image.open(os.path.join(BASE_DIR_PATH, NO_ATTRIBUTES_IMAGE_PATH))

    if att_num != 6:
        start_x = 2 + (att_num * 102)
        start_y = 2 + (ind * 104)
        return attributes_img.crop((start_x, start_y, start_x + 96, start_y + 96))
    
    # case where no attribute
    start_x = 2
    start_y = 2 + (ind * 104)
    return no_attributes_img.crop((start_x, start_y, start_x + 96, start_y + 96))

# add reutnr type
def get_image(id: int = 3, attributes: list[int] = [6, 3], output_path: str = TEST_IMAGE_PATH):
    images_to_remove: list[str] = []
    page_num: int = (id // 100) + 1
    page_str: str = str(page_num).zfill(3)
    file_name: str = 'CARDS_' + page_str + '.PNG'
    path: str = os.path.join(BASE_DIR_PATH, MONSTER_PAGE_DIR)
    path = os.path.join(path, file_name)
    print("file name is ", file_name)

    try:
        # get base monster image
        # each monster has a width and height of 96, and total paddings are 2px with 6 pixels inbetween monsters
        monsters_page_img = Image.open(path)
        start_x = 2 + 102 * ((id - 1) % 10)
        start_y = 2 + 102 * (((id - 1)%100)//10)
        print("startx is ", start_x, " starty is ", start_y)
        base_img = monsters_page_img.crop((start_x, start_y, start_x + 96, start_y + 96))
        base_image_path = "temp_images/monster" + str(id) + ".PNG"
        base_image_path = os.path.join(BASE_DIR_PATH, base_image_path)
        base_img.save(base_image_path)
        images_to_remove.append(base_image_path)


        # get attributes to overlay on top
        attribute_imgs = [get_frame(att, ind) for ind, att in enumerate(attributes)]
        attribute_frame_img = attribute_imgs[0]
        if len(attribute_imgs) > 1:
            for img in attribute_imgs[1:]:
                attribute_frame_img.paste(img, (0,0), img)

        # # combine both images
        final_monster_img = Image.new('RGB', (96,96), color='white')
        final_monster_img.paste(base_img, (0,0), base_img)
        final_monster_img.paste(attribute_frame_img,(0,0), attribute_frame_img)

        final_monster_img.save(output_path)

    except IOError as err:
        print("errored!")
        print(err)


if __name__ == '__main__':
    get_image(11141)
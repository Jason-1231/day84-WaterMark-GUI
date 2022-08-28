from PIL import Image, ImageTk

main_img = Image.open('waterfall.jpeg')
logo_img = Image.open('Kobe_logo.png').convert("RGBA")

# Dimensions
width, height = main_img.size
l_height = int(round(height / 3, 0))
l_width = int(round(width / 3, 0))
l_pos_x = width - l_width
l_pos_y = height - l_height

# Resize logo image
logo_img = logo_img.resize((l_width, l_height))
logo_img.show()

transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
transparent.paste(main_img, (0, 0))
transparent.paste(logo_img, (l_pos_x, l_pos_y), mask=logo_img)
transparent.show()

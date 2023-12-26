import config

def get_img_path(filename):
	return f'{config.CAPTCHA_DIR}/{filename[:6]}/{filename}'
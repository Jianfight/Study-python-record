"""该方法不适用与gif格式的图片，.jpg、.png都适用"""
from PIL import Image
import argparse

def get_char(r, g, b, alpha=255):
	"""将获取的RGB值转换为相应的灰度值，并且定义一个ASCII码值列表，将某段灰度值指定相应的字符"""
	if alpha == 0:
		return ' '
	else:
		# 因为python在计算整形的数字时速度比浮点型快，所以故将公式变换为整形的形式。
		gary = (2126 * r + 7152 * g + 722 * b) / 10000
		#print(gary)
		ascii_char = list("$@B%8&WM#*abcdefghijklmnopqrstuvwxyzABDEFGHJKLMNQRTUVWXYZ/\|()1{}[]?-_+~<>i!lI;:,\"^`'123456789.")
		#print(ascii_char)
		x = int((gary / alpha) * len(ascii_char))
		#print(x)
		return ascii_char[x-1]

def out_write_file(out_file_name,content):
	with open(out_file_name, 'w') as f:
		f.write(content)

def main(file_name, out_file_name="out_file.txt", width=100, height=50):
	"""打开图片文件，调整图片尺寸，使用嵌套读取图片中的每一个像素并将其转换为字符"""
	text = ""
	picture = Image.open(file_name)
	picture = picture.resize((width,height))
	for i in range(height):
		for j in range(width):
			content = picture.getpixel((j,i))
			# print(content)
			
			text += get_char(*content)
		text += "\n"
	print(text)
	out_write_file(out_file_name,text)

'''
def parse_param():
	""" param analyzer"""
	parser = argparse.ArgumentParser()
	# input_file
	parser.add_argument("input_file")
	parser.add_argument("out_file")

	parser.add_argument("--width", type=int, default=100)
	parser.add_argument("--height", type=int, default=50)
	args = parser.parse_args()
	width, height, in_file, out_file = args.width, args.height, args.input_file, args.out_file
	return width, height, input_file, out_file
'''

if __name__ == '__main__':
	#width, height, in_f, out_f = parse_param()
	file_name = input("Please enter name of file: ")
	main(file_name)
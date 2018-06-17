name = "wang jian"
print(name.title())
print(name.upper())
print(name.lower())
#.title()方法将字符串中的每个单词的首字母改为大写，.upper()方法将字符串中的字母全改为大写，.lower()方法将字符串中的字母全改写为小写

fise_name = "wang"
last_name = "jian"
full_name = fise_name + " " + last_name
print(full_name.title())
print("Hellow, " + full_name.title() +"!")

#将相应的字符串存储到变量中在输出
message = "Hellow, " + full_name.title() + "!";
print (message);

#换行符\n 制表符\t
print("language: \n\tPython\n\tC\n\tJavaScript")

#删除空白
#删除字符串末尾的空白 .rstrip() 删除字符串开头的空白 .lstrip() 删除字符串两端的空白 .strip()
favorite_language = '    Python !  '
print(favorite_language.rstrip())  #删除末尾
print(favorite_language.lstrip())  #删除开头
print(favorite_language.strip())   #删除两端

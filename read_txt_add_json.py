#coding:utf-8
import json


def read_json():
	f = open("data.json","r",encoding='utf-8')
	result = json.load(f)
	pre_guojianeiluan = result['国家内乱']
	for keys in result.keys():
		print(keys,len(result[keys]))
	print(len(pre_guojianeiluan))
	data_list = read_txt()
	print(len(data_list))
	# txt文档 1行标题一行内容，格式固定
	for i in range(0,len(data_list),2):
		term = {}
		term["title"] = data_list[i]
		term["context"] = data_list[i+1]
		pre_guojianeiluan.append(term)

	result["国家内乱"] = pre_guojianeiluan
	for keys in result.keys():
		print(keys,len(result[keys]))

	f = open("bbbbbbbbbbbb.json","w",encoding='utf8')
	f.write(json.dumps(result,  ensure_ascii=False))
	f.close()
	# print(type(result))
	# print(result['国家内乱'])
	pass


def read_txt():
	txt_info = open("66666.txt","r",encoding='utf-8')
	result = txt_info.readlines()
	txt_info.close()
	return result
	# print(result)	
	# print(type(result))


if __name__ == '__main__':
	read_json()
	# read_txt()
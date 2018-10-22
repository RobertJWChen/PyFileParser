import sys

def main():

	if len(sys.argv) < 3:
		print("please enter pattern config file path & source file path")
		sys.exit(1)
	pattern_config_path = sys.argv[1]
	file_in = sys.argv[2]
	pattern_file = open(pattern_config_path,'rb')
	pattern_text = pattern_file.readline()
	pattern_tags =  pattern_text.split(' ')

	pattern_file.close
	pattern_tags_length = len(pattern_tags)
	f = open (file_in, "rb")
	text = bytearray(f.read())
	f.close
	sp = 0
	ep = 0
	file_count = 0
	for b in text:
		ep+=1

		if (ep == len(text)-pattern_tags_length):
			write('./result/part'+str(file_count), text[sp:ep])
			ep+=pattern_tags_length
			break
		found_pattern_tags = False
		offset = 0
		for tag in pattern_tags:
			if (text[ep+offset] == int(tag,0)):
				found_pattern_tags = True
			else:
				found_pattern_tags = False
				break
			offset = offset+1
		if (found_pattern_tags == True):	
			#Find a header
			write('./result/part'+str(file_count), text[sp:ep])
			sp = ep
			file_count=file_count+1
	print("### Parsing Completed! input file size: "+str(ep)+"byte, seperated to "+str(file_count)+" files in ./result/ folder")

def write(output_file_path, data_buf):
	fout = open(output_file_path, 'wb+')
	fout.write(data_buf)
	fout.close()

if __name__ == "__main__":
	main()

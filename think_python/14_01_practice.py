def sed(old_str, new_str, old_file, new_file):
    try:
        fp = open(old_file)
        ft = open(new_file, 'w')
        for line in fp:
            if old_str in line:
                new_line = line.replace(old_str, new_str)
                ft.write(new_line)
            else:
                ft.write(line)
        ft.close()
    except:
        print('可能有些错误产生，请确认和检查')


sed('eBook is for the use of anyone', 'for anynoe', 'emma cop.txt', 'new_file.txt')
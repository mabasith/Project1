import yaml
def yaml_loader(filepath):
	with open(filepath, "r") as file_descriptor:
		data = yaml.load(file_descriptor)
	return data
def cp_update(nickname,x,y,theta,wp_type,index):
	cp_str =""
	cp_str += 'nickname' + str(index) + ': ' + nickname + '\n'
	cp_str += 'X' + str(index) + ': ' + str(x) + '\n'
	cp_str += 'Y' + str(index) + ': ' + str(y) + '\n'
	cp_str += 'theta' + str(index) + ': ' + str(theta) + '\n'
	cp_str += 'wp_type' + str(index) + ': ' + str(wp_type) + '\n\n'
	return cp_str
def buffer(index):
	for i in range(3):

		cp_str =""
		cp_str += 'nickname' + str(index) + ': ' + 'BFF'+str(i) + '\n'
		cp_str += 'X' + str(index) + ': ' + '0' + '\n'
		cp_str += 'Y' + str(index) + ': ' + '0' + '\n'
		cp_str += 'theta' + str(index) + ': ' + '0' + '\n'
		cp_str += 'wp_type' + str(index) + ': ' + 'WAYPOINT' + '\n\n'
		index+=1
		return index


if __name__ == "__main__":
	filepath='/home/hitech/cp.yaml'
	factory_path='/home/hitech/Documents/HAVELLS_MASTER/cp.yaml'
	data1=yaml_loader(filepath)
	cp_str1=''
	index=1378
	pre_nickname=''

	with open(factory_path, 'w') as cp_file:
		for i in range(201):
			nickname=data1['nickname' + str(i)]
			x=data1['X' + str(i)]
			y=data1['Y' + str(i)]
			theta=data1['theta' + str(i)]
			wp_type=data1['wp_type' + str(i)]
			cp_str1=cp_update(nickname,x,y,theta,wp_type,index)
			cp_file.writelines(cp_str1)
			index+=1
			pre_nickname=nickname
			nic_list=list(nickname)
			pre_nic_list=list(pre_nickname)
			







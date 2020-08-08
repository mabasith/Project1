def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i],list):
            for index in index_all(search_list[i],item):
                indices.append([i]+index)
    return indices

def main():
    print(index_all([1, 2, [4,2,4],9,[7,4,2,1],[[1,2,4]]], 2))

if __name__=="__main__":
    main()
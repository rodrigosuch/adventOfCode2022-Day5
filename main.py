import re
INPUT_FILE = "input_origin.txt"
def populate_list():
    list_idx = 0
    with open(INPUT_FILE) as file:
        line = file.readline()
        while line[1] != '1':
            for line_idx in range(1, list_size*4 ,4):
                if len(line) > line_idx and line[line_idx] != " ":
                    list[list_idx].append(line[line_idx])
                list_idx += 1
            list_idx = 0
            line = file.readline()


def find_list_size():
    with open(INPUT_FILE) as file:
        line = file.readline()
        while line[1] != '1':
            line = file.readline()
    return int((len(line) + 1)/4)

def read_cmds():
    with open(INPUT_FILE) as file:
        line = file.readline()
        while line != '':
            if line[0] == 'm':
                cmd = re.split("move | from | to |\n", line)
                for item in list[int(cmd[2])-1][0:int(cmd[1])]:
                    list[int(cmd[3])-1].insert(0, item)
                    list[int(cmd[2]) - 1].pop(0)
                #print(cmd)
                #print(list)

            line = file.readline()


list_size = 0
list = []


list_size = find_list_size()

for _ in range(0, list_size):
    list.append([])

populate_list()
read_cmds()
print(list)
for item in list:
    print(item[0])
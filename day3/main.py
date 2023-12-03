
def main(filename: str):

    with open(filename, 'r') as f:
        line = f.readline()
        schematic = []
        
        while line:
            line_list = [x for x in line if x != '\n']
            schematic.append(line_list)
            line = f.readline()

    return schematic

if __name__ == "__main__":
    print(main('test.txt'))
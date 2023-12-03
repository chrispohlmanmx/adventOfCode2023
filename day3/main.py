


def check_adjacent_and_diag(x: int, y: int, array: list):
    left = x - 1 
    right = x + 1
    above = y - 1
    below = y + 1

    special_chars = '*'
    
    # check cardinal directions
    if left >= 0:
        if array[y][left] in special_chars:
            num_star_mapping[f'{x},{y}'] = [y,left]
            return True
    if right <= len(array[y]) -1:
        if array[y][right] in special_chars:
            num_star_mapping[f'{x},{y}'] = [y,right]
            return True
    if above >= 0:
        if array[above][x] in special_chars:
            num_star_mapping[f'{x},{y}'] = [above,x]
            return True
    if below <= len(array) - 1:
        if array[below][x] in special_chars:
            num_star_mapping[f'{x},{y}'] = [below,x]
            return True
    # check diaganols
    if left >= 0 and above >= 0:
        if array[above][left] in special_chars:
            num_star_mapping[f'{x},{y}'] = [above,left]
            return True
    if right <= len(array[y]) - 1 and above >= 0:
        if array[above][right] in special_chars:
            num_star_mapping[f'{x},{y}'] = [above,right]
            return True
    if below <= len(array) - 1 and left >= 0:
        if array[below][left] in special_chars:
            num_star_mapping[f'{x},{y}'] = [below,left]
            return True
    if below <= len(array) - 1 and right <= len(array[below]) - 1:
        if array[below][right] in special_chars:
            num_star_mapping[f'{x},{y}'] = [below,right]
            return True
    else:
        return False



def main(filename: str):
    nums_to_sum = []
    num_pairs = []
    star_num_pair_mapping = {}
    with open(filename, 'r') as f:
        line = f.readline()
        schematic = []
        
        while line:
            line_list = [x for x in line if x != '\n']
            schematic.append(line_list)
            line = f.readline()

    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if check_adjacent_and_diag(x, y, schematic) and char != '.':
                #walk backwards to find starting x coord for num
                curr_num = ''
                curr_nums_star = []
                start_x = x
                end_x = x
                for i in range(x, -1, -1):
                    if row[i].isnumeric():
                        start_x = i
                    else:
                        break
                # walk forwards to find ending x coord for num
                for i in range(x, len(row)):
                    if row[i].isnumeric():
                        end_x = i
                    else:
                        break
                curr_num = int(curr_num.join(row[start_x:end_x+1]))
                curr_nums_star = num_star_mapping[f'{x},{y}']
                curr_nums_star_key = f'{curr_nums_star[0]},{curr_nums_star[1]}'
                if curr_nums_star_key in star_num_pair_mapping:
                    star_num_pair_mapping[curr_nums_star_key].append(curr_num)
                else:
                    star_num_pair_mapping[curr_nums_star_key] = [curr_num]
                row[start_x:end_x+1] = '.' * ((end_x - start_x) + 1)
    
    
    for key in star_num_pair_mapping:
        if len(star_num_pair_mapping[key]) == 2:
            pair = star_num_pair_mapping[key]
            value = pair[0] * pair[1]
            nums_to_sum.append(value)

    # print(nums_to_sum)
    print(sum(nums_to_sum))
    return 'finished'

if __name__ == "__main__":
    num_star_mapping = {}
    print(main('test.txt'))
    num_star_mapping = {}
    print(main('puzzle3.txt'))
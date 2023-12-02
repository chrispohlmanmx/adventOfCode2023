# Stole the values from a reddit answer, didn't get a clean win on this one
num_hash = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    }

def main1(file):
    with open(file, 'r') as f:
        line = f.readline()
        sums = []
        while line:
            nums = [x for x in line if x.isnumeric()]
            num_to_add = nums[0] + nums[-1]
            sums.append(int(num_to_add))
            line = f.readline()
    return sum(sums)

def main2(file):
    sums = [];
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            for key in num_hash.keys():
                if key in line:
                    line = line.replace(key, num_hash[key])
            nums = [x for x in line if x.isnumeric()]
            num_to_add = nums[0] + nums[-1]
            sums.append(int(num_to_add))
            line = f.readline()
        
    return (sum(sums))


    f = open('puzzle1.txt')

    res = 0




    for i,l in enumerate(f):
        # print(i,l)
        m =  [None, None]
        x = re.search('(one|two|three|four|five|six|seven|eight|nine|[0-9])', l)
        m[0] = l[x.start():x.end()] 
        n = len(l)
        for i in range(n-1,-1,-1):
            x = re.match('(one|two|three|four|five|six|seven|eight|nine|[0-9])', l[i:n])
            if x is not None:
                m[1] = l[i:n][x.start():x.end()]
                break

        res += int(str(to_int(m[0]))+str(to_int(m[1])))

    print(res)
        
if __name__ == "__main__":
    print(main1('puzzle1.txt'))

    print(main2('puzzle1.txt'))
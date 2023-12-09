

def main(file: str):
    with open(file, 'r') as f:
        line = f.readline()

        cards = {}
        count = 1
        while line:
            cards[count] = {'winning_nums': [], 'nums_elf_has': [], 'copies': 1}
            line = line[line.index(':')+1:-1]
            winning_nums, nums_elf_has = line.split('|')

            winning_nums = winning_nums.split(' ')
            winning_nums = [x for x in winning_nums if x != '']
            cards[count]['winning_nums'] = winning_nums
            
            nums_elf_has = nums_elf_has.split(' ')
            nums_elf_has = [x for x in nums_elf_has if x != '']
            cards[count]['nums_elf_has'] = nums_elf_has

            count += 1
            line = f.readline()

        card_values = []

        for card in cards.keys():
            num_of_matches = 0
            for num in cards[card]['nums_elf_has']:
                if num in cards[card]['winning_nums']:
                    num_of_matches += 1
            
            for i in range(cards[card]['copies']):
                for i in range(1, num_of_matches + 1):
                    cards[card + i]['copies'] += 1

            card_values.append(cards[card]['copies'])


    print(sum(card_values))
    return 


if __name__== "__main__":
    main('puzzle4.txt')
    # main('test.txt')
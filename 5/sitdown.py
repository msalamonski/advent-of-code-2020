#!/usr/bin/python3
''' AoC 5 '''
with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def seat():
    ''' find the highest seat ID on a boarding pass '''
    seat_id_list = []
    for board in INP: # boarding pass
        divisor = 128
        row = [1, divisor]
        divisor_col = 8
        col = [1, divisor_col]
        print(board + ' || ', end='')
        for half in list(board[:7]): # row
            if half == 'F':
                divisor /= 2
                row[1] -= divisor
            else:
                divisor /= 2
                row[0] += divisor
            # print(row[1] - row[0])
            print(row)
            if row[1] - row[0] == 1:
                if half == 'B':
                    row_result = row[0] - 1
                else:
                    row_result = row[1] - 1
                print('row: ' + str(row_result), end='')
                break

        for other in list(board[7:]): # column
            if other == 'L':
                divisor_col /= 2
                col[1] -= divisor_col
            else:
                divisor_col /= 2
                col[0] += divisor_col
            # print(col)
            if col[1] - col[0] == 1:
                if other == 'L':
                    col_result = col[0] - 1
                else:
                    col_result = col[1] - 1
                print(' | col: ' + str(col_result), end='')
                break

        seat_id = (row_result * 8) + col_result
        print(' | seat_id: ' + str(seat_id))
        seat_id_list.append(seat_id)
    return max(seat_id_list) # 823 BBFFBBFRRR row 102 col 7 # 824 is too low

def proper_seat():
    ''' pieces taken from others, to study from '''
    seatidlist = []
    for board in INP:
        s = board.rstrip()
        x1 = int(s[:7].replace('F', '0').replace('B', '1'), 2)
        x2 = int(s[7:].replace('L', '0').replace('R', '1'), 2)
        print(x1 * 8 + x2)
        seatidlist.append(x1*8 + x2)
    print('---')
    openseats = list(range(0, 127 * 8 + 7))
    diff = [x for x in openseats if x not in seatidlist]
    print(diff)
    return max(seatidlist)

if __name__ == '__main__':
    print(proper_seat())
    # print(seat())
    # seat()

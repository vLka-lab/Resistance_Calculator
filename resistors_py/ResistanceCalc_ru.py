def Float_chek(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        value = input('Введите ЧИСЛО БОЛЬШЕ 0: ')

def File_open(path, mode, write_wa=None):
    try:
        file = open(path, mode)
    except:
        print(f'Файл - {path} - не найден')
        return False
    if mode == 'r':
        ret = file.read()
        file.close()
        return ret
    if mode == 'a':
        file.write(write_wa)
        file.close()
        return True
    if mode == 'w':
        file.write(write_wa)
        file.close()
        return True
    
def Calc_paralel_res(r1, r2):
    rret = r1 * r2 / (r1 + r2)
    return rret

run = True
all_resistorsT = File_open('YourResistors.txt', 'r')
while all_resistorsT == False:
    run = False
    break
all_resistorsLS = all_resistorsT.split()
all_resistors = list(map(float, all_resistorsLS))
var = '0'
print('Все считаные резисторы:', all_resistors, '\n')
while run:
    var = input('Введите вариант действия:\nПоследовательное подключение - 1\nПаралельноe подключение - только расчёт сопративления - 2\n')
    if var == '1':
        counter = 0
        v_ref = Float_chek(input('Vref = '))
        v_out = Float_chek(input('Vout = '))
        for r2 in all_resistors:
            r1 = r2 * (v_out/v_ref - 1)
            if r1 in all_resistors:
                print('R1:', r1, 'R2:', r2,)
                counter =+ 1
        # if counter == 0:
        #     for r2 in all_resistors:
        #         r1 = r2 * (v_out/v_ref - 1)
        #         for r12 in all_resistors:
        #             if r12 != r1:
        #                 r11 = r1 * r12 / (r12 - r1)
        #                 if r11 in all_resistors:
        #                     print(f'R1 в паралельном подключении: {r1}, состоит из - R1.1: {r12}, R1.2 {r11}, R2: {r2}')
        if counter == 0:
            paralel_var = {}
            for r11 in all_resistors:
                for r12 in all_resistors:
                    for r21 in all_resistors:
                        for r22 in all_resistors:
                            v_out_calc =  (((r11 * r12) * (r21 + r22) ) / ((r21 * r22) * (r11 + r12)) + 1) * v_ref
                            key = abs(v_out - v_out_calc)
                            paralel_var.update({key: (r11, r12, r21, r22)})
            sorted_paralel_var = dict(sorted(paralel_var.items()))
            keys = list(sorted_paralel_var.keys())
            result_r = sorted_paralel_var[keys[0]] 
            print(f'Погрещность Vout: {keys[0]},\nR1.1 = {result_r[0]}, R1.2 = {result_r[1]} (R1 эквивалент = {Calc_paralel_res(result_r[0], result_r[1])})\nR2.1 = {result_r[2]}, R2.2 = {result_r[3]} (R2 эквивалент = {Calc_paralel_res(result_r[2], result_r[3])})')
            # r11 = result_r[0]
            # r12 = result_r[1]
            # r21 = result_r[2]
            # r22 = result_r[3]
            # print((((r11 * r12) * (r21 + r22) ) / ((r21 * r22) * (r11 + r12)) + 1) * v_ref)
            result_r = sorted_paralel_var[keys[1]] 
            print(f'Погрещность Vout: {keys[1]},\nR1.1 = {result_r[0]}, R1.2 = {result_r[1]} (R1 эквивалент = {Calc_paralel_res(result_r[0], result_r[1])})\nR2.1 = {result_r[2]}, R2.2 = {result_r[3]} (R2 эквивалент = {Calc_paralel_res(result_r[2], result_r[3])})')
            # r11 = result_r[0]
            # r12 = result_r[1]
            # r21 = result_r[2]
            # r22 = result_r[3]
            # print((((r11 * r12) * (r21 + r22) ) / ((r21 * r22) * (r11 + r12)) + 1) * v_ref)
            # print(((r11 / r21) * (r12 / r22)  * ((r21 + r22 ) / (r11 + r12)) + 1) * v_ref)
                             
                             
                         
    if var == '2':
        r1 = Float_chek(input('R1 = '))
        r2 = Float_chek(input('R2 = '))
        par = round((r1 * r2) / (r1 + r2), 4)
        print(f'Сопротивление при паралельном подключении - {r1}, {r2}: {par}')
        File_open('ResultParalel.txt', 'a', f'{r1}, {r2}: {par};\n')
    print('\n')

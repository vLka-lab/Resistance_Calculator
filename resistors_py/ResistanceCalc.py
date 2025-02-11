def fileOpen(path, mode, write_wa=None):
    file = open(path, mode)
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

AllResistors = fileOpen('YourResistors.txt', 'r').split()
AllResistors = list(map(float, AllResistors))
var = '0'
print('All your resistors:', AllResistors, '\n')
while True:
    var = input('Введите вариант действия:\nПоследовательное подключение - 1\nПаралельноe подключение - расчёт сопративления - 2\n')
    if var == '1':
        Vref = float(input('Vref = '))
        Vout = float(input('Vout = '))
        for r2 in AllResistors:
            r1 = r2 * (Vout/Vref - 1)
            if r1 in AllResistors:
                print('R1:', r1, 'R2:', r2,)
    if var == '2':
        R1 = float(input('R1 = '))
        R2 = float(input('R2 = '))
        par = round((R1 * R2) / (R1 + R2), 4)
        print(f'Сопротивление при паралельном подключении - {R1}, {R2}: {par}')
        fileOpen('ResultParalel.txt', 'a', f'{R1}, {R2}: {par};\n')
    print('\n')
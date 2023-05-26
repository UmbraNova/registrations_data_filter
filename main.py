registrations = open('registrations.txt', 'r')
registrations_good = open('registrations_good.log', 'w')
registrations_bad = open('registrations_bad.log', 'w')


def data_validation(data):
    error = ''
    try:
        if len(data) != 3:
            error = 'All three fields are NOT present'
            raise IndexError
        if not data[0].isalpha():
            error = 'Field |Name| contains NOT only letters'
            raise NameError
        if '@' not in data[1] or '.' not in data[1]:
            error = 'The |Email| field does NOT contain @ and . (dot)'
            raise SyntaxError
        if not 9 < int(data[2]) < 100:
            error = 'The |Age| field is NOT a number from 10 to 99'
            raise ValueError

        registrations_good.write('{}\n'.format(' '.join(data)))
    except:
        registrations_bad.write('{}\t\t {}\n'.format(' '.join(data), error))


for i_line in registrations:
    line = i_line.split()
    data_validation(line)

registrations.close()
registrations_good.close()
registrations_bad.close()

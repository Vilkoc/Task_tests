import unittest

#6
def task_6(d):
    return (((2 * 50 * d) / 30) ** 0.5) // 1

#12
def task_12():
    result = []
    for i in range(1000, 3001):
        if not ((i // 1000) % 2) and not (((i % 1000) // 100) % 2) and not (((i % 100) // 10) % 2) and not ((i % 10) % 2):
            result.append(str(i))
    return ','.join(result)

#18
def task_18 (password_list):
    import string
    result = []
    passwords = password_list.split(',')
    for password in passwords:
        flags = {'lower': False, 'capital': False, 'digit': False, 'char': False}
        for char in password:
            if char in string.ascii_lowercase and not flags['lower']:
                flags['lower'] = True
            if char in string.ascii_uppercase and not flags['capital']:
                flags['capital'] = True
            if char in string.digits and not flags['digit']:
                flags['digit'] = True
            if char in '$#@' and not flags['char']:
                flags['char'] = True

        if 6 <= len(password) <= 12 and all(flags.values()):
            # print(password, flags)
            result.append(password)

    return ', '.join(result)

def task_24(num):
    return str(num)

def task_30():
    d = {k:k*k for k in range(1, 4)}
    return d

def task_36():
    l = [element**2 for element in range(1, 21)]
    return l[-5:]

def task_42(num_list):
    return list(filter(lambda x: not x%2, num_list))

def task_48(email=''):
    # email = input('enter email: ')
    return email.split('@')[1].split('.')[0]

def task_54(n=10):
    # n = int(input('input finish number: '))
    def generator(n):
        i = 0
        while i <= n:
            yield str(i)
            i += 2
    #return ', '.join(list(generator(n)))
    return ', '.join(list(map(str, range(0, n+1, 2))))

def task_60():
    from random import randrange
    return [randrange(100, 201, 2) for i in range(5)]




class AllTest(unittest.TestCase):
    def test_task_6(self):
        self.assertEqual(task_6(180), 24)

    def test_task_12(self):
        self.assertEqual(task_12(), "2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888")

    def test_task_18(self):
        self.assertEqual(task_18('ABd1234@1,a F1#,2w3E*,2We3345'), 'ABd1234@1')

    def test_task_24(self):
        self.assertEqual(task_24(541), '541')

    def test_task_30(self):
        self.assertEqual(task_30(), {1: 1, 2: 4, 3: 9})

    def test_task_36(self):
        self.assertEqual(task_36(), [256, 289, 324, 361, 400])

    def test_task_42(self):
        self.assertEqual(task_42([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])

    def test_task_48(self):
        self.assertEqual(task_48('john@google.com'), 'google')

    def test_task_54(self):
        self.assertEqual(task_54(), '0, 2, 4, 6, 8, 10')

    def test_task_60(self):
        self.assertTrue(all([i for i in task_60() if 100 <= i <= 200 and not i%2]))



if __name__ == '__main__':
    unittest.main()
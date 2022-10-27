#!/usr/bin/env python3
# coding: utf8

from io import StringIO
from unittest.mock import patch
import unittest
import os
import sys
env = globals().copy()

<<<<<<< HEAD
os.chdir(os.path.dirname(os.path.abspath(__file__)))
=======
>>>>>>> 3e2b7c6 (Exercise template)

def runfile(name):
    filename = name + '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    code = compile(source, filename, 'exec')
    exec(code, env)


def patchio(*args):
    if args:
        return lambda meth: \
            patch('builtins.input', side_effect=list(args))(
                patch('sys.stdout', new_callable=StringIO)(lambda self, stdout, _: meth(self, stdout)))
    else:
        return lambda meth: \
            patch('sys.stdout', new_callable=StringIO)(meth)

########################################################################################################################


class TestCapitalLetters(unittest.TestCase):
    @patchio("KaluKaMa KaDo")
    def test_correct(self, stdout):
        runfile('capital_letters')
        self.assertRegex(stdout.getvalue(), "\\D*5\n*")


class TestPassword(unittest.TestCase):
    @patchio("Piotr4")
    def test_correct(self, stdout):
        runfile('password')
        self.assertRegex(stdout.getvalue(), "(The p|P)assword is secure.\n")

    @patchio("PPP4")
    def test_lowercase(self, stdout):
        runfile('password')
        self.assertRegex(stdout.getvalue(), "(The p|P)assword is insecure!\n")

    @patchio("ppp4")
    def test_capital(self, stdout):
        runfile('password')
        self.assertRegex(stdout.getvalue(), "(The p|P)assword is insecure!\n")

    @patchio("Asia")
    def test_digit(self, stdout):
        runfile('password')
        self.assertRegex(stdout.getvalue(), "(The p|P)assword is insecure!\n")


class Triangles:

    @staticmethod
    def triangle1(num):
        return [i * '*' for i in range(1, num+1)]

    @staticmethod
    def triangle2(num):
        return [(num-1-i) * ' ' + (2*i+1) * '*' for i in range(num)]

    def run_test(self, variant, stdout):
        variant = f"triangle{variant}"
        runfile(variant)
        result = [s.rstrip() for s in stdout.getvalue().split('\n')[:-1]]
        if all(s[0] == ' ' for s in result if s):
            result = [s[1:] for s in result if s]
        if result[0] == '':
            result = result[1:]
        if result[-1] == '':
            result = result[:-1]
        self.assertEqual(result, getattr(self, variant)(7))
        if result[0][0] == ' ':
            self.assertEqual(result, self.triangle2(7))
            del Triangles.triangle2
        else:
            self.assertEqual(result, self.triangle1(7))
            del Triangles.triangle1


class TestTriangle1(Triangles, unittest.TestCase):
    @patchio("7")
    def test_Triangle1(self, stdout):
        self.run_test(1, stdout)


class TestTriangle2(Triangles, unittest.TestCase):
    @patchio("7")
    def test_Triangle2(self, stdout):
        self.run_test(2, stdout)


class TestPiApproximations(unittest.TestCase):

    @patchio()
    def testPi(self, stdout):
        runfile('pi_approximations')
        results = [float(s.strip())
                   for s in stdout.getvalue().split('\n')[:-1]]
        correct = [
            3.133787490628162,
            3.137677900950937,
            3.138980103882128,
            3.139632221929398,
            3.140023818600600,
            3.140285018940355,
            3.140471657210304,
            3.140611672348951,
            3.140720594610756,
            3.140807746030402,
            3.140879060737555,
            3.140938495848743,
            3.140988791491478,
            3.141031905249145,
            3.141069272900385,
            3.141101971419381,
            3.141130824467760,
            3.141156472734795,
            3.141179422072162,
            3.141200077192821,
            3.141218765744481,
            3.141235755819479,
            3.141251268898044,
            3.141265489556666,
            3.141278572846968,
            3.141290649972213,
            3.141301832702638,
            3.141312216844878,
            3.141321884993700,
            3.141330908733529,
            3.141339350413953,
            3.141347264592388,
            3.141354699214476,
            3.141361696586238,
            3.141368294179572,
            3.141374525303569,
            3.141380419666945,
            3.141386003851691,
            3.141391301713876,
            3.141396334724335,
            3.141401122259511,
            3.141405681850745,
            3.141410029398788,
            3.141414179359083,
            3.141418144902313,
            3.141421938054040,
            3.141425569816519,
            3.141429050275261,
            3.141432388692585,
            3.141435593589904,
            3.141438672820382,
            3.141441633633147,
            3.141444482730302,
            3.141447226317554,
            3.141449870149334,
            3.141452419569085,
            3.141454879545318,
            3.141457254703932,
            3.141459549357223,
            3.141461767530038,
            3.141463912983323,
            3.141465989235413,
            3.141467999581278,
            3.141469947109970,
            3.141471834720463,
            3.141473665136055,
            3.141475440917473,
            3.141477164474823,
            3.141478838078521,
            3.141480463869233,
            3.141482043867057,
            3.141483579979864,
            3.141485074010990,
            3.141486527666306,
            3.141487942560709,
            3.141489320224108,
            3.141490662106949,
            3.141491969585295,
            3.141493243965543,
            3.141494486488775,
            3.141495698334787,
            3.141496880625828,
            3.141498034430078,
            3.141499160764838,
            3.141500260599553,
            3.141501334858578,
            3.141502384423766,
            3.141503410136892,
            3.141504412801906,
            3.141505393187018,
            3.141506352026689,
            3.141507290023438,
            3.141508207849566,
            3.141509106148777,
            3.141509985537671,
            3.141510846607150,
            3.141511689923770,
            3.141512516030945,
            3.141513325450136,
            3.141514118681956,
        ]
        # self.assertEqual(len(results), len(correct))
        for i, c in enumerate(correct):
            r = results[i]
            self.assertAlmostEqual(
                r, c, 6, f"{r} != {c} ({i+1} approximation)")


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())

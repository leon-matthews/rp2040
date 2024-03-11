"""
Fully Saturated Rainbow
=======================

        Red     Green   Blue

1       255     0       0
2       255     255     0
3       0       255     0
4       0       255     255
5       0       0       255
6       255     0       255
7       255     0       0      # Repeat of step 1


6 * 255 = 1,536 steps total

"""
import unittest


def rainbow(hue):
    # hue: 0 to 1529
    hue = hue % 1530

    # value: 0 to 255
    phase, value = divmod(hue, 255)
    if phase == 0:
        return (255, value, 0)
    elif phase == 1:
        return (255-value, 255, 0)
    elif phase == 2:
        return (0, 255, value)
    elif phase == 3:
        return (0, 255-value, 255)
    elif phase == 4:
        return (value, 0, 255)
    elif phase == 5:
        return (255, 0, 255-value)


class TestRainbow(unittest.TestCase):
    def test_phase_0(self):
        # Red through orange to yellow.
        self.assertEqual(rainbow(0),    (255,   0,   0))
        self.assertEqual(rainbow(1),    (255,   1,   0))
        self.assertEqual(rainbow(128),  (255, 128,   0))
        self.assertEqual(rainbow(254),  (255, 254,   0))

    def test_phase_1(self):
        # Yellow through chartreuse to green
        self.assertEqual(rainbow(255),  (255, 255,   0))
        self.assertEqual(rainbow(256),  (254, 255,   0))
        self.assertEqual(rainbow(384),  (126, 255,   0))
        self.assertEqual(rainbow(508),  (  2, 255,   0))
        self.assertEqual(rainbow(509),  (  1, 255,   0))

    def test_phase_2(self):
        # Green to cyan
        self.assertEqual(rainbow(510),  (  0, 255,   0))
        self.assertEqual(rainbow(640),  (  0, 255, 130))
        self.assertEqual(rainbow(764),  (  0, 255, 254))

    def test_phase_3(self):
        # Cyan to blue
        self.assertEqual(rainbow(765),  (  0, 255, 255))
        self.assertEqual(rainbow(893),  (  0, 127, 255))
        self.assertEqual(rainbow(1019), (  0,   1, 255))

    def test_phase_4(self):
        # Blue to purple
        self.assertEqual(rainbow(1020), (  0,   0, 255))
        self.assertEqual(rainbow(1147), (127,   0, 255))
        self.assertEqual(rainbow(1274), (254,   0, 255))

    def test_phase_5(self):
        self.assertEqual(rainbow(1275), (255,   0, 255))
        self.assertEqual(rainbow(1403), (255,   0, 127))
        self.assertEqual(rainbow(1529), (255,   0,   1))

    def test_roll_around(self):
        self.assertEqual(rainbow(1530), (255,   0,   0))


if __name__ == '__main__':
    unittest.main()

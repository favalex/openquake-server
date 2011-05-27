# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010-2011, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with OpenQuake.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License.


import unittest

from utils import log_scale


class ScalesTestCase(unittest.TestCase):
    """
    This test suite exercise the number scale generation in the
    :py:module:`utils` module.
    """

    def test_log_scale(self):
        lb = 0.060256
        ub = 9.780226
        n = 10

        expected_scale = [
            0.060255999999999997, 0.1060705, 0.1867192, 0.32868750000000002,
            0.57859870000000002, 1.0185251, 1.7929411, 3.1561694999999999,
            5.5559022999999996, 9.7802260000000008]

        scale = log_scale(lb, ub, n)

        # the first and last values in the scale should be equal to
        # the lower_bound and upper_bound, respectively
        self.assertEqual(lb, scale[0])
        self.assertEqual(ub, scale[-1])

        self.assertEqual(expected_scale, scale)

    def test_log_scale_raises_when_n_lt_2(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when 'n' is less than two ('n' indicates the length of the
        generated scale).
        """
        # args are in the order: lower_bound, upper_bound, n (num of elements)
        self.assertRaises(AssertionError, log_scale, 0.01, 0.1, 1)

    def test_log_scale_raises_when_lb_is_0(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when lower bound is 0.0.
        """
        self.assertRaises(AssertionError, log_scale, 0, 3.14, 10)

    def test_log_scale_raises_when_ub_is_0(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when upper bound is 0.0.
        """
        self.assertRaises(AssertionError, log_scale, 0.1, 0, 10)

    def test_log_scale_raises_when_bounds_are_0(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when lower bound and upper bound are both 0.0.
        """
        self.assertRaises(AssertionError, log_scale, 0, 0, 10)

    def test_log_scale_raises_when_lb_gt_ub(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when lower bound > the upper bound.
        """
        self.assertRaises(AssertionError, log_scale, 0.1, 0.01, 10)

    def test_log_scale_raises_when_lb_eq_ub(self):
        """
        This test ensures that :py:function:`utils.log_scale` raises
        errors when lower bound == upper bound
        """
        self.assertRaises(AssertionError, log_scale, 0.1, 0.1, 10)


#!/usr/bin/env python3
#############################################
#                                           #
# Test module for Edge2.py                  #
# Author: ES Alexander                      #
# Date: 06/Apr/2019                         #
# Modified: 07/Nov/2019                     #
#                                           #
#############################################
from testrun.TestRun import TestRun
import sys
sys.path.append('..') # allow Edge2 to be detected
from edgy_lines.Edge2 import *

class EdgeTests(TestRun):
    ''' A class for testing the Edge class methods. '''
    def test_is_point(self):
        ''' Tests the 'is_point' method. '''
        assert Edge.is_point([0,0,0,0]), "Should have been point."
        assert not Edge.is_point([0,0,1,1]), "Should not have been point."

    def test_get_line_points(self):
        ''' Tests the 'get_line_points' method. '''
        assert (Edge.get_line_points(np.array([[0,0,1,1]]),0) ==\
                np.array([[0,0],[1,1]])).all()

    def test_distsq(self):
        ''' Tests the 'distsq' method. '''
        assert Edge.distsq(np.array([0,0]),np.array([0,1])) == 1,\
               "Dist should have been 1."

    def test_get_line(self):
        ''' '''
        res = Edge.get_line(np.array([[0,0],[0,1],[0,2],[0,3]]))
        assert (res == np.array([0,0,0,3])).all(), "{}".format(res)

    def test_equal_lines(self):
        ''' '''
        assert Edge.equal_lines(np.array([0,0,0,1]),np.array([0,1,0,0]))
        assert not Edge.equal_lines(np.array([0,1,8,2]),np.array([3,4,5,6]))

    def test_add_new_lines(self):
        ''' '''
        assert (Edge.add_new_lines(np.array([[0,0,0,1]]),
                                   np.array([0,0,0,1])) == \
                np.array([[0,0,0,1]])).all()
        assert (Edge.add_new_lines(np.array([[0,0,0,1]]),
                                   np.array([0,0,0,2])) == np.array([[0,0,0,1],
                                                             [0,0,0,2]])).all()

    def test_duplicate_point(self):
        ''' '''
        assert Edge.duplicate_point([[1,1],[1,1]]), "[1,1] == [1,1]"
        assert not Edge.duplicate_point([[1,2],[1,1]]), "[1,2] != [1,1]"

    def test_line_angle(self):
        ''' '''
        assert Edge.line_angle([0,0,0,1]) == 90
        assert Edge.line_angle([0,0,1,1]) == 45
        assert Edge.line_angle([0,0,1,0]) == 0

    def test_angle_between_lines(self):
        ''' '''
        assert Edge.angle_between_lines([0,0,0,1],[0,0,1,0]) == -90

    def test_dist_point_to_segment(self):
        ''' '''
        assert Edge.dist_point_to_segment(np.array([0,0]), np.array([0,0]),
                                          np.array([0,1])) == 0
        assert Edge.dist_point_to_segment(np.array([0,0]), np.array([1,0]),
                                          np.array([1,0])) == 1
        assert Edge.dist_point_to_segment(np.array([0,0]), np.array([0,1]),
                                          np.array([1,1])) == 1

    def test_min_dist_segments(self):
        ''' '''
        res = Edge.min_dist_segments(np.array([[0,0,0,1],[1,0,2,1]]))
        assert res == 1, "{}".format(res)

    def test_offset_line(self):
        ''' '''
        assert (Edge.offset_line(np.array([0,0,0,1]),np.array([1,2])) ==\
                np.array([1,2,1,3])).all()

    def test_get_intersection_points(self):
        ''' '''
        res = Edge.get_intersection_points(
            np.array([[[0,1],[1,0]],[[0,2],[2,0]]]), np.array([[0,1],[1,0]]))
        assert (res == np.array([[1,2]])).all(), \
            '[[[0,1],[1,0]]],[[0,2],[2,0]]] became ' + str(ret) + ', not ' +\
            '[[1,2]]'

    def test_get_intersections(self):
        ''' '''
        assert (Edge.get_intersections(np.array([[0,0,0,1],[1,0,1,1]])) ==\
                   np.array([[0,0],[0,0]])).all()
        assert (Edge.get_intersections(np.array([[-1,0,1,0],[0,1,0,-1]])) ==\
                   np.array([[0,1],[1,0]])).all()

    def test_get_joined_lines(self):
        ''' '''
        pass

    def test_reduce_lines(self):
        ''' '''
        pass

if __name__ == '__main__':
    Tests = EdgeTests()
    Tests.run_failed_tests()

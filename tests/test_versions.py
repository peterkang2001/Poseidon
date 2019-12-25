#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-18
"""

from poseidon.core.version import *
from poseidon.core.version_types import Types


class TestPathInfo:
    def test_get_old_version(self):
        version = get_old_version()
        assert version != None

    def test_new_version_major(self):
        """Types.Major + 1"""
        _old_major_version = get_old_version().split(".")[0]
        _new_major_version = get_new_version(version_type=Types.Major).split(".")[0]
        assert int(_old_major_version) + 1 == int(_new_major_version)

    def test_new_version_major_step2(self):
        """Types.Major + 2"""
        _old_major_version = get_old_version().split(".")[0]
        _new_major_version = get_new_version(version_type=Types.Major, step=2).split(".")[0]
        assert int(_old_major_version) + 2 == int(_new_major_version)

    def test_new_version_minor(self):
        """Types.Minor + 1"""
        _old_minor_version = get_old_version().split(".")[1]
        _new_minor_version = get_new_version(version_type=Types.Minor).split(".")[1]
        assert int(_old_minor_version) + 1 == int(_new_minor_version)

    def test_new_version_minor_step2(self):
        """Types.Minor + 2"""
        _old_minor_version = get_old_version().split(".")[1]
        _new_minor_version = get_new_version(version_type=Types.Minor, step=2).split(".")[1]
        assert int(_old_minor_version) + 2 == int(_new_minor_version)

    def test_new_version_revision(self):
        """Types.Revision + 1"""
        _old_revision_version = get_old_version().split(".")[2]
        _old_revision_version = _old_revision_version.split("_")[0]
        _new_revision_version = get_new_version(version_type=Types.Revision).split(".")[2]
        _new_revision_version = _new_revision_version.split("_")[0]
        assert int(_old_revision_version) + 1 == int(_new_revision_version)

    def test_new_version_revision_step2(self):
        """Types.Revision + 2"""
        _old_revision_version = get_old_version().split(".")[2]
        _old_revision_version = _old_revision_version.split("_")[0]
        _new_revision_version = get_new_version(version_type=Types.Revision, step=2).split(".")[2]
        _new_revision_version = _new_revision_version.split("_")[0]
        assert int(_old_revision_version) + 2 == int(_new_revision_version)

    def test_new_version_build(self):
        """Test build"""
        _old_build_version = get_new_version().split("_")[1]
        _first, _second = _old_build_version.split("-")
        assert _first == "build"
        assert _second != None

    def test_new_version_alpha(self):
        """Types.Alpha"""
        _suffix = get_new_version(suffix=Types.Alpha)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.Alpha.name

    def test_new_version_beta(self):
        """Types.Beta"""
        _suffix = get_new_version(suffix=Types.Beta)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.Beta.name

    def test_new_version_rc(self):
        """Types.RC"""
        _suffix = get_new_version(suffix=Types.RC)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.RC.name

    def test_new_version_ga(self):
        """Types.GA"""
        _suffix = get_new_version(suffix=Types.GA)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.GA.name

    def test_new_version_m1(self):
        """Types.M1"""
        _suffix = get_new_version(suffix=Types.M1)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.M1.name

    def test_new_version_m2(self):
        """Types.M2"""
        _suffix = get_new_version(suffix=Types.M2)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.M2.name

    def test_new_version_m3(self):
        """Types.M3"""
        _suffix = get_new_version(suffix=Types.M3)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.M3.name

    def test_new_version_snapshot(self):
        """Types.SNAPSHOT"""
        _suffix = get_new_version(suffix=Types.SNAPSHOT)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.SNAPSHOT.name

    def test_new_version_pre(self):
        """Types.PRE"""
        _suffix = get_new_version(suffix=Types.PRE)
        _suffix = _suffix.split("_")[-1]
        assert _suffix == Types.PRE.name


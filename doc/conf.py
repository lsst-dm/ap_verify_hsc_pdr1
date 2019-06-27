"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.ap.verify.hsc.pdr1


_g = globals()
_g.update(build_package_configs(
    project_name='ap_verify_hsc_pdr1',
    version=lsst.ap.verify.hsc.pdr1.version.__version__))

# Copyright 2014-2016, Tresys Technology, LLC
# Copyright 2016-2017, Chris PeBenito <pebenito@ieee.org>
#
# This file is part of SETools.
#
# SETools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1 of
# the License, or (at your option) any later version.
#
# SETools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SETools.  If not, see
# <http://www.gnu.org/licenses/>.
#
# Create a Python representation of the policy.
# The idea is that this is module provides convenient
# abstractions and methods for accessing the policy
# structures.

from . import exception

from .libpolicyrep import BoundsRuletype, ConstraintRuletype, DefaultRuletype, DefaultValue, \
                          DefaultRangeValue, FSUseRuletype, HandleUnknown, IoctlSet, \
                          IomemconRange, IoportconRange, MLSRuletype, NodeconIPVersion, \
                          PolicyTarget, PortconProtocol, PortconRange, RBACRuletype, \
                          SELinuxPolicy, TERuletype

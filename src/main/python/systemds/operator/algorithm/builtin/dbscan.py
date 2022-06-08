# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/dbscan.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def dbscan(X: Matrix,
           **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    Implements the DBSCAN clustering algorithm using Euclidian distance matrix
    
    
    :param X: The input Matrix to do DBSCAN on.
    :param eps: Maximum distance between two points for one to be considered reachable for the other.
    :param minPts: Number of points in a neighborhood for a point to be considered as a core point
        (includes the point itself).
    :return: 'OperationNode' containing 
        clustering matrix 
    """
    params_dict = {'X': X}
    params_dict.update(kwargs)
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    vX_2 = Scalar(X.sds_context, '')
    output_nodes = [vX_0, vX_1, vX_2, ]

    op = MultiReturn(X.sds_context, 'dbscan', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]
    vX_2._unnamed_input_nodes = [op]

    return op

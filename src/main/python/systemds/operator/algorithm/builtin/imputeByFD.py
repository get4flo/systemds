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
# Autogenerated From : scripts/builtin/imputeByFD.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def imputeByFD(X: Matrix,
               Y: Matrix,
               threshold: float,
               **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    Implements builtin for imputing missing values from observed values (if exist) using robust functional dependencies
    
    
    :param X: Vector X, source attribute of functional dependency
    :param Y: Vector Y, target attribute of functional dependency and imputation
    :param threshold: threshold value in interval [0, 1] for robust FDs
    :param verbose: flag for printing verbose debug output
    :return: 'OperationNode' containing 
        vector y, with missing values mapped to a new max valuevector y, with imputed missing values 
    """
    params_dict = {'X': X, 'Y': Y, 'threshold': threshold}
    params_dict.update(kwargs)
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    output_nodes = [vX_0, vX_1, ]

    op = MultiReturn(X.sds_context, 'imputeByFD', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]

    return op

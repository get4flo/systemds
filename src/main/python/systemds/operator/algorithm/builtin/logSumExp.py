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
# Autogenerated From : scripts/builtin/logSumExp.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def logSumExp(M: Matrix,
              **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    Built-in LOGSUMEXP
    
    
    :param M: matrix to perform Log sum exp on.
    :param margin: if the logsumexp of rows is required set margin = "row"
        if the logsumexp of columns is required set margin = "col"
        if set to "none" then a single scalar is returned computing logsumexp of matrix
    :return: 'OperationNode' containing 
        a 1*1 matrix, row vector or column vector depends on margin value 
    """
    params_dict = {'M': M}
    params_dict.update(kwargs)
    return Matrix(M.sds_context,
        'logSumExp',
        named_input_nodes=params_dict)

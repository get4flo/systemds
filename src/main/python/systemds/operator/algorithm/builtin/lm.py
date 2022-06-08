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
# Autogenerated From : scripts/builtin/lm.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def lm(X: Matrix,
       y: Matrix,
       **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    The lm-function solves linear regression using either the direct solve method or the conjugate gradient
    algorithm depending on the input size of the matrices (See lmDS-function and lmCG-function respectively).
    
    
    :param X: Matrix of feature vectors.
    :param y: 1-column matrix of response values.
    :param icpt: Intercept presence, shifting and rescaling the columns of X
    :param reg: Regularization constant (lambda) for L2-regularization. set to nonzero
        for highly dependant/sparse/numerous features
    :param tol: Tolerance (epsilon); conjugate gradient procedure terminates early if L2
        norm of the beta-residual is less than tolerance * its initial norm
    :param maxi: Maximum number of conjugate gradient iterations. 0 = no maximum
    :param verbose: If TRUE print messages are activated
    :return: 'OperationNode' containing 
        the model fit 
    """
    params_dict = {'X': X, 'y': y}
    params_dict.update(kwargs)
    return Matrix(X.sds_context,
        'lm',
        named_input_nodes=params_dict)

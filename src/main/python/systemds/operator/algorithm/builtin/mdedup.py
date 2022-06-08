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
# Autogenerated From : scripts/builtin/mdedup.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def mdedup(X: Frame,
           LHSfeatures: Matrix,
           LHSthreshold: Matrix,
           RHSfeatures: Matrix,
           RHSthreshold: Matrix,
           verbose: bool):
    """
    Implements builtin for deduplication using matching dependencies (e.g. Street 0.95, City 0.90 -> ZIP 1.0)
    and Jaccard distance.
    
    
    
    :param X: Input Frame X
    :param LHSfeatures: A matrix 1xd with numbers of columns for MDs
        (e.g. Street 0.95, City 0.90 -> ZIP 1.0)
    :param LHSthreshold: A matrix 1xd with threshold values in interval [0, 1] for MDs
    :param RHSfeatures: A matrix 1xd with numbers of columns for MDs
    :param RHSthreshold: A matrix 1xd with threshold values in interval [0, 1] for MDs
    :param verbose: To print the output
    :return: 'OperationNode' containing 
        matrix nx1 of duplicates 
    """
    params_dict = {'X': X, 'LHSfeatures': LHSfeatures, 'LHSthreshold': LHSthreshold, 'RHSfeatures': RHSfeatures, 'RHSthreshold': RHSthreshold, 'verbose': verbose}
    return Matrix(X.sds_context,
        'mdedup',
        named_input_nodes=params_dict)

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
# Autogenerated From : scripts/builtin/img_mirror.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def img_mirror(img_in: Matrix,
               horizontal_axis: bool):
    """
    This function is an image data augmentation function.
    It flips an image on the X (horizontal) or Y (vertical) axis.
    
    
    :param img_in: Input matrix/image
    :param max_value: The maximum value pixels can have
    :return: 'OperationNode' containing 
        flipped matrix/image 
    """
    params_dict = {'img_in': img_in, 'horizontal_axis': horizontal_axis}
    return Matrix(img_in.sds_context,
        'img_mirror',
        named_input_nodes=params_dict)

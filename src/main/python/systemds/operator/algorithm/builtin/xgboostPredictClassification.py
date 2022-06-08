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
# Autogenerated From : scripts/builtin/xgboostPredictClassification.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def xgboostPredictClassification(X: Matrix,
                                 M: Matrix,
                                 **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting. This xgboost
    implementation supports classification  and is capable of working with categorical features.
    
    
    :param X: Matrix of feature vectors we want to predict (X_test)
    :param M: The model created at xgboost
    :param learning_rate: The learning rate used in the model
    :return: 'OperationNode' containing 
        the predictions of the samples using the given xgboost model. (y_prediction) 
    """
    params_dict = {'X': X, 'M': M}
    params_dict.update(kwargs)
    return Matrix(X.sds_context,
        'xgboostPredictClassification',
        named_input_nodes=params_dict)
